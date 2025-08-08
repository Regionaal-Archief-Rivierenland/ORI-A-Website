---
title: Veelgestelde vragen
position: 5
---

Hieronder worden vragen over ORI-A behandeld die niet pasten onder één van de andere rubrieken.

# Wat is raadsinformatie, en wat is een videotuul?

**Raadsinformatie** is een verzamelnaam voor alle digitale informatie die overheden aanmaken bij politieke en/of bestuurlijke besluitvorming. Deze besluitvorming vindt plaats in vergaderingen.

Een **videotuul** (samenvoeging van "video" en "notulen") is een audiovisueel verslag van zo'n vergadering. Een videotuul bestaat meestal uit **twee onderdelen**: een video-opname; en metagegevens die contextinformatie geven over de vergadering, zoals een overzicht van de aanwezige fracties,  een lijst met behandelde agendapunten, of sprekersinformatie.

Een vergadering die is vastgelegd middels een audio-opname wordt ook wel een **audiotuul** genoemd.

# Moeten videotulen worden bewaard?

Strikt genomen zijn overheden niet altijd verplicht om videotulen te bewaren. Als een vergadering ook schriftelijk is vastgelegd, dan hoort de meest informatierijke bron te worden bewaard. Wel is het vanuit cultuurhistorisch oogpunt belangrijk dat videotulen permanent bewaard worden. Videotulen zijn namelijk een belangrijk onderdeel van de digitale democratie. 

----

Bron: [Selectielijst gemeenten en intergemeentelijke organen 2020](https://www.nationaalarchief.nl/archiveren/kennisbank/selectielijst-gemeenten-en-intergemeentelijke-organen-2020)

# Waarom een speciale archiefstandaard?

ORI en ORI-A hebben vergelijkbare doelstellingen, waaronder het gestandaardiseerd beschikbaarstellen van raadsinformatie.

Toch waren er enkele redenen waarom een speciale archiefvariant van ORI nodig bleek:

* **XML ondersteuning.** 
ORI is alleen beschikbaar in het [JSON bestandsformaat](https://en.wikipedia.org/wiki/JSON). Alhoewel er niks mis is met JSON, ondersteunen e-depots en de software die archiefinstellingen gebruiken meestal alleen XML. Door het ORI-A [XML-schema](downloads) te ontwikkelen, wordt beter aangesloten op gewoontes in de archiefsector.

* **Aansluiten bij bestaande (archief)standaarden.** 
Het Nationaal Archief beheert [MDTO](https://www.nationaalarchief.nl/archiveren/mdto#collapse-102790) als norm voor het vastleggen en uitwisselen van metagegevens van overheidsinformatie, waarvoor ook een [XML-schema](https://www.nationaalarchief.nl/archiveren/mdto/xml-schema) is ontwikkeld. In dit schema staan de entiteiten informatieobject en bestand centraal. MDTO wordt veel gebruikt bij het migreren van overheidsinformatie naar archiefdiensten.

In het ORI-informatiemodel staan veel gegevens over informatieobjecten. Deze gegevens zijn weggelaten uit ORI-A en vervangen door verwijzingen naar MDTO. Beide standaarden zijn hierdoor goed samen bruikbaar. ORI-A richt zich dus uitsluitend op **domeinspecifieke gegevens**: raadsinformatie.

  ::: tip
  **Tip:** Je kunt meer lezen over het combineren van ORI-A en MDTO in de praktijk in [Hoe werkt ORI-A?](tutorial#mdto)
  :::

* **Achterwaartse compatibiliteit (_backwards compatibility_).**  Bestaande raadsinformatie voldoet niet altijd aan alle eisen van het ORI-informatiemodel. Uit analyses van RIS-systemen kwam bijvoorbeeld naar voren dat ORI soms gegevens vereist die ofwel niet beschikbaar zijn, ofwel niet beschikbaar zijn in de gevraagde vorm. Dit komt vooral voor bij **oudere vergaderingen**. Omdat ook deze vergaderingen gearchiveerd moeten worden, is ORI-A op bepaalde punten flexibeler (zie ook [Hoe verhoudt ORI-A zich tot ORI](faq#hoe-verhoudt-ori-a-zich-tot-ori)).

* **Duurzame toegankelijkheid.** Sommige gegevens in ORI, zoals de datum waarop een vergadering gehouden is, zijn essentieel voor de toekomstige interpreteerbaarheid van raadsinformatie, maar niet verplicht in het ORI-informatiemodel. Om de [duurzame toegankelijkheid](https://www.nationaalarchief.nl/archiveren/kennisbank/duurzaam-toegankelijk) van raadsinformatie te waarborgen zijn zulke gegevens in ORI-A wél verplicht gesteld.

# Waarom heeft ORI•A geen aggregatieniveaus?

In tegenstelling tot MDTO kent ORI-A geen aggregatieniveaus, en ook relatief weinig hiërarchie. ORI-A draait om de entiteit vergadering, maar lang niet alle entiteiten van ORI-A zijn daaronder beschreven. 

De hoofdreden voor deze relatief platte structuur is dat entiteiten in het ORI-informatiemodel bijna allemaal **meervoudige relaties** hebben. Om een voorbeeld te noemen: een aanwezige deelnemer neemt weliswaar deel aan een vergadering, maar kan net zo goed deelnemen aan een stemming, of spreken tijdens een agendapunt. Door deze verstrengelingen lijkt een raadsvergadering meer op een spinnenweb dan een hiërarchische boomstructuur.

<!-- "Voor sommige e-depots is het handig als ORI-A XML-bestanden bij het opmaken van een levering worden opgeknipt en verspreid over de aggregatieniveaus in een MDTO sidecar-structuur. Zie hiervoor de voorbeeldimplementatie van ELO" (Hier een link opnemen naar de voorbeeldbestanden van ELO, waarin ORI-A gegevens in de MDTO aggregatieniveaus is onderverdeeld) -->

# Hoe verhoudt ORI•A zich tot ORI?

ORI-A is gebaseerd op het informatiemodel dat is ontworpen voor de [Open Raadsinformatie (ORI) API](https://github.com/VNG-Realisatie/ODS-Open-Raadsinformatie). Dit informatiemodel is aangepast aan de behoeftes van archieven. ORI-A biedt bijvoorbeeld geen ruimte voor gegevens over informatieobjecten, maar verwijst op die momenten naar MDTO. Ook zijn sommige verplichtingen verschillend. Een volledige lijst van de verschillen wordt nog opgemaakt.

Ondanks deze kleine aanpassingen is wel geprobeerd ORI-A **interoperabel** te houden met ORI. Formeler gezegd: je kan ORI zonder informatieverlies converteren naar een combinatie van ORI-A en MDTO (zie ook [round-trip format conversion](https://en.wikipedia.org/wiki/Round-trip_format_conversion)). De andere kant op (ORI-A + MDTO → ORI) kan ook, maar dan treedt mogelijk informatieverlies op, aangezien ORI-A + MDTO een _superset_ is van ORI.

::: waarschuwing
Meer achtergrondinformatie over de verschillende projecten rondom ORI kun je vinden op [de website van de ontwikkelaars van openbesluitvorming.nl](https://ontola.io/nl/cases/openbesluitvorming/) en [de website van openstate.eu](https://openstate.eu/nl/projecten-tools-data/besluiten/open-raadsinformatie/).
:::

<!-- todo: benoem conversiescripts wanneer die af zijn -->

# Voor wie is ORI•A bedoeld? 

ORI-A is bedoeld voor iedereen die betrokken is bij de duurzame toegankelijkheid van raadsinformatie. In het bijzonder:

- Adviseurs van overheidsorganisaties die de eisen opstellen voor raadsinformatiesystemen (RIS'en) en deze vertalen naar concrete maatregelen, bijvoorbeeld bij het migreren naar een e-depot. Denk aan: architecten, informatiemanagers en -beheerders, inkoopadviseurs en adviseurs digitale archivering.
- Leveranciers die hun producten of diensten willen afstemmen op de behoeften vanuit de overheid.
- Beheerders van raadsinformatiesystemen en andere functionarissen die betrokken zijn bij het migreren van raadsinformatie richting een e-depot. 

Tenslotte kan ORI-A ook dienen als naslagwerk voor iedereen die gebruik wil maken van door overheden gepubliceerde ORI-A metagegevens. Denk bijvoorbeeld aan applicatiebouwers die viewers of zoekmachines voor (openbare) raadsinformatie willen ontwikkelen.

# Wanneer gebruik je ORI•A? 

ORI-A is toepasbaar in verschillende scenario’s:

- **Bij het ontwerpen van informatiesystemen:** bij het inkopen, bouwen, aanpassen of uitfaseren van een informatiesysteem kan ORI-A worden gebruikt bij het bepalen van het programma van eisen voor het uitwisselen van metagegevens. Bij het configureren en beheren van het systeem kan ORI-A worden gebruikt als nadere toelichting op het programma van eisen. 
- **Bij het ontwerpen van koppelingen tussen bestuurlijke informatiesystemen en e-depots:** met behulp van het ORI-A XML-schema kunnen metagegevens gestructureerd en geautomatiseerd uitgewisseld worden. 
- **Bij het gebruiken van metagegevens:** met behulp van het XML-schema en het metagegevensschema kunnen gebruikers metadata lezen en interpreteren. 
- **Bij het vormgeven van de presentatie van raadsinformatie in een e-depot:** ORI-A bevat in de basis alle benodigde data-elementen om de presentatie van raadsinformatie in onderlinge samenhang mogelijk te maken. 

# Hoe spel je ORI•A? 

ORI-A mag je zowel spellen met een bolletje (ORI•A) als met een streepje (ORI-A).

Wanneer je gebruik wilt maken van het bolletje, gebruik dan het Unicode karakter [Bullet (U+2022)](https://www.compart.com/en/unicode/U+2022).
