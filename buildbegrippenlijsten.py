#!/usr/bin/python3

from pathlib import Path
from jinja2 import FileSystemLoader, Environment
from rdflib import Graph, SKOS, RDF, OWL, DCTERMS

def build_label(concept, g):
    """Recursively prepend broader concept labels, e.g. 'A | B | C'."""
    label = g.value(concept, SKOS.prefLabel)

    if broader := g.value(concept, SKOS.broader):
        return f"{build_label(broader, g)} | {label}"
    else:
        return label

env = Environment(
    loader=FileSystemLoader(["pages", "templates"]),
    trim_blocks=True,
    lstrip_blocks=True,
)

begrippenlijsten_page_template = env.get_template("begrippenlijsten.md.j2")
table_template = env.get_template("begrippenlijst_table.md")
all_tables = {}

for ttl in Path("ori-a-begrippenlijsten").glob("*.ttl"):
    g = Graph()
    g.parse(ttl)

    begrippenlijst = next(g.subjects(RDF.type, SKOS.ConceptScheme))
    begrippenlijst_naam = (
        g.value(begrippenlijst, DCTERMS.title)
        .lower()
        .replace(" ", "_")
        .replace("-", "_")
    )
    begrippen = []

    # FIXME: does this create a stable ordering?
    for concept in g.subjects(RDF.type, SKOS.Concept):
        begrippen.append(
            {
                "label": build_label(concept, g),
                # empty definitions are rendered as a hyphen
                "definition": g.value(concept, SKOS.definition) or "-",
                "altLabels": g.value(concept, SKOS.altLabel),
                "deprecated": bool(g.value(concept, OWL.deprecated)),
            }
        )

    md_table = table_template.render(begrippenlijst=begrippen)
    all_tables[f"{begrippenlijst_naam}_table"] = md_table

begrippenlijsten_page = begrippenlijsten_page_template.render(**all_tables)
begrippenlijsten_page = begrippenlijsten_page.replace("<!-- -*- mode: markdown -*- -->", "")

with open("pages/begrippenlijsten.md", "w") as f:
    f.write(begrippenlijsten_page)
