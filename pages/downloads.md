---
title: Downloads
title-icon: download.svg
position: 8
---

Hier vind je bestanden die je helpen bij het maken, begrijpen of valideren van ORI-A metagegevens.

# XML-schema

<!-- ::: tip -->
<!-- **Tip:**  Technische feedback of vragen over de XSD kun je achterlaten op [Github](https://github.com/regionaal-archief-rivierenland/ORI-A-XSD/issues). -->
<!-- ::: -->

Het ORI-A XML-schema beschrijft de regels van valide ORI-A XML. Met dit schema kun je **controleren** of een XML-document valide ORI-A XML bevat.

Dit schema is beschikbaar in het **XSD-bestandsformaat**.

<!-- ![Valideren van ORI-A XML](validatie.svg){ width=95% } -->

``` {=html}
<figure>
<svg viewBox="0 0 527.411 242.886" width="95%">
  <use xlink:href="validatie.svg#validatie"/>
</svg>
<figcaption>Valideren van ORI-A XML</figcaption>
</figure>
```


:::tip
**Tip:** Voor het valideren van XML raden we [xmllint](https://en.wikipedia.org/wiki/Libxml2) (_commandline_ programma) of [xmlschema](https://github.com/sissaschool/xmlschema) (Python pakket) aan.
:::

``` {=html}
<div class="grid download">
<select aria-label="Versie">
  <option disabled value="">Versie</option>
  <option selected>v0.0.15</option>
  <option disabled>v1.0.0</option>
</select>

<a download href="ORI-A.xsd" role=button><span><strong>ORI-A XML schema</strong> (xsd)</span></a>
</div>
```

## Semantisch versioneren {.dropdown}

Het ORI-A XML-schema houdt een vorm van [semantisch versioneren](https://semver.org/lang/nl/) aan. Dit betekent dat elk fragment van een versienummer in de vorm `MAJEUR.MINEUR.PATCH` een speciale betekenis draagt:

1. `MAJEUR` wordt verhoogd bij schemawijzigingen die bestaande ORI-A XML onvalide maken.
2. `MINEUR` wordt verhoogtd wanneer functionaliteit wordt toegevoegd _zonder_ de status van bestaande ORI-A XML te veranderen (ook wel "compatibele wijzigingen").
3. `PATCH` wordt verhoogtd bij compatibele _bugfixes_, zoals correcties in de documentatie.

Kort gezegd: alle XML die valide is bevonden op basis van schema versie `1.1.0` is nog steeds valide in versie `1.2.1`, maar _niet_ valide in versie `2.0.0`.

## Versiewijzigingen {.dropdown}

[Volledig overzicht van wijzigingen](https://github.com/Regionaal-Archief-Rivierenland/ORI-A-XSD/commits/main/) | [Historische versies van de XSD](https://github.com/Regionaal-Archief-Rivierenland/ORI-A-XSD/releases)

###  Versie 1.0.0

* Eerste publieke release

# Voorbeeldbestanden

Een voorbeeld van hoe je een vergadering kan beschrijven in ORI-A XML. De voorbeeldbestanden laten ook zien hoe je de **video-opname** en **bijbehorende vergaderstukken** kan beschrijven in MDTO.

::: tip
**Tip:** Voor meer informatie over ORI-A + MDTO, zie [ORI-A & MDTO combineren](ORI-A & MDTO combineren).
:::

De vergadering in kwestie [is gebaseerd op een vergadering van de gemeenteraad van de gemeente Leiden](https://leiden.parlaeus.nl/app/public/agenda/8028228820022a0a0282a0a8814c778c/vod). Sommige gegevens zijn om didactische redenen gefictionaliseerd.


<figure style="text-align: left">

```
ORI-A voorbeeldbestanden/
├── Voorbeeld.ori-a.xml
├── 23-11-30_Transcript_Raadsvergadering_Leiden/
│   ├── 23-11-30_Transcript_Raadsvergadering_Leiden.pdf
│   ├── 23-11-30_Transcript_Raadsvergadering_Leiden.mdto.xml
│   └── 23-11-30_Transcript_Raadsvergadering_Leiden.pdf.bestand.mdto.xml
└── Videotuul_Gemeenteraad_30_november_2023/
    ├── Videotuul_Gemeenteraad_30_november_2023.mp4
    ├── Videotuul_Gemeenteraad_30_november_2023.mdto.xml
    ├── Videotuul_Gemeenteraad_30_november_2023.mp4.bestand.mdto.xml
    …
```

<figcaption style="text-align: center">Gedeelte van de inhoud van de ORI-A + MDTO voorbeeldbestanden</figcaption>
</figure>

``` {=html}
<div class="grid download">
<select aria-label="Voorbeeldbestand pakketten" required">
  <option disabled value="">Soort</option>
  <option selected>ORI-A + MDTO</option>
  <option disabled>ORI-A + MDTO (opex)</option>
  <option disabled>ORI-A + TMLO</option>
</select>

<a href="ORI-A voorbeeldbestanden.zip" download role=button><span><strong>Voorbeeldbestanden</strong> (zip)</span></a>
</div>
```

## Gebruikersscenario: ORI-A voorbeeldbestanden in Preservica

Gebruikersscenario van Erfgoed Leiden & Omstreken waar andere Preservica-gebruikers mogelijk inspiratie uit op kunnen doen.

::: waarschuwing
**Let op:**  Dit gedeelte van de website is nog niet af.
:::

[Preservica voorbeeldset (download)](Preservica_documentatieset.zip){download="Preservica voorbeeldset.zip"}



# Diagram

Het ORI-A diagram is een visuele, op UML-geïnspireerde weergave van het ORI-A informatiemodel. Nuttig als je een globaal beeld van ORI-A wilt krijgen.

Verplichte gegevens zijn **dikgedrukt**.

<figure class="largefigure">
    <a href="ORI-A-diagram.pdf" target="_blank" aria-label="ORI-A diagram" style="color: unset">
      <svg viewBox="0 0 1023.4499 537.95622">
        <use xlink:href="klein.svg#klein"/>
      </svg>
    </a>
    <figcaption>
    Klein gedeelte van het ORI-A informatiemodel ([klik voor het volledige figuur](ORI-A-diagram.pdf){target="_blank"})
    </figcaption>
</figure>

``` {=html}
<div class="grid download">
<select aria-label="Bestandsformaat diagram">
  <option disabled value="">Bestandsformaat</option>
  <option value="pdf_diagram" selected>PDF</option>
  <option disabled value="svg_diagram">SVG</option>
</select>

<a href="ORI-A-diagram.pdf" download role=button><span><strong>ORI-A diagram</strong> (pdf)</span></a>
</div>
```

# Logo

Dit logo kun je bijvoorbeeld gebruiken in promotiemateriaal of slides.


<figure>
  <img src="logo.svg" alt="ORI-A logo" width="60%">
</figure>


``` {=html}
<div class="grid download">
<select aria-label="Bestansformaat logo">
  <option disabled value="">Bestandsformaat</option>
  <option value="png_logo" selected>PNG</option>
  <option value="svg_logo">SVG</option>
</select>

<a href="logo.png" download role=button><span><strong>Logo</strong> (png)</span></a>
</div>
```

``` {=html}
<script defer>

document.querySelectorAll(".grid.download").forEach(group => {
    const fmap = {
    "v1.0.0": "ORI-A (v1.0.0).xsd",
    "v0.0.15": "ORI-A.xsd",
    "pdf_diagram": "ORI-A-diagram.pdf",
    "svg_diagram": "ORI-A-diagram.svg",
    "png_logo": "logo.png",
    "svg_logo": "logo.svg",
    "ORI-A + MDTO": "ORI-A Voorbeeldbestanden.zip",
    "ORI-A + MDTO (opex)": "ORI-A Voorbeeldbestanden.zip",
    };
    const select = group.querySelector("select");
        // link == download button
        const link = group.querySelector("a");
        const span = link.querySelector("span");
        const strong = link.querySelector("strong");

    // Update link/button label when selection changes
    select.addEventListener("change", () => {
        const value = select.value;
        if (!value) return;
        const label = value.split("_")[0];
        span.innerHTML = "<strong>" + strong.textContent + "</strong> (" + label.toLowerCase() + ")";;
        const file = fmap[value];
        if (!file) return;
        link.setAttribute("href", file)
    });

    });
</script>
```
