#!/bin/python

import xml.etree.ElementTree as ET
import re

from jinja2 import FileSystemLoader, Environment

ns = {"xs": "http://www.w3.org/2001/XMLSchema"}
# this dir is a git submodule
root = ET.parse("ORI-A-XSD/ORI-A.xsd").getroot()

gegevensgroepen_elems = [e for e in root.findall(".//xs:complexType", namespaces=ns)]
# the first complextype, ORI-A, does not have a name attribute
gegevensgroepen_names = ["ORI-AGegevens"] + [
    e.attrib["name"] for e in gegevensgroepen_elems[1:]
]

def camel_to_seperate_words(string) -> list[str]:
    """Convert camel cased string to a list of words"""
    return re.sub('([A-Z][a-z]+)', r' \1', string).split()

def add_wbr_to_camel_case(string):
    return re.sub(r'(?<!^)(?=[A-Z])', '<wbr>', string)

def complextype_to_dict(complextype: ET.Element) -> list[dict]:
    """
    Convert <xs:complexType> to a list of fat dicts, holding
    information about each gegevensgroep.
    """
    rows = []
    tooltips = {
        "string": "Reeks tekens",
        "anyURI": "Link naar een webpagina",
        "boolean": "true of false",
        "date": "YYYY-MM-dd",
        "dateTime": "YYYY-MM-DDThh:mm:ss",
        "enumeratie": "Lijst van keuzes",
        "integerOfTijdcode": "Getal of tijdcode (hh:mm:ss)",
        "positiveInteger": "Positief getal",
        "nonNegativeInteger": "Getal boven of gelijk aan 0",
    }

    for elem in complextype.findall(".//xs:element", namespaces=ns):
        docstring = elem.find(".//xs:documentation", namespaces=ns).text
        naam = elem.attrib["name"]

        # long elem names mess up the table, so add a wordbreak
        # suggestion to the final word
        if len(naam) >= 22:
            words = camel_to_seperate_words(naam)
            naam_wbr = "".join(words[:-1]) + "<wbr>" + words[-1]
        else:
            naam_wbr = naam

        verplicht = bool(int(elem.attrib["minOccurs"]))
        herhaalbaar = True if elem.attrib["maxOccurs"] == "unbounded" else False
        # assume enumaration if type is not specified
        # FIXME: this assumption is wrong in case of regexes
        datatype = elem.attrib.get("type", None)
        enumeratie_naam = None
        # In XSD, restrictions do not set `type=`, so we need to look at info within the restriction
        if not datatype:
            if len(elem.findall(".//xs:enumeration", namespaces=ns)) > 1:
                datatype = "enumeratie"
                # this is just a copy of the name of the element
                enumeratie_naam = str(naam)
            else:
                datatype = "string"

        datatype = datatype.replace("xs:", "")

        opties = []
        # change datatype to "keuze uit: `X`, `Y`, `...`"  if enumeratie
        if datatype == "enumeratie":
            for optie in elem.findall(".//xs:enumeration", namespaces=ns):
                opties.append(optie.attrib["value"])

        # construct "pretty" (i.e. normal dutch) variants of datatypes names
        if datatype == "date":
            datatype_pretty = "datum"
        elif datatype == "dateTime":
            datatype_pretty = "datum + tijd"
        elif datatype == "anyURI":
            datatype_pretty = "URL"
        elif datatype == "integerOfTijdstempel":
            datatype_pretty = "integer of tijd"
        elif datatype == "language":
            datatype_pretty = "taal"
        else:
            datatype_pretty = str(datatype)

        datatype_seperate_words = camel_to_seperate_words(datatype)
        naam_seperate_words = camel_to_seperate_words(naam)

        if datatype in gegevensgroepen_names:
            # strip -Gegevens suffix, except in some cases
            slice_index = None
            if not datatype in ["verwijzingGegevens", "begripGegevens", "informatieobjectGegevens"]:
                slice_index = -1

            # this is pandoc's anchor link fmt
            datatype_url = f"#{'-'.join(datatype_seperate_words[0:slice_index]).lower()}"
        else:
            datatype_url = None

        if datatype in tooltips.keys():
            datatype_tooltip = tooltips[datatype]
        else:
            datatype_tooltip = None

        # adding a lil extra padding to the box looks better
        extra_box_padding = 2

        # insert places to break words with <wbr>

        # make an exception for dagelijksbestuurlidmaatschapgegevens,
        # as breaking it at every word looks pretty bad
        # (and same for stemmingOverPersonenGegevens)
        if datatype == "dagelijksBestuurLidmaatschapGegevens":
            datatype_wbr = "dagelijksBestuur<wbr>LidmaatschapGegevens"
            width_class = f"code-ch-{len('LidmaatschapGegevens') + extra_box_padding}"
        elif datatype == "stemmingOverPersonenGegevens":
            datatype_wbr = "stemmingOver<wbr>PersonenGegevens"
            width_class = f"code-ch-{len('PersonenGegevens') + extra_box_padding}"
        else:
            datatype_wbr = "<wbr>".join(datatype_seperate_words)
            # find longest word in datatype. This is used later on to set
            # inline code boxes to an appropiate width (yes, this needs to
            # happen manually; tho only to make sure that these boxes look
            # right when word wrapping occurs)
            maxlen = max(len(w) for w in datatype_seperate_words)
            # add 2ch to account for padding? in any case, some kind of increment is visually nicer
            maxlen = maxlen + extra_box_padding
            # associate maxlen with a css class
            width_class = f"code-ch-{maxlen}"

        # e.g. Dagelijksbestuur lidmaatschap gegevens
        naam_pretty = " ".join(w.lower() for w in naam_seperate_words).capitalize()
        if naam == "ID":
            naam_pretty = "ID"

        rows.append(
            {
                "naam": naam,
                "naam_pretty": naam_pretty,
                "naam_wbr": naam_wbr,
                "enumeratie_naam": enumeratie_naam,
                "toelichting": docstring,
                "datatype": datatype,
                "datatype_wbr": datatype_wbr,
                "datatype_width_class": width_class,
                "datatype_pretty": datatype_pretty,
                "datatype_url": datatype_url,
                "datatype_tooltip": datatype_tooltip,
                "herhaalbaar": herhaalbaar,
                "verplicht": verplicht,
                "opties": opties,
            }
        )

    return rows


outfile = "pages/xml-schema.md"
outfile_diagram = "diagram/ORI-A-diagram.tex"
# Setup environment with whitespace control
env = Environment(
    loader=FileSystemLoader(["pages", "templates", "diagram"]),
    trim_blocks=True,
    lstrip_blocks=True,
)

documentatie_template = env.get_template("xml-schema.md.j2")
table_template = env.get_template("gegevensgroep_table.html")

diagram_template = env.get_template("ORI-A-diagram.tex.j2")

# to be passed as kwards to jinja
all_tables_html = {}
all_tables = {} # more general struct; used in latex

for gegevensgroep_name, elem in zip(gegevensgroepen_names, gegevensgroepen_elems):
    rows = complextype_to_dict(elem)
    # e.g. verwijzingGegevens → ['verwijzing', 'Gegevens']
    gegevensgroep_seperate_words = camel_to_seperate_words(gegevensgroep_name)

    # remove -Gegevens suffix, sometimes
    slice_index = None
    if not gegevensgroep_name in ["verwijzingGegevens", "begripGegevens", "informatieobjectGegevens"]:
        slice_index = -1

    gegevensgroep_pretty = " ".join(w.lower() for w in gegevensgroep_seperate_words[0:slice_index]).capitalize()
    snake_case_name = "_".join(gegevensgroep_seperate_words[:-1] + ["table"]).lower()
    snake_case_name = snake_case_name.replace("ori-a", "ori_a")
    html_table = table_template.render(rows=rows, table_title=gegevensgroep_pretty)
    all_tables_html[snake_case_name] = html_table
    all_tables[snake_case_name] = rows

md_with_html_tables = documentatie_template.render(**all_tables_html)
# this string must be removed for the yaml frontmatter to be syntactically correct
md_with_html_tables = md_with_html_tables.replace('<!-- -*- mode: markdown -*- -->', '')
diagram_rendered = diagram_template.render(**all_tables)
diagram_rendered = diagram_rendered.replace('<!-- -*- mode: LaTex -*- -->', '')

with open(outfile, "w") as f:
    f.write(md_with_html_tables)

with open(outfile_diagram, "w") as f:
    f.write(diagram_rendered)
