---
title: Over ORI-A
position: 1
title-icon: archive.svg
---

::: waarschuwing
**Disclaimer:** De ORI-A website en bijbehorende documentatie zijn nog in ontwikkeling. Hou er daarom rekening mee dat alle informatie op deze website onvolledig, onnauwkeurig of verouderd kan zijn.
:::

# Wat is ORI-A?

De Open Raadsinformatie Archiefstandaard (ORI-A) beschrijft de regels voor het duurzaam bewaren en uitwisselen van raadsinformatie in XML-formaat. Hiervoor is het ORI-A XML-schema ontwikkeld, dat kan worden gebruikt wanneer raadsinformatie, zoals een collectie videotulen, voor permanente bewaring naar een [e-depot](https://www.nationaalarchief.nl/archiveren/kennisbank/wat-is-een-e-depot) wordt gemigreerd. 

ORI-A is gebaseerd op het informatiemodel van [de Open Raadsinformatie (ORI) API Specificatie](https://github.com/VNG-Realisatie/ODS-Open-Raadsinformatie).

## Achtergrond

In de zomer van 2021 is tijdens een landelijke ['videotulenbijeenkomst'](https://kiacommunity.nl/thoughts/11904) door diverse stakeholders in het informatiedomein de wens uitgesproken om te komen tot een standaard voor het duurzaam bewaren en beschikbaar stellen van raadsinformatie in een digitale archiefbewaarplaats (het e-depot). De toen opgerichte [Werkgroep Archivering Raadsinformatie](colofon) stelde zich als taak deze standaard te realiseren. ORI-A is daarvan het resultaat.

De werkgroep heeft zich drie doelen gesteld: 
 - het ontwikkelen, testen en gebruiksklaar maken van een ORI-A XML-schema ([XSD](https://en.wikipedia.org/wiki/XML_Schema_(W3C)));
 - het promoten en tijdelijk ondersteunen van het gebruik van de standaard;
 - het borgen van het beheer van de standaard op de lange termijn.

## Status

Het ORI-A XML-schema is momenteel in bèta, en [kan hier gedownload worden](https://github.com/Regionaal-Archief-Rivierenland/ORI-XSD/releases). De website ondergaat de komende tijd een publieksreview. Vanaf het najaar volgen enkele pilotimplementaties, waarin de standaard wordt ingezet in de praktijk. Hierover zullen periodiek berichten op [KIA](https://kiacommunity.nl/welcome) verschijnen.

# Waarom is ORI-A ontwikkeld?

ORI-A heeft een vergelijkbaar doel als het ORI-informatiemodel: het gestandaardiseerd beschikbaar stellen van raadsinformatie. Deze standaardisatieslag is hard nodig, omdat ieder RIS-systeem momenteel een eigen, niet-publiekelijk gedocumenteerd formaat voor raadsinformatie hanteert. Hiermee komt de toekomstige **vindbaarheid** en **interpreteerbaarheid** van raadsinformatie in gevaar.

Waar ORI-A verschilt van de andere initiatieven is dat het zich ook richt op het migreren van raadsinformatie. Met ORI-A kan raadsinformatie gestandaardiseerd in XML-formaat worden opgeslagen. Hierin is eerst gekeken naar het ORI-informatiemodel, maar deze kon niet aan alle behoeften van archiefdiensten voldoen. Toen is besloten een archiefvariant van ORI te ontwikkelen. Je kan hier meer over lezen in [Waarom een speciale archiefstandaard?](faq)

# Documentatie

<!-- todo: benoem downloads pagina, het plaatje, en de voor mensen bedoelde documentatie   -->
De documentatie van de XSD is een work-in-progress. De betekenis van de verschillende (sub)elementen kan op dit moment achterhaald worden uit de waardes binnen de `<xs:documentation>` tags.

Bovendien bestaat er een [grafische representatie van het informatiemodel.](ORI-A-diagram.pdf)
