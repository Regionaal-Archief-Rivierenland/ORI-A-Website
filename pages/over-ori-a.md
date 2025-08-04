---
title: Over ORI•A
position: 1
---

::: waarschuwing
**Disclaimer:** De ORI-A website en bijbehorende documentatie zijn nog in ontwikkeling. Hou er daarom rekening mee dat alle informatie op deze website onvolledig, onnauwkeurig of verouderd kan zijn.
:::

# Wat is ORI•A?

De Open Raadsinformatie Archiefstandaard (ORI-A) beschrijft de regels voor het duurzaam bewaren van raadsinformatie in XML-formaat. Dit XML-formaat kan gebruikt worden wanneer raadsinformatie, zoals een collectie videotulen, voor permanente bewaring naar een [e-depot](https://www.nationaalarchief.nl/archiveren/kennisbank/wat-is-een-e-depot) wordt gemigreerd. 

ORI-A is gebaseerd op het informatiemodel onder de [Open Raadsinformatie (ORI) API specificatie](https://github.com/VNG-Realisatie/ODS-Open-Raadsinformatie).

## Achtergrond

Vanuit enkele archiefdiensten is de behoefte ontstaan om te komen tot een standaard voor het duurzaam bewaren en beschikbaarstellen van raadsinformatie in een digitale archiefbewaarplaats (het e-depot). Deze archiefdiensten hebben zich verenigd in de [Werkgroep Archivering Raadsinformatie](colofon).

De werkgroep heeft twee doelen: het ontwikkelen, testen en gebruiksklaar maken van een ORI-A XSD, en vervolgens het gebruik van de standaard aanmoedigen en ondersteunen.

## Status

De ORI-A XSD is momenteel in bèta, en [kan hier gedownload worden](https://github.com/Regionaal-Archief-Rivierenland/ORI-XSD/releases). De standaard is de afgelopen tijd getest aan enkele praktijkcases, momenteel wordt gewerkt aan de documentatie en voorbeeldbestanden. Vanaf het najaar volgen enkele pilotimplementaties, waarin de standaard wordt ingezet in de praktijk. Hierover zullen periodiek berichten op [KIA](https://kiacommunity.nl/welcome) verschijnen.

# Waarom is ORI-A ontwikkeld?

ORI-A heeft een vergelijkbaar doel als het ORI-project geleid door de VNG: het gestandaardiseerd beschikbaar stellen van raadsinformatie. Deze standaardisatie slag is hard nodig, omdat ieder RIS-systeem momenteel een eigen, niet-publiekelijk gedocumenteerd formaat voor raadsinformatie hanteert. Hiermee komt de toekomstige **vindbaarheid** en **interpreteerbaarheid** van raadsinformatie in gevaar.

Toch kon VNG's ORI niet aan alle behoeften van archieven voldoen. Hierom is besloten een archiefvariant van ORI te ontwikkelen. Je kan hier meer over lezen in [Waarom een speciale archiefstandaard?](faq).

# Documentatie

<!-- todo: benoem downloads pagina, het plaatje, en de voor mensen bedoelde documentatie   -->
De documentatie van de XSD is een work-in-progress. De betekenis van de verschillende (sub)elementen kan op dit moment achterhaald worden uit de waardes binnen de `<xs:documentation>` tags.

Bovendien bestaat er een [grafische representatie van het informatiemodel.](ORI-A-diagram.pdf)
