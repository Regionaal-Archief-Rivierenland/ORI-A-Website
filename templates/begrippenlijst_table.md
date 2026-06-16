+---------------+---------------+
| Label         | Definitie     |
+===============+===============+
{% for begrip in begrippenlijst  %}
| {{ "<del>" + begrip.label + "</del>" if begrip.deprecated else begrip.label | replace("|", "\|")}} | {{ begrip.definition }} |
+---------------+---------------+
{% endfor %}
