---
title: Veelgestelde vragen
position: 4
---

# Wat is raadsinformatie en wat is een videotuul?
Raadsinformatie is een verzamelnaam voor alle digitale informatie die overheden aanmaken bij politieke en/of bestuurlijke besluitvorming. Deze besluitvorming vindt plaats in vergaderingen.

Een videotuul is een audiovisueel verslag (samenvoeging van video en notulen) van zo'n vergadering. Als het alleen een geluidsopname is wordt het een audiotuul genoemd. Naast de opname bestaat een videotuul uit metagegevens die contextinformatie geven over de vergadering, zoals agendapunten, sprekersinformatie, spreekfragmenten en aanwezige deelnemers. Domeinspecifieke gegevens dus.

# Moeten videotulen worden bewaard?
Strikt genomen zijn overheden niet altijd verplicht om videotulen te bewaren. Als er ook schriftelijke verslagen zijn van vergaderingen, dan hoort de meest informatierijke bron te worden bewaard. Vanuit cultuurhistorisch oogpunt is het wel belangrijk dat videotulen permanent bewaard worden. Videotulen zijn een belangrijk onderdeel van de digitale democratie.

# Waarom is ORI-A ontwikkeld?
ORI-A is ontwikkeld als domeinspecifieke standaard voor raadsinformatie, wanneer dit voor permanente bewaring naar een [e-depot](https://www.nationaalarchief.nl/archiveren/kennisbank/wat-is-een-e-depot) wordt gemigreerd. Om videotulen op een [duurzaam toegankelijke] (https://www.nationaalarchief.nl/archiveren/kennisbank/duurzaam-toegankelijk) manier te kunnen beheren en beschikbaar stellen. Om migratie van raadsinformatie uniformer en efficiënter te maken, en zeker te zijn dat de juiste metagegevens meekomen.

# Waarom is ORI-A een XML-schema?
ORI-A is als XML Schema Document (XSD) ontworpen, zodat het gezamenlijk met [MDTO](https://www.nationaalarchief.nl/archiveren/mdto) kan worden gebruikt bij migraties naar het e-depot. Metagegevens over informatieobjecten en bestanden kan dan in MDTO worden uitgedrukt, en metagegevens over raadsinformatie in ORI-A.

# Waarom heeft ORI-A geen aggregatieniveaus?
ORI-A draait om de entiteit vergadering. ORI-A is zo ontworpen, dat een ORI-A XML altijd over maximaal één vergadering informatie bevat. Het is wel mogelijk om informatie over één vergadering in meerdere ORI-A.xml-bestanden te verspreiden. 

In de praktijk zal ORI-A vaak gezamenlijk met MDTO worden ingezet. Het is dan mogelijk om je raadsinformatie per vergadering in één ORI-A.xml op te nemen en je informatieobjecten in een MDTO [sidecar-structuur](https://www.nationaalarchief.nl/archiveren/mdto/specificatie-submission-information-package/structuur#:~:text=Sidecar%2D%20structuur&text=Een%20bestand%20kan%20op%20elk,heeft%20zijn%20eigen%20MDTO%20metagegevensbestand.). Je kan de ORI-A.xml ook opsplitsen en opnemen als [aanvullende metagegevens](https://www.nationaalarchief.nl/archiveren/mdto/aanvullendeMetagegevens) bij je informatieobjecten.  

# Hoe verhoudt ORI-A zich tot ORI?
ORI-A is gebaseerd op het informatiemodel dat is ontworpen voor de [Open Raadsinformatie (ORI) API](https://github.com/VNG-Realisatie/ODS-Open-Raadsinformatie). Op sommige vlakken is besloten af te wijken van dit informatiemodel. ORI-A biedt in tegenstelling tot ORI geen ruimte voor gegevens over informatieobjecten, maar verwijst op die momenten naar MDTO. Ook zijn sommige verplichtingen verschillend. Een volledige lijst van de verschillen wordt nog opgemaakt.

Voor meer achtergrondinformatie over ORI, lees [hier](https://ontola.io/nl/cases/openbesluitvorming/) en [hier](https://openstate.eu/nl/projecten-tools-data/besluiten/open-raadsinformatie/).

# Voor wie is ORI-A bedoeld? 

ORI-A is bedoeld voor iedereen die betrokken is bij de duurzame toegankelijkheid van raadsinformatie. In het bijzonder:

- Adviseurs van overheidsorganisaties die de eisen opstellen voor bestuurlijke informatiesystemen en deze vertalen naar concrete maatregelen, bijvoorbeeld bij het migreren naar een e-depot. Denk aan: architecten, informatiemanagers en -beheerders, inkoopadviseurs en adviseurs digitale archivering.
 - Leveranciers die hun producten of diensten willen afstemmen op de behoeften vanuit de overheid. 
 - Beheerders van bestuurlijke informatiesystemen en andere functionarissen die betrokken zijn bij het migreren van raadsinformatie richting een e-depot. 

ORI-A kan ook worden gebruikt als naslagwerk voor iedereen die gebruik wil maken van de ORI-A metagegevens die door een overheidsorganisatie beschikbaar zijn gesteld. Zoals voor het koppelen van een zoekmachine aan (openbare) raadsinformatie of voor het bouwen van andere applicaties die toegang bieden tot raadsinformatie, zoals viewers. 

# Wanneer gebruik je ORI-A? 

ORI-A is toepasbaar in verschillende scenario’s:

- **Bij het ontwerpen van informatiesystemen:** bij het inkopen, bouwen, aanpassen of uitfaseren van een informatiesysteem kan ORI-A worden gebruikt bij het bepalen van het programma van eisen voor het uitwisselen van metagegevens. Bij het configureren en beheren van het systeem kan ORI-A worden gebruikt als nadere toelichting op het programma van eisen. 
- **Bij het ontwerpen van koppelingen tussen bestuurlijke informatiesystemen en e-depots:** met behulp van het ORI-A XML-schema kunnen metagegevens gestructureerd en geautomatiseerd uitgewisseld worden. 
- **Bij het gebruiken van metagegevens:** met behulp van het XML-schema en het metagegevensschema kunnen gebruikers metadata lezen en interpreteren. 
- **Bij het vormgeven van de presentatie van raadsinformatie in een e-depot:** ORI-A bevat in de basis alle benodigde data-elementen om de presentatie van raadsinformatie in onderlinge samenhang mogelijk te maken. 