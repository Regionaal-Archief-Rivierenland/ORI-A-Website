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
    """Convert <xs:complexType> to a markdown table"""
    rows = []
    tooltips = {
        "string": "Reeks van tekens",
        "boolean": "true of false",
        "date": "YYYY-MM-dd",
        "dateTime": "YYYY-MM-DDThh:mm:ss, bijv. 2012-05-15T13:20:00",
        "enumeratie": "Lijst van keuzes",
        "integerOfTijdstempel": "Getal of tijdsstempel (hh:mm:ss)",
        "positiveInteger": "Positief getal",
    }

    for elem in complextype.findall(".//xs:element", namespaces=ns):
        docstring = elem.find(".//xs:documentation", namespaces=ns).text
        naam = elem.attrib["name"]

        # long elem names mess up the table, so add a wordbreak
        # suggestion to the final word
        if len(naam) >= 22:
            words = camel_to_seperate_words(naam)
            naam_wbr = "".join(words[:-1]) + "<wbr/>" + words[-1]
        else:
            naam_wbr = naam


        verplicht = bool(int(elem.attrib["minOccurs"]))
        herhaalbaar = True if elem.attrib["maxOccurs"] == "unbounded" else False
        # assume enumaration if type is not specified
        # FIXME: this assumption is wrong in case of regexes
        datatype = elem.attrib.get("type", "enumeratie").replace("xs:", "")

        opties = []
        # change datatype to "keuze uit: `X`, `Y`, `...`"  if enumeratie
        if datatype == "enumeratie":
            for optie in elem.findall(".//xs:enumeration", namespaces=ns):
                opties.append(optie.attrib["value"])

        seperate_words = camel_to_seperate_words(datatype)

        if datatype in gegevensgroepen_names:
            # this is pandoc's anchro link fmt
            datatype_url = f"#{"-".join(seperate_words).lower()}"
        else:
            datatype_url = None

        if datatype in tooltips.keys():
            datatype_tooltip = tooltips[datatype]
        else:
            datatype_tooltip = None

        # insert places to break words
        if datatype == "dagelijksBestuurLidmaatschapGegevens":
            # make an exception for dagelijksbestuurlidmaatschapgegevens,
            # as breaking it at every word looks pretty bad
            datatype_wbr = "dagelijksBestuur<wbr/>LidmaatschapGegevens"
            width_class = f"code-ch-{len('LidmaatschapGegevens') + 2}" 
        else:
            datatype_wbr = "<wbr/>".join(seperate_words)
            # find longest word in datatype. This is used later on to set
            # inline code boxes to an appropiate width (yes, this needs to
            # happen manually; tho only to make sure that these boxes look
            # right when word wrapping occurs)
            maxlen = max(len(w) for w in seperate_words)
            # add 2ch to account for padding? in any case, some kind of increment is needed
            maxlen = maxlen + 2
            # associate maxlen with a css class
            width_class = f"code-ch-{maxlen}"

        rows.append(
            {
                "naam": naam,
                "naam_wbr": naam_wbr,
                "toelichting": docstring,
                "datatype": datatype,
                "datatype_wbr": datatype_wbr,
                "datatype_width_class": width_class,
                "datatype_url": datatype_url,
                "datatype_tooltip": datatype_tooltip,
                "herhaalbaar": herhaalbaar,
                "verplicht": verplicht,
                "opties": opties,
            }
        )

    return rows

outfile = "pages/documentatie.md"
# Setup environment with whitespace control
env = Environment(
    loader=FileSystemLoader(["pages", "templates"]),
    trim_blocks=True,
    lstrip_blocks=True,
)

documentatie_template = env.get_template("documentatie.md.j2")
table_template = env.get_template("gegevensgroep_table.html")

# to be passed as kwards to jinja
all_tables = {}

for name, elem in zip(gegevensgroepen_names, gegevensgroepen_elems):
    rows = complextype_to_dict(elem)
    # e.g. verwijzingGegevens → ['verwijzing', 'Gegevens']
    name_seperate_words = camel_to_seperate_words(name)
    pretty_name = " ".join([name_seperate_words[0].capitalize()] + [n.lower() for n in name_seperate_words[1:]])
    snake_case_name = "_".join(name_seperate_words[:-1] + ["table"]).lower()
    html_table = table_template.render(rows=rows, table_title=pretty_name)
    # add place to word break
    all_tables[snake_case_name] = html_table

md_with_html_tables = documentatie_template.render(**all_tables)
# this string must be removed for the yaml frontmatter syntactically correct
md_with_html_tables = md_with_html_tables.replace('<!-- -*- mode: markdown -*- -->', '')

with open(outfile, "w") as f:
    f.write(md_with_html_tables)
