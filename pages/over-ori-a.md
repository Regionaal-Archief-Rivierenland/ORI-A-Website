---
title: Over ORI-A
position: 1
---

ORI-A is een archiefstandaard voor het duurzaam bewaren van **raadsinformatie** --- oftewel, de digitale gegevens die overheden zoals gemeentes en provincies aanmaken tijdens bestuurlijke of politieke besluitvorming.

Hieronder wordt het belang van een archiefstandaard voor zulke informatie uitgelegd, en vind je een overzicht van alle ORI-A documentatie.

# Wat is ORI-A?

De Open Raadsinformatie Archiefstandaard (ORI-A) beschrijft de regels voor het duurzaam bewaren van raadsinformatie in XML-formaat. Deze regels zijn vastgelegd in het [ORI-A XML-schema](downloads#xml-schema). Dit schema kan gebruikt worden wanneer raadsinformatie, zoals een collectie videotulen, voor permanente bewaring naar een [e-depot](https://www.nationaalarchief.nl/archiveren/kennisbank/wat-is-een-e-depot) wordt gemigreerd.

ORI-A is gebaseerd op het informatiemodel dat de VNG heeft ontworpen voor [de Open Raadsinformatie (ORI) API](https://github.com/VNG-Realisatie/ODS-Open-Raadsinformatie). In ["Hoe verhoudt ORI-A zich tot ORI?"](faq#hoe-verhoudt-ori-a-zich-tot-ori) kun je meer lezen over de verschillen tussen deze twee informatiemodellen.

# Waarom is ORI-A ontwikkeld?

ORI-A heeft hetzelfde hoofddoel als het ORI project van de VNG: het gestandaardiseerd beschikbaar stellen van raadsinformatie. Deze standaardisatieslag is hard nodig, omdat ieder raadsinformatiesysteem (RIS) momenteel een eigen, niet-publiek gedocumenteerd formaat voor raadsinformatie hanteert. Hiermee komt de toekomstige **vindbaarheid** en **interpreteerbaarheid** van raadsinformatie in gevaar.

De ORI-standaard van de VNG voldeed echter niet volledig aan de behoeften van archiefdiensten, waaronder [de mogelijkheid tot integratie met **MDTO**](hoe-werkt-ori-a#ori-a-mdto-combineren). Hierom is besloten een archiefvariant van ORI te ontwikkelen. Je kan hier meer over lezen in [Waarom een speciale archiefstandaard?](faq#waarom-een-speciale-archiefstandaard)

# Beheer van de standaard

ORI-A wordt beheerd door de [Werkgroep Archivering Raadsinformatie](colofon). De komende tijd richten we ons op pilotimplementaties, waarin we de 1.0 versie van de standaard gaan inzetten voor migraties vanuit RIS-systemen. Houd deze site en [KIA](https://kiacommunity.nl/groups/86-videotulen/welcome) in de gaten voor updates!

::: tip
**Versie 1.0** van het [ORI-A XML-schema](downloads#xml-schema) is uitgekomen 🎉 We nodigen iedereen uit feedback over ORI-A te delen via [onze GitHub](https://github.com/Regionaal-Archief-Rivierenland/ORI-A-XSD)
:::

# Documentatie

De ORI-A documentatie bestaat uit een aantal onderdelen:

``` {=html}
<div class="cardgrid">
  <a href="hoe-werkt-ori-a">
    <article class="card">
      <header>
        <svg width=27 height=27>
          <use xlink:href="boek.svg#boek"/>
        </svg>Hoe werkt ORI-A?</header>
      <p>Stapgewijze uitleg van ORI-A aan de hand van stukjes XML</p>
    </article>
  </a>
  <a href="xml-schema">
    <article class="card">
      <header><span style='margin-right: 0.3em'>&lt;/&gt;</span>XML-schema</header>
<p>Complete specificatie van het XML-schema</p>
</article>
</a>
<a href="downloads#voorbeeldbestanden">
  <article class="card">
    <header>
      <svg width=27 height=27>
        <use xlink:href="download.svg#download"/>
      </svg>Voorbeeldbestanden</header>
    <p>Voorbeeld van hoe je een echte vergadering + videotuul met behulp van ORI-A en MDTO kan beschrijven</p>
  </article>
</a>
<a href="begrippenlijsten">
  <article class="card">
    <header>
      <svg width=27 height=27>
        <use xlink:href="lijst.svg#lijst"/>
      </svg>Begrippenlijsten</header>
    <p>Definities van begrippen die met raadsinformatie te maken hebben</p>
  </article>
</a>
<a href="downloads#diagram">
  <article class="card">
    <header>
      <svg width=27 height=27 style="margin-top: -0.2em; margin-right: 0.4em">
        <use xlink:href="image.svg#image"/>
      </svg>Diagram</header>
    <p>Schematische weergave van het ORI-A informatiemodel</p>
  </article>
</a>
<a href="faq">
  <article class="card">
    <header>
      <svg width=27 height=27>
        <use xlink:href="faq.svg#faq"/>
      </svg>Veelgestelde vragen</header>
    <p>Algemene vragen over ORI-A</p>
  </article>
</a>
</div>
```
