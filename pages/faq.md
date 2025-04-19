---
title: FAQ
position: 4
---

# Waarom is ORI-A ontwikkeld?

Nederlandse overheden zijn met de Archiefwet verplicht om archiefbescheiden die daarvoor in aanmerking komen, na twintig jaar voor permanente bewaring over te dragen naar een archiefbewaarplaats. De verslagen van vertegenwoordigende organen en bestuurlijke vergaderingen zijn een belangrijk voorbeeld van archiefbescheiden die permanent te bewaren zijn. Ze vormen een waardevolle bron voor onderzoek naar lokale en regionale besluitvorming. De afgelopen decennia is het bestuurlijk besluitvormingsproces ingrijpend gedigitaliseerd. In groeiende mate zien raden af van het maken van schriftelijke notulen, maar besluiten ze audio- of video-opnamen te maken van de vergaderingen. Dit worden ook wel audiotulen of videotulen genoemd.

Audiotulen en videotulen worden gemaakt en beheerd in domeinspecifieke procesondersteunende software, die naar gelang de overheidslaag die ze bedienen Raads-, Staten- of Bestuurlijk informatiesystemen (RIS, SIS, BIS) worden genoemd. Bij het maken van deze verslagen wordt veel data gegenereerd die helpt om de verslagen te begrijpen en gebruiken. Denk aan sprekersinformatie, agendapunten, ondertitels, stemmingen en verwijzingen naar documenten die als bijlage dienen bij agendapunten. Deze metagegevens zijn belangrijke contextgegevens die bewaard zouden moeten worden. ORI-A wil dit mogelijk maken.

Binnen de Nederlandse archiefsector is men gewoon te werken met XML bij het uitwisselen van overheidsinformatie naar digitale depots. Het Nationaal Archief beheert hiervoor het MDTO XML-schema. Dit metagegevensschema beschrijft de syntax en elementen voor metagegevens die betrekking hebben op informatieobjecten en bestanden. ORI-A biedt de mogelijkheid om daarnaast metagegevens uit te wisselen die specifiek betrekking hebben op het domein van bestuurlijke besluitvorming. 

# Hoe verhoudt ORI-A zich tot ORI?

ORI (Open Raadsinformatie, ook wel [Open Raads-, Staten- en Bestuursinformatie](https://vng-realisatie.github.io/ODS-Open-Raadsinformatie/)) is een verzamelnaam voor een aantal initiatieven die met elkaar samenhangen rondom het thema van actieve openbaarmaking van informatie uit het politiek en bestuurlijk besluitvormingsproces. 

Vanaf 2015 heeft een samenwerking tussen de Open State Foundation, VNG Realisatie, Argu en Ontola het platform openraadsinformatie.nl (nu: openbesluitvorming.nl) opgeleverd. Dit platform richtte zich op het ophalen en vervolgens doorzoekbaar maken van zoveel mogelijk digitaal gepubliceerde politieke en bestuurlijke besluitvormingsstukken van gemeenten en dit op herbruikbare wijze als open data te ontsluiten. Sinds de intrede van de Wet open overheid in 2022 is de scope uitgebreid naar alle Nederlandse politieke en bestuurlijke overheidsorganen. 

De ontwikkeling van openbesluitvorming.nl splitste zich uiteen in het ontwerp van een pull-API ([Open Raadsinformatie API](https://github.com/openstate/open-raadsinformatie)), een elastic search front-end voor het doorzoekbaar maken van deze data ([openbesluitvorming](https://github.com/ontola/openbesluitvorming)) en een informatiemodel voor raadsinformatie op basis waarvan een Open API Specificatie wordt opgesteld ([ODS Open Raadsinformatie](https://github.com/VNG-Realisatie/ODS-Open-Raadsinformatie)). Deze laatste heeft als basis gediend voor ORI-A.

Het ORI-A XML-schema is gebaseerd op het informatiemodel onder de Open API Specificatie. De elementen, attributen en onderlinge relaties in het informatiemodel zijn zoveel mogelijk één-op-één overgenomen. De gedachte hierachter is dat we een organisatie die al werkt met ORI zo min mogelijk meerwerk willen bezorgen om ook ORI-A te implementeren. ORI-A volgt de doorontwikkeling van ORI en zal waar nodig worden aangepast om gezamenlijke implementatie zo laagdrempelig mogelijk te maken.

# Waarop is ORI-A van toepassing? 

ORI-A is van toepassing op het uitwisselen van metagegevens die tijdens het bestuurlijk besluitvormingsproces worden gegenereerd in een raads-, staten- of bestuurlijk informatiesysteem (RIS/SIS/BIS), wanneer deze naar een digitale archiefbewaarplaats worden gemigreerd. Hoewel ORI-A in andere vormen van uitwisseling kan worden gehanteerd, is de syntax, opbouw en ontwerp gericht op dat toepassingsscenario. 

# Voor wie is ORI-A bedoeld? 

ORI-A is bedoeld voor iedereen die betrokken is bij de duurzame toegankelijkheid van raadsinformatie. In het bijzonder:

- Adviseurs van overheidsorganisaties die de eisen opstellen voor bestuurlijke informatiesystemen en deze vertalen naar concrete maatregelen, bijvoorbeeld wat betreft de uitwisseling richting een digitale archiefbewaarplaats. Bijvoorbeeld: architecten, informatiemanagers en -beheerders, inkoopadviseurs en adviseurs digitale archivering. 
 - Leveranciers die hun producten of diensten willen afstemmen op de behoeften vanuit de overheid. 
 - Beheerders van bestuurlijke informatiesystemen en andere functionarissen die betrokken zijn bij uitwisseling van raadsinformatie richting een digitale archiefbewaarplaats. 

ORI-A kan ook worden gebruikt als naslagwerk voor iedereen die gebruik wil maken van de ORI-A metagegevens die door een overheidsorganisatie beschikbaar zijn gesteld. Zoals voor het koppelen van een zoekmachine aan (openbare) raadsinformatie of voor het bouwen van andere applicaties die toegang bieden tot raadsinformatie, zoals viewers. 

# Waarom gebruik je ORI-A? 

Het doel van ORI-A is het op uniforme manier uitwisselen van de metagegevens die gebruik en raadpleging van digitale raadsinformatie mogelijk maken. Dit zodat er bij het uitwisselen geen foutgevoelige en bewerkelijke vertalingen nodig zijn. Hiermee worden de kwaliteit van de metagegevens bevorderd en de kosten voor uitwisselen verlaagd. 

# Wanneer gebruik je ORI-A? 

ORI-A is toepasbaar in verschillende scenario’s:

- **Bij het ontwerpen van informatiesystemen**: bij het inkopen, bouwen, aanpassen of uitfaseren van een informatiesysteem kan ORI-A worden gebruikt bij het bepalen van het programma van eisen voor het uitwisselen van metagegevens. Bij het configureren en beheren van het systeem kan ORI-A worden gebruikt als nadere toelichting op het programma van eisen. 
- **Bij het ontwerpen van koppelingen tussen bestuurlijke informatiesystemen en digitale depots**: met behulp van het XML-schema kunnen metagegevens gestructureerd en geautomatiseerd uitgewisseld worden. 
- **Bij het gebruiken van metagegevens**: met behulp van het XML-schema en het metagegevensschema kunnen gebruikers metadata lezen en interpreteren. 
- **Bij het vormgeven van de presentatie van raadsinformatie in een digitaal depot**: ORI-A bevat in de basis alle benodigde data-elementen om de presentatie van raadsinformatie in onderlinge samenhang mogelijk te maken. 

# Hoe verhoudt ORI-A zich tot MDTO/ToPX?

ORI-A is een domeinspecifieke archiefstandaard voor metagegevens die worden gegenereerd tijdens het politiek en bestuurlijk besluitvormingsproces. Deze metagegevens hebben betrekking op bestuurlijke vergaderingen die worden vastgelegd in audiovisuele vorm, zoals audiotulen of videotulen. ORI-A beschrijft enkel die metagegevens.

MDTO (Metagegevens voor duurzaam toegankelijke overheidsinformatie) is een norm voor het vastleggen en uitwisselen van eenduidige metagegevens om de duurzame toegankelijkheid van overheidsinformatie mogelijk te maken. MDTO beschrijft hierin metagegevens voor informatieobjecten en bestanden.

Wanneer binnen het bestuurlijk besluitvormingsproces informatieobjecten en/of bestanden worden beschreven of uitgewisseld, raden we aan deze in MDTO (of ToPX) uit te drukken. Voor metagegevens over het besluitvormingsproces zelf (over vergaderingen, deelnemers, agendapunten, spreekfragmenten et cetera) is ORI-A bedoeld. Dit betekent dat uitwisseling van raadsinformatie naar een digitaal depot in de praktijk altijd een gecombineerde toepassing zal zijn van ORI-A en MDTO/ToPX.
