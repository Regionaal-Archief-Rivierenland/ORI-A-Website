#!/bin/python

from jinja2 import Environment, FileSystemLoader
from bs4 import BeautifulSoup
import frontmatter

import re
import glob

pages_folder = "pages"
icons_folder = "site"
html_folder = "pages"
output_folder = "site"

env = Environment(loader=FileSystemLoader("templates"), trim_blocks=True, lstrip_blocks=True)
base_template = env.get_template("base.html")
navbar_template = env.get_template("navbar.html")
navbar_nested_template = env.get_template("navbar_nested.html")
logo = env.get_template("logo.html")


def pageinfo(filestem):
    """Build pageinfo (title, etc.) from markdown YAML frontmatter and pandoc html"""

    # get title from YAML frontmatter
    doc = frontmatter.load(filestem + ".md")
    title = doc.metadata["title"]
    title_icon = doc.metadata.get('title-icon', None)
    position = int(doc.metadata.get("position", 0))
    hide = bool(doc.metadata.get("hide_from_navigation", False))

    # findall <h1> headers (and their anchors)
    with open(filestem + ".html", "r") as f:
        soup = BeautifulSoup(f, "html.parser")

    headers = []
    # dict that stores h2 info under its h1 sibling(/"parent")
    h2_by_h1 = {}
    for header in soup.find_all("h1"):
        # pandoc generates anchors automatically!
        anchor = header.get("id")
        if anchor:
            headers.append((header.text, anchor))

        h2s = []
        for sibling in header.find_next_siblings():
            if sibling.name == "h1":
                break
            if sibling.name == "h2":
                h2s.append((sibling.text, sibling.get("id")))

        h2_by_h1[header.text] = h2s

    headers_h2 = []
    for header in soup.find_all("h2"):
        # pandoc generates anchors automatically!
        anchor = header.get("id")
        if anchor:
            headers_h2.append((header.text, anchor))

    return {
        "title": title,
        "title-icon": title_icon,
        "position": position,
        "hide": hide,
        "filename": f"{filestem.removeprefix(f'{pages_folder}/')}",
        "headers": headers,
        "headers_h2": headers_h2,
        "h2_by_h1": h2_by_h1,
    }


def add_icon_to_links(html):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a", href=re.compile(r"^https?://"))

    for link in links:
        link["class"] = ["external"]

    return str(soup)

def add_title_section(html, title, icon):
    soup = BeautifulSoup(html, "html.parser")

    title_tag = soup.new_tag('h1')
    title_tag.string = title
    title_tag["class"] = "title"
    soup.insert(0, title_tag)

    if icon:
        if icon.endswith('.svg'):
            with open(f"{icons_folder}/{icon}", "r") as f:
                icon_tag = BeautifulSoup(f.read(), 'html.parser').svg
                icon_tag["aria-hidden"] = "true"
                title_tag.insert(0, icon_tag)
        elif type(icon) == str:
            # "icons" can be plain text
            span = soup.new_tag('span')
            span["aria-hidden"] = "true"
            span["role"] = "presentation"
            span.string = icon + " "
            title_tag.insert(0, span)



    hrule = soup.new_tag('hr')
    first_sibling = title_tag.find_next_sibling()
    # add hrule after first p
    if first_sibling.name == "p":
        first_sibling["class"] = "muted"
        first_sibling.insert_after(hrule)
    else:
        title_tag.insert_after(hrule)

    return str(soup)

def delete_pandoc_cruft(html):
    """
    Pandoc inserts unused <a> tags in code blocks, as well as extra
    spans and divs. This is non-configurable.
    Hence, we delete these here.
    """
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup.select("code span > a"):
        tag.decompose()

    # Unwrap spans with ids like cb3-2 inside <code>
    for span in soup.select("code span[id]"):
        if re.match(r"^cb\d+-\d+$", span["id"]):
            span.unwrap()

    for div in soup.find_all("div", class_="sourceCode"):
        div.unwrap()

    return str(soup)


def colorize_inline_xml(html):
    soup = BeautifulSoup(html, "html.parser")
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
    soup = BeautifulSoup(html, "html.parser")
    headers = soup.find_all(re.compile("^h[1-6]$"))
    for h in headers:
        a = soup.new_tag("a", **{"href": f"#{h['id']}", "class": "secondary"})
        # put the actual "icon" (the # char) in a span, to stop an accessibility issue
        s = soup.new_tag("span", **{"aria-hidden": "true"})
        a.append(s)
        s.append("#")
        h.append(a)
    return str(soup)


def headers_to_accordions(html):
    soup = BeautifulSoup(html, "html.parser")
    h1s_and_h2s = soup.find_all("h1") + soup.find_all("h2")

    for h in h1s_and_h2s:
        if not 'dropdown' in h.attrs.get("class", []):
            continue

        h_title = h.get_text().replace('#', '')

        details = soup.new_tag("details")

        summary = soup.new_tag("summary")
        summary.attrs["role"] = "button"
        summary.attrs["class"] = "outline contrast"
        summary.string = h_title
        details.append(summary)

        # Collect siblings until next header
        sibling = h.find_next_sibling()
        h1_or_h2 = sibling.name in ["h1", "h2"]
        while sibling and not h1_or_h2:
            next_sibling = sibling.find_next_sibling()
            details.append(sibling.extract())

            if not next_sibling:
                break

            h1_or_h2 = next_sibling.name in ["h1", "h2"]
            sibling = next_sibling

        h.replace_with(details)



    return str(soup)


pages = []

for md_file in glob.glob(f"{pages_folder}/*.md"):
    pages.append(pageinfo(md_file.removesuffix(".md")))

# sort pages according to their position key in the YAML frontmatter
pages = sorted(pages, key=lambda p: p["position"])

for page in pages:
    # read pandoc-converted HTML file
    with open(f"{html_folder}/{page['filename']}.html", "r") as f:
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
    page_contents = anchor_icon_to_headers(page_contents)
    page_contents = headers_to_accordions(page_contents)
    page_contents = add_title_section(page_contents, page["title"], page["title-icon"])
    page_contents = colorize_inline_xml(page_contents)


    page_contents = delete_pandoc_cruft(page_contents)

    # this needs current_page because that visited page needs to styled in the navbar
    logo_html = logo.render()
    if page["title"] in ["Het XML-schema"]:
        navbar_html = navbar_nested_template.render(
            pages=[p for p in pages if not p["hide"]],
            current_page=page["filename"],
        )
    else:
        navbar_html = navbar_template.render(
            # don't add colofon/pages with hide_from_nav to navbar
            pages=[p for p in pages if not p["hide"]],
            current_page=page["filename"],
        )

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

    with open(f"{output_folder}/{page['filename']}.html", "w") as f:
        f.write(html)
