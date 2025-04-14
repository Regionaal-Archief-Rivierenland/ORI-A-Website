---
title: FAQ
---

# Waarom is ORI-A ontwikkeld?

Nederlandse overheden zijn met de Archiefwet verplicht om archiefbescheiden die daarvoor in aanmerking komen, na twintig jaar voor permanente bewaring over te dragen naar een archiefbewaarplaats. De verslagen van vertegenwoordigende organen en bestuurlijke vergaderingen zijn een belangrijk voorbeeld van archiefbescheiden die permanent te bewaren zijn. Ze vormen een waardevolle bron voor onderzoek naar lokale en regionale besluitvorming. De afgelopen decennia is het bestuurlijk besluitvormingsproces ingrijpend gedigitaliseerd. In groeiende mate zien raden af van het maken van schriftelijke notulen, maar besluiten ze audio- of video-opnamen te maken van de vergaderingen. Dit worden ook wel audiotulen of videotulen genoemd.

Audiotulen en videotulen worden gemaakt en beheerd in domeinspecifieke procesondersteunende software, die naar gelang de overheidslaag die ze bedienen Raads-, Staten- of Bestuurlijk informatiesystemen (RIS, SIS, BIS) worden genoemd. Bij het maken van deze verslagen wordt veel data gegenereerd die helpt om de verslagen te begrijpen en gebruiken. Denk aan sprekersinformatie, agendapunten, ondertitels, stemmingen en verwijzingen naar documenten die als bijlage dienen bij agendapunten. Deze metagegevens zijn belangrijke contextgegevens die bewaard zouden moeten worden. ORI-A wil dit mogelijk maken.

Binnen de Nederlandse archiefsector is men gewoon te werken met XML bij het uitwisselen van overheidsinformatie naar digitale depots. Het Nationaal Archief beheert hiervoor het MDTO XML-schema. Dit metagegevensschema beschrijft de syntax en elementen voor metagegevens die betrekking hebben op informatieobjecten en bestanden. ORI-A biedt de mogelijkheid om daarnaast metagegevens uit te wisselen die specifiek betrekking hebben op het domein van bestuurlijke besluitvorming. 

# Wat is ORI en hoe verhoudt ORI-A zich tot ORI?

ORI (Open Raadsinformatie, ook wel [Open Raads-, Staten- en Bestuursinformatie](https://vng-realisatie.github.io/ODS-Open-Raadsinformatie/)) is een verzamelnaam voor een aantal initiatieven die met elkaar samenhangen rondom het thema van actieve openbaarmaking van informatie uit het politiek en bestuurlijk besluitvormingsproces. 

Vanaf 2015 heeft een samenwerking tussen de Open State Foundation, VNG Realisatie, Argu en Ontola het platform openraadsinformatie.nl (nu: openbesluitvorming.nl) opgeleverd. Dit platform richtte zich op het ophalen en vervolgens doorzoekbaar maken van zoveel mogelijk digitaal gepubliceerde politieke en bestuurlijke besluitvormingsstukken van gemeenten en dit op herbruikbare wijze als open data te ontsluiten. Sinds de intrede van de Wet open overheid in 2022 is de scope uitgebreid naar alle Nederlandse politieke en bestuurlijke overheidsorganen. 

De ontwikkeling van openbesluitvorming.nl splitste zich uiteen in het ontwerp van een pull-API ([Open Raadsinformatie API](https://github.com/openstate/open-raadsinformatie)), een elastic search front-end voor het doorzoekbaar maken van deze data ([openbesluitvorming](https://github.com/ontola/openbesluitvorming)) en een informatiemodel voor raadsinformatie op basis waarvan een Open API Specificatie wordt opgesteld ([ODS Open Raadsinformatie](https://github.com/VNG-Realisatie/ODS-Open-Raadsinformatie)). Deze laatste heeft als basis gediend voor ORI-A.

ORI-A heeft het informatiemodel onder de Open API Specificatie als basis genomen voor de ontwikkeling van een XML-schema. De begrippen, attributen en onderlinge relaties in het informatiemodel zijn zoveel mogelijk één-op-één overgenomen. De gedachte hierachter was dat we een organisatie die al werkt met ORI zo min mogelijk meerwerk wilden bezorgen om ook ORI-A te implementeren.

# Hoe verhoudt ORI-A zich tot MDTO en TMLO/ToPX?

ORI-A is een domeinspecifieke uitwisselstandaard voor metagegevens die worden gegenereerd tijdens het politiek en bestuurlijk besluitvormingsproces. Deze metagegevens hebben betrekking op bestuurlijke vergaderingen die worden vastgelegd in audiovisuele vorm, zoals audiotulen of videotulen. ORI-A beschrijft enkel die metagegevens.

MDTO (Metagegevens voor duurzaam toegankelijke overheidsinformatie) is een norm voor het vastleggen en uitwisselen van eenduidige metagegevens om de duurzame toegankelijkheid van overheidsinformatie mogelijk te maken. MDTO beschrijft hierin metagegevens voor informatieobjecten en bestanden.

Wanneer binnen het bestuurlijk besluitvormingsproces informatieobjecten en/of bestanden worden beschreven of uitgewisseld, raden we aan deze in MDTO (of ToPX) uit te drukken. Voor metagegevens over het raadsproces zelf (over vergaderingen, deelnemers, agendapunten, spreekfragmenten et cetera) is ORI-A bedoeld. Dit betekent dat uitwisseling van raadsinformatie naar een digitaal depot in de praktijk altijd een gecombineerde toepassing zal zijn van ORI-A en MDTO/ToPX.
