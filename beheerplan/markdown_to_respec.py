#!/usr/bin/env python3

# adapted from https://github.com/webrecorder/markdown-to-respec

import os
import re
import sys
import json
import logging
import pathlib
import argparse
import frontmatter


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("infile", type=pathlib.Path, help="Markdown file to convert")
    parser.add_argument("-o", dest="outfile", type=pathlib.Path, help="Output HTML file")
    parser.add_argument("--branch", help="Git branch to publish to")
    parser.add_argument("--publish", action="store_true", help="Commit and push new HTML files")
    args = parser.parse_args()

    outfile = args.outfile or args.infile.with_suffix(".html")
    html_file = convert(args.infile, outfile)
    print(f"converted {args.infile} to {html_file}")

    if args.publish:
        git_push(args.branch or "gh-pages", [html_file])

def convert(markdown_file, html_file):
    html_file.open("w").write(respec(markdown_file))
    return html_file

def respec(markdown_file):
    """Generate HTML for a Markdown file (or file object).
    """
    doc = parse_markdown(markdown_file)
    return head(doc.metadata) + doc.content + foot()

def head(respec_config):
    """
    Generate the head section of the ReSpec HTML including the ReSpec
    configuration.
    """
    config_json = json.dumps(respec_config, default=str, indent=2)
    # conformance and sotd
    return f"""
<!DOCTYPE html>
<html lang="{respec_config["lang"]}">
  <head>
  <meta charset="utf-8">
  <meta name="color-scheme" content="light dark">
  <title>{respec_config["title"]}</title>
  <script src="{respec_config["respec_js"]}" class="remove" defer ></script>
  <script class="remove">
    var respecConfig = {config_json}
  </script>
  <link href="https://ori-a.nl/favicon.ico" rel="icon">
  <style>
    #logo-small {{
        background: none;
    }}
        
  </style>
  </head>
  <body>

<p class="copyright override">Dit document valt onder de volgende licentie: <a rel="license" href="https://creativecommons.org/licenses/by/4.0/legalcode" class="subfoot"><img class="license" style="float: left; padding-right: 5px; background: none" src="https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by.svg" alt="Logo Creative Commons Attribution 4.0 International Public License"><br> Creative Commons Attribution 4.0 International Public License</a>
</p>

<!-- these need to be flush left or else all the markdown gets mucked up -->
<section id="sotd" class="override introductory">
    <h2>Status van dit document</h2>
    {respec_config["sotd"]}
</section>
<section id="abstract">{respec_config["abstract"]}</section>

<!-- start of markdown text -->

"""

def foot():
    """Return the footer for the ReSpec HTML.
    """
    return """

<!-- end  of markdown text -->

  </body>
</html>"""

def parse_markdown(markdown_file):
    """
    Parse a Markdown file or file object and return a frontmatter.Post object
    If the Markdown contains no frontmatter it will look for a corresponding
    JSON file and load metadata from that instead.
    """
    doc = frontmatter.load(markdown_file)

    # if there is no frontmatter configuration look for JSON file
    if len(doc.metadata) == 0:
        doc.metadata = load_external_config(markdown_file)

    # the spec can live as markdown in the HTML as long as we tell respec
    doc.metadata['format'] = 'markdown'

    # the respec javascript
    if 'respec_js' not in doc.metadata:
        doc.metadata['respec_js'] = 'https://www.w3.org/Tools/respec/respec-w3c'

    # Ensure respec applies localization by always setting the lang attribute
    # of the <html> element. Assume a default of English, per the respec docs.
    if 'lang' not in doc.metadata:
        doc.metadata['lang'] = 'en'

    # respec requires these at least to be empty to work
    if 'logos' not in doc.metadata:
        doc.metadata['logos'] = []
    if 'authors' not in doc.metadata:
        doc.metadata['authors'] = []
    if 'title' not in doc.metadata:
        extract_title(doc)

    # These need to be <section> elements, but it's nice to have them as
    # headinged sections in the Markdown.
    extract_section(doc, 'Samenvatting', 'abstract')
    extract_section(doc, 'Conformance', 'conformance')
    extract_section(doc, 'Status van dit document', 'sotd')

    # respec doesn't really have support for footnotes? I think?
    footnotes_to_html(doc)

    return doc

def footnotes_to_html(doc):
    pass
    fnt_ref = re.search(r"\[\^(\d+)\]", doc.content)
    fnt_def = re.search(r"\[\^(\d+)\]:", doc.content)
    

def extract_title(doc):
    """Extract the title from the Markdown using the first header.
    """
    if 'title' not in doc.metadata and (m := re.search(r'# (.+?)$', doc.content, re.MULTILINE)):
        doc.metadata['title'] = m.group(1).strip()
        doc.content = doc.content.replace(m.group(0), '', 1)
    else:
        logging.warn("Unable to find title in Markdown or in frontmatter")
        doc.metadata['title'] = ''

def extract_section(doc, header, name):
    """
    Extract a given section from the Markdown. The header should be the text
    of the header to be extracted, and the name is the config name to use to
    refer to the extracted section.
    """
    pattern = re.compile(r'^#+ ' + header + r'$((?:\W|\w)+?)^#', re.MULTILINE)
    if name not in doc.metadata and (m := re.search(pattern, doc.content)):
        text = m.group(1).strip()
        doc.metadata[name] = text
        doc.content = doc.content.replace(m.group(0), '#', 1)
    else:
        doc.metadata[name] = ''

def load_external_config(markdown_file):
    """Look for an external JSON config for the given Markdown file.
    """
    json_file = markdown_file.stem + '.json'
    json_file = markdown_file.parent / json_file
    if json_file.is_file():
        return json.load(json_file.open('r'))
    else:
        raise Exception(f"Unable to find external ReSpec config at {json_file}")


if __name__ == "__main__":
    main()

