---
title: Downloads
title-icon: download.svg
position: 8
---

Hier vindt je bestanden die je helpen bij het maken, begrijpen of valideren van ORI-A metagegevens.

# XML-schema

<!-- ::: tip -->
<!-- **Tip:**  Technische feedback of vragen over de XSD kun je achterlaten op [Github](https://github.com/regionaal-archief-rivierenland/ORI-A-XSD/issues). -->
<!-- ::: -->

Het ORI-A XML-schema beschrijft de regels van valide ORI-A XML. Je kan dit schema gebruiken om te **controleren** of een XML document valide ORI-A XML bevat.

Dit schema is beschikbaar in het **XSD bestandsformaat**.

![Valideren van ORI-A XML](validatie.svg){ width=95% }


:::tip
**Tip:** Voor het valideren van XML raden we [xmllint](https://en.wikipedia.org/wiki/Libxml2) (_commandline_ programma) of [xmlschema](https://github.com/sissaschool/xmlschema) (Python pakket) aan.
:::

``` {=html}
<div class="grid download">
<select name="versie picker" aria-label="Versie" required">
  <option selected disabled value="">Versie</option>
  <option selected="selected">v1.0.0</option>
</select>

<button><span><strong>ORI-A XML schema</strong> (xsd)</span></button>
</div>
```

## Semantisch versionering {.dropdown}

Het ORI-A XML-schema houdt een vorm van [semantisch versionering](https://semver.org/lang/nl/) aan. Dit betekent dat elk fragment van een versienummer in de vorm `MAJEUR.MINEUR.PATCH` een speciale betekenis draagt:

1. `MAJEUR` wordt verhoogt bij schema wijzigingen die bestaande ORI-A XML onvalide maakt.
2. `MINEUR` wordt verhoogt wanneer functionaliteit wordt toegevoegd _zonder_ de status van bestaande ORI-A XML te veranderen (ook wel "compatibele wijzigingen").
3. `PATCH` wordt verhoogt bij compatibele _bugfixes_, zoals correcties in de documentatie.

Kort gezegd: alle XML die valide is bevonden op basis van schema versie `1.1.0` is nog steeds valide in versie `1.2.1`, maar _niet_ valide in versie `2.0.0`.

## Versie wijzigingen {.dropdown}

[Volledig overzicht van wijzigingen](https://github.com/Regionaal-Archief-Rivierenland/ORI-A-XSD/commits/main/) | [Historische versies van de XSD](https://github.com/Regionaal-Archief-Rivierenland/ORI-A-XSD/releases)

###  Versie 1.0.0

* Eerste publieke release

# Voorbeeldbestanden

Een voorbeeld van hoe je een vergadering kan beschrijven in ORI-A XML. De voorbeeldbestanden laten ook zien hoe je de **video-opname** en **bijbehorende vergaderstukken** kan beschrijven in MDTO (of de niet langer actief ondersteunde voorloper van MDTO, [TMLO](https://www.nationaalarchief.nl/archiveren/kennisbank/tmlo)).

::: tip
**Tip:** Voor meer informatie over ORI-A + MDTO, zie [ORI-A & MDTO combineren](ORI-A & MDTO combineren).
:::

De vergadering in kwestie [is gebaseerd op een gemeenteraad van de gemeente Leiden](https://leiden.parlaeus.nl/app/public/agenda/8028228820022a0a0282a0a8814c778c/vod). Sommige gegevens zijn om didactische redenen gefictionaliseerd of ingekort.


<figure style="text-align: left">

```
Voorbeelden/
├── Voorbeeld.ori-a.xml
└── MDTO/
    ├── 23-11-30_Transcript_Raadsvergadering_Leiden.pdf
    ├── 23-11-30_Transcript_Raadsvergadering_Leiden.mdto.xml
    ├── 23-11-30_Transcript_Raadsvergadering_Leiden.pdf.bestand.mdto.xml
    ├── Videotuul_Gemeenteraad_30_november_2023.mp4
    ├── Videotuul_Gemeenteraad_30_november_2023.mdto.xml
    ├── Videotuul_Gemeenteraad_30_november_2023.mp4.bestand.mdto.xml
    …
```

<figcaption style="text-align: center">Gedeelte van de inhoud van de ORI-A + MDTO voorbeeldbestanden</figcaption>
</figure>

``` {=html}
<div class="grid download">
<select name="versie picker" aria-label="Versie" required">
  <option selected disabled value="">Soort</option>
  <option selected="selected">ORI-A + MDTO</option>
  <option>ORI-A + MDTO (opex)</option>
  <option>ORI-A + TMLO</option>
</select>

<button><span><strong>Voorbeeldbestanden</strong> (zip)</span></button>
</div>
```

## Gebruikersscenario: ORI-A voorbeeldbestanden in Preservica

Gebruikersscenario door Erfgoed Leiden & Omstreken waar andere Preservica gebruikers mogelijk inspiratie uit op kunnen doen.

TODO

# Diagram

Het ORI-A diagram is een visuele, op UML-geïnspireerde weergave van het ORI-A informatiemodel. Nuttig als je een globaal plaatje van ORI-A wilt krijgen.

Verplichte gegevens zijn **dik gedrukt**.

<figure class="largefigure">
    <a href="ORI-A-diagram.pdf" target="_blank">
        <img alt="Klein gedeelte van het ORI-A informatiemodel" class="largefigure" src="klein.svg">
    </a>
    <figcaption>
    Klein gedeelte van het ORI-A informatiemodel ([klik voor het volledige figuur](ORI-A-diagram.pdf){target="_blank"})
    </figcaption>
    </figure>

``` {=html}
<div class="grid download">
<select name="versie picker" aria-label="Versie" required">
  <option selected disabled value="">Bestandsformaat</option>
  <option selected="selected">PDF</option>
  <option>SVG</option>
</select>

<button><span><strong>ORI-A diagram</strong> (pdf)</span></button>
</div>
```

# Logo

Dit logo kun je bijvoorbeeld gebruiken in promotiemateriaal of slides.

![ ](logo.svg){width=60%}

``` {=html}
<div class="grid download">
<select aria-label="Bestansformaat" required">
  <option selected disabled value="">Bestandsformaat</option>
  <option selected="selected">SVG</option>
  <option>PNG</option>
</select>

<button><span><strong>Logo</strong> (svg)</span></button>
</div>
```
