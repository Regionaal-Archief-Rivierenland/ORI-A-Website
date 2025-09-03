---
title: Veelgestelde vragen
position: 5
---

# Wat is raadsinformatie, en wat is een videotuul? {.dropdown}

**Raadsinformatie** is een verzamelnaam voor alle digitale informatie die overheden aanmaken bij politieke en/of bestuurlijke besluitvorming. Deze besluitvorming vindt plaats in vergaderingen.

Een **videotuul** (samenvoeging van "video" en "notulen") is een audiovisueel verslag van zo'n vergadering. Een videotuul bestaat meestal uit **twee onderdelen**: een video-opname; en metagegevens die contextinformatie geven over de vergadering, zoals een overzicht van de aanwezige fracties,  een lijst met behandelde agendapunten, of sprekersinformatie.

Een vergadering die is vastgelegd middels een audio-opname wordt ook wel een **audiotuul** genoemd.

# Moeten videotulen worden bewaard? {.dropdown}

Strikt genomen zijn overheden niet altijd verplicht om videotulen te bewaren. Als een vergadering ook schriftelijk is vastgelegd, dan hoort de meest informatierijke bron te worden bewaard. Wel is het vanuit cultuurhistorisch oogpunt belangrijk dat videotulen permanent bewaard worden. Videotulen zijn namelijk een belangrijk onderdeel van de digitale democratie. 

----

Bron: [Selectielijst gemeenten en intergemeentelijke organen 2020](https://www.nationaalarchief.nl/archiveren/kennisbank/selectielijst-gemeenten-en-intergemeentelijke-organen-2020)

# Waarom een speciale archiefstandaard? {.dropdown}

ORI en ORI-A hebben vergelijkbare doelstellingen, waaronder het gestandaardiseerd beschikbaarstellen van raadsinformatie.

Toch waren er enkele redenen waarom een speciale archiefvariant van ORI nodig bleek:

* **XML ondersteuning.** ORI is alleen beschikbaar in het [JSON bestandsformaat](https://en.wikipedia.org/wiki/JSON). Alhoewel er niks mis is met JSON, ondersteunen e-depots en de software die archiefinstellingen gebruiken meestal alleen XML. Door een XML standaard en [aansluitend validatie-schema](https://en.wikipedia.org/wiki/XML_Schema_(W3C)) te ontwikkelen --- [de ORI-A XSD](downloads) --- sluit ORI-A beter aan op gewoontes in de archiefsector.

* **Aansluiten bij bestaande (archief)standaarden.** [Het Nationaal Archief raadt aan](https://www.nationaalarchief.nl/archiveren/mdto#collapse-102790) algemene gegevens over informatieobjecten --- zoals aanmaakdatum en auteur --- vast te leggen in MDTO, een metadatastandaard gericht op het duurzaam toegankelijk maken van overheidsdocumenten. In tegenstelling tot ORI is ORI-A zo ontwikkeld dat deze taak volledig bij MDTO blijft.  ORI-A richt zich daarentegen uitsluitend op **domeinspecifieke gegevens** --- oftewel, raadsinformatie.

  ::: tip
  **Tip:** Je kunt meer lezen over het combineren van ORI-A en MDTO in [Hoe werkt ORI-A?](tutorial#mdto)
  :::

* **Achterwaartse compatibiliteit (_backwards compatibility_).**  Bestaande raadsinformatie voldoet niet altijd aan alle eisen van ORI. Uit analyses van RIS systemen kwam bijvoorbeeld naar voren dat ORI soms gegevens vereist die ofwel niet beschikbaar zijn, ofwel niet beschikbaar zijn in de gevraagde vorm. Dit komt vooral voor bij **oudere vergaderingen**. Omdat ook deze vergaderingen gearchiveerd moeten worden, is ORI-A op bepaalde punten flexibeler (zie ook [Hoe verhoudt ORI-A zich tot ORI](faq#hoe-verhoudt-ori-a-zich-tot-ori)).

* **Duurzame toegankelijkheid.** Sommige gegevens in ORI, zoals de datum waarop een vergadering gehouden is, zijn essentieel voor de toekomstige interpreteerbaarheid van raadsinformatie, maar niet verplicht. Om de [duurzame toegankelijkheid](https://www.nationaalarchief.nl/archiveren/kennisbank/duurzaam-toegankelijk) van raadsinformatie te waarborgen zijn zulke gegevens in ORI-A wél verplicht gesteld.


# Waarom heeft ORI-A geen aggregatieniveaus? {.dropdown}

ORI-A draait om de entiteit vergadering. Deze vergadering is niet verder opgesplitst in hiërarchisch gestructureerde niveaus, ook wel bekend als 'aggregatieniveaus'. 

De hoofdreden voor deze relatief platte structuur is dat entiteiten in het  oorspronkelijke ORI informatiemodel bijna allemaal **meervoudige relaties** hebben. Om een voorbeeld te noemen: een raadsvoorstel is weliswaar een onderdeel van een vergadering, maar kan net zo goed onderdeel zijn van iemand's portefeuille, een stemming teweeg brengen, of ondertekend worden door een groep personen. Door deze verstrengelingen lijkt een raadsvergadering meer op een spinnenweb dan een hiërarchische boomstructuur.

# Hoe verhoudt ORI-A zich tot ORI? {.dropdown}

ORI-A is gebaseerd op het informatiemodel dat is ontworpen voor de [Open Raadsinformatie (ORI) API](https://github.com/VNG-Realisatie/ODS-Open-Raadsinformatie). Dit informatiemodel is aangepast aan de behoeftes van archieven. ORI-A biedt bijvoorbeeld geen ruimte voor gegevens over informatieobjecten, maar verwijst op die momenten naar MDTO. Ook zijn sommige verplichtingen verschillend. Een volledige lijst van de verschillen wordt nog opgemaakt.

Ondanks deze kleine aanpassingen is wel geprobeerd ORI-A **interoperabel** te houden met ORI. Formeler gezegd: je kan ORI zonder informatieverlies converteren naar een combinatie van ORI-A en MDTO (zie ook [round-trip format conversion](https://en.wikipedia.org/wiki/Round-trip_format_conversion)). De andere kant op (ORI-A + MDTO → ORI) kan ook, maar dan treed mogelijk informatieverlies op, aangezien ORI-A + MDTO een _superset_ is van ORI.

::: waarschuwing
Meer achtergrondinformatie over ORI kun je vinden op [de website van de ontwikkelaars van openbesluitvorming.nl](https://ontola.io/nl/cases/openbesluitvorming/) en [de website van openstate.eu](https://openstate.eu/nl/projecten-tools-data/besluiten/open-raadsinformatie/).
:::

<!-- todo: benoem conversiescripts wanneer die af zijn -->

# Voor wie is ORI-A bedoeld? {.dropdown}

ORI-A is bedoeld voor iedereen die betrokken is bij de duurzame toegankelijkheid van raadsinformatie. In het bijzonder:

- Adviseurs van overheidsorganisaties die de eisen opstellen voor raadsinformatiesystemen (RIS'en) en deze vertalen naar concrete maatregelen, bijvoorbeeld bij het migreren naar een e-depot. Denk aan: architecten, informatiemanagers en -beheerders, inkoopadviseurs en adviseurs digitale archivering.
- Leveranciers die hun producten of diensten willen afstemmen op de behoeften vanuit de overheid.
- Beheerders van raadsinformatiesystemen en andere functionarissen die betrokken zijn bij het migreren van raadsinformatie richting een e-depot. 

Ten slotte kan ORI-A ook dienen als naslagwerk voor iedereen die gebruik wil maken van door overheden gepubliceerde ORI-A metagegevens. Denk bijvoorbeeld aan applicatiebouwers die viewers of zoekmachines voor (openbare) raadsinformatie willen ontwikkelen.

# Wanneer gebruik je ORI-A? {.dropdown}

ORI-A is toepasbaar in verschillende scenario’s:

- **Bij het ontwerpen van informatiesystemen:** bij het inkopen, bouwen, aanpassen of uitfaseren van een informatiesysteem kan ORI-A worden gebruikt bij het bepalen van het programma van eisen voor het uitwisselen van metagegevens. Bij het configureren en beheren van het systeem kan ORI-A worden gebruikt als nadere toelichting op het programma van eisen. 
- **Bij het ontwerpen van koppelingen tussen bestuurlijke informatiesystemen en e-depots:** met behulp van het ORI-A XML-schema kunnen metagegevens gestructureerd en geautomatiseerd uitgewisseld worden. 
- **Bij het gebruiken van metagegevens:** met behulp van het XML-schema en het metagegevensschema kunnen gebruikers metadata lezen en interpreteren. 
- **Bij het vormgeven van de presentatie van raadsinformatie in een e-depot:** ORI-A bevat in de basis alle benodigde data-elementen om de presentatie van raadsinformatie in onderlinge samenhang mogelijk te maken. 


