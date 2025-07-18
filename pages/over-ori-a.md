---
title: Over ORI•A
position: 1
---

<section>
:::: waarschuwing
**Disclaimer:** De ORI-A website en bijbehorende documentatie zijn nog in ontwikkeling. Hou er daarom rekening mee dat alle informatie op deze website onvolledig, onnauwkeurig of verouderd kan zijn.
::::
</section>

# Wat is ORI•A?

De Open Raadsinformatie Archiefstandaard (ORI-A) beschrijft de regels voor het duurzaam bewaren van raadsinformatie in XML-formaat. Het is gebaseerd op het informatiemodel onder de [Open API Specificatie voor Raadsinformatie](https://github.com/VNG-Realisatie/ODS-Open-Raadsinformatie). 

## Achtergrond

Vanuit enkele archiefdiensten is de behoefte ontstaan om te komen tot een standaard voor het uitwisselen van raadsinformatie naar een voorziening voor digitale duurzaamheid (e-depots). Deze archiefdiensten hebben zich verenigd in de [Werkgroep Archivering Raadsinformatie](colofon).

De werkgroep heeft twee doelen: het ontwikkelen, testen en gebruiksklaar maken van een ORI-A XSD, en vervolgens het gebruik van de standaard aanmoedigen en ondersteunen.

## Status

De ORI-A XSD is momenteel in bèta, en [kan hier gedownload worden](https://github.com/Regionaal-Archief-Rivierenland/ORI-XSD/releases). De standaard wordt de komende tijd getest aan enkele praktijkcases en op basis daarvan aangepast. Wijzigingen op de ORI-A XSD ten gevolge van deze tests worden op [GitHub](https://github.com/Regionaal-Archief-Rivierenland/ORI-A-XSD) bijgehouden.

## Documentatie

De documentatie van de XSD is een work-in-progress. De betekenis van de verschillende (sub)elementen kan op dit moment achterhaald worden uit de waardes binnen de `<xs:documentation>` tags.

Bovendien bestaat er een [grafische representatie van het informatiemodel.](ORI-A-diagram.pdf)

# Downloads

De voorbeeldbestanden zijn in verschillende variaties beschikbaar:

<div class="grid">
  <select id="voorbeeld-select" required>
    <option>ORI-A + MDTO</option>
    <option>ORI-A + MDTO (met OPEX wrapper)</option>
    <option>ORI-A + ToPX Sidecar</option>
    <option>ORI-A + ToPX RIP</option>
  </select>
  <button id="voorbeeld-dl">Download</button>
</div>
