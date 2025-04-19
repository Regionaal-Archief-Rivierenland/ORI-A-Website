#!/bin/python

from jinja2 import Environment, FileSystemLoader
from bs4 import BeautifulSoup
import frontmatter

import re
import glob

pages_folder = "pages"
html_folder = "pages"
output_folder = "site"

# file that will serve as index.html
main_page = "main.html" 

env = Environment(loader=FileSystemLoader("templates"))
base_template = env.get_template("base.html")
navbar_template = env.get_template("navbar.html")
logo = env.get_template("logo.html")

def pageinfo(filestem):
    """Build pageinfo (title, etc.) from markdown YAML frontmatter and pandoc html"""

    # get title from YAML frontmatter
    doc = frontmatter.load(filestem+".md")
    title = doc.metadata['title']
    position = int(doc.metadata['position'])
    hide = bool(doc.metadata.get('hide_from_navigation', False))
    
    # findall <h1> headers (and their anchors)
    with open(filestem+".html", 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')

    headers = []
    if title != "FAQ":
        for header in soup.find_all('h1'):
            # pandoc generates anchors automatically!
            anchor = header.get('id')
            if anchor:
                headers.append((header.text, anchor))

    return {
        "title": title,
        "position": position,
        "hide": hide,
        "filename": f"{filestem.removeprefix(f"{pages_folder}/")}.html",
        "headers": headers
    }

def add_icon_to_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all("a", href=re.compile(r"^https?://"))

    for link in links:
        link["class"] = ["external"]

    return str(soup)

def colorize_inline_xml(html):
    soup = BeautifulSoup(html, 'html.parser')
    code_tags = soup.find_all("code", string=re.compile(r"^<.*>$"))

    for code in code_tags:
        code["class"] = "sourceCode xml"
        # FIXME: I think you can do this extraction with regexs?
        content = code.string[1:-1]  # Extract inner text (without < and >)
        
        # Create a new <span class="kw"> element
        span = soup.new_tag("span", **{"class": "kw"})
        span.string = content  # Set its text content

        # Rebuild the code tag with the new structure
        code.clear()
        code.append("<")
        code.append(span)
        code.append(">")


    return str(soup)

def anchor_icon_to_headers(html):
    soup = BeautifulSoup(html, 'html.parser')
    headers = soup.find_all(re.compile('^h[1-6]$'))
    for h in headers:
        a = soup.new_tag("a", **{"href": f"#{h['id']}", "class" : "secondary", "aria-hidden" : "true"})
        a.append("#")
        h.append(a)
    return str(soup)

# TODO: this should probably 
def headers_to_accordions(html):
    soup = BeautifulSoup(html, 'html.parser')
    h1s = soup.find_all("h1")

    # Section for the title
    title_section = soup.new_tag("section")
    new_title = soup.new_tag("h1", id="FAQ")
    new_title.string = "Veel gestelgde vragen"
    title_section.append(new_title)

    # Section for the accordions
    details_section = soup.new_tag("section")

    for idx, h in enumerate(h1s):
        details = soup.new_tag("details")
        # if idx == 0:
        #     details.attrs["open"] = "true"

        summary = soup.new_tag("summary")
        summary.string = h.get_text()
        details.append(summary)

        # Collect siblings until next h1
        sibling = h.find_next_sibling()
        while sibling and sibling.name != "h1":
            next_sibling = sibling.find_next_sibling()
            details.append(sibling.extract())
            sibling = next_sibling

        details_section.append(details)

        if idx < len(h1s) - 1:
            hr = soup.new_tag("hr")
            details_section.append(hr)

        h.decompose()

    # Insert the two sections at the top of the document
    soup.insert(0, details_section)
    soup.insert(0, title_section)

    return str(soup)
    


pages = []

for md_file in glob.glob(f"{pages_folder}/*.md"):
    pages.append(pageinfo(md_file.removesuffix('.md')))

# sort pages according to their position key in the YAML frontmatter
pages = sorted(pages, key=lambda p: p["position"])

for page in pages:
    # read pandoc-converted HTML file
    with open(f"{html_folder}/{page['filename']}", 'r') as f:
        page_contents = f.read()

    with open(f"{output_folder}/sun.svg") as f:
        sunsvg = f.read()

    with open(f"{output_folder}/github.svg") as f:
        githubsvg = f.read()
        
    with open(f"{output_folder}/hamburger.svg") as f:
        hamburgersvg = f.read()
        
    with open(f"{output_folder}/moon.svg") as f:
        moonsvg = f.read()

    # process html
    page_contents = add_icon_to_links(page_contents)
    page_contents = colorize_inline_xml(page_contents)
    if page["title"] == "FAQ":
        page_contents = headers_to_accordions(page_contents)
    page_contents = anchor_icon_to_headers(page_contents)
    
    # this needs current_page because that visited page needs to styled in the navbar
    logo_html = logo.render()
    navbar_html = navbar_template.render(
        # don't add colofon/pages with hide_from_nav to navbar
        pages=[p for p in pages if not p["hide"]],
        current_page=page["filename"])
    html = base_template.render(
        logo=logo_html,
        content=page_contents,
        navbar=navbar_html,
        title=page["title"],
        sunsvg=sunsvg,
        moonsvg=moonsvg,
        githubsvg=githubsvg,
        hamburgersvg=hamburgersvg,
        current_page=page["filename"],
    )

    with open(f"{output_folder}/{page["filename"]}", 'w') as f:
        f.write(html)
