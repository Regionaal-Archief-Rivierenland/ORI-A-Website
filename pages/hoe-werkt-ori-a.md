---
title: Hoe werkt ORI-A?
title-icon: boek.svg
position: 2
---

Op deze pagina laten we zien hoe je verschillende onderdelen van een vergadering in ORI-A XML kan uitdrukken.

# Een vergadering beschrijven

Het meest simpele ORI-A XML-bestand bestaat uit een **vergadering** met een lijst **agendapunten**.

``` {=html}
<article class="card">
  <header>
    <p>
      <strong data-tooltip="Titel van de vergadering">Gemeenteraad</strong></p>
    <p class="muted" style="font-size: 0.85em; padding-top:0.3em; line-height: 1.0em; display: flex; align-items: top">
      <svg height="1.0em" viewBox="0 0 24 24" style="padding-right:0.1em; margin-top: 0.1em"><title>locatie-marker</title>
        <use xlink:href="locatie.svg#locatie"/>
      </svg>Raadzaal Stadhuis
      <svg height="1.0em" viewBox="0 0 24 24" style="padding-left: 0.3em; padding-right:0.2em; margin-top: 0.1em"><title>datum</title>
        <use xlink:href="kalender.svg#kalender"/>
      </svg>do. 30 november 2023
    </p>
  </header>
  <details>
    <summary class="outline contrast" role=button>1. Vaststelling Agenda</summary>
    <p>De raad stelt de agenda vast.</p>
  </details>
  <details>
    <summary class="outline contrast" role=button>2. Medelingen</summary>
    <p>Mededelingen aan de raad.</p>
  </details>
</article>
```


Neem bijvoorbeeld de vergadering hierboven, met als titel simpelweg 'Gemeenteraad'. In ORI-A XML zou je deze vergadering zo uitdrukken:

``` xml
<ORI-A>
    <vergadering>
        <ID>20a280a8a8a88220008208822f6b6b02</ID>
        <naam>Gemeenteraad</naam>
        <datum>2023-11-30</datum>
        <locatie>Raadzaal Stadhuis</locatie>
    </vergadering>
    <agendapunt>
        <ID>2028a00aaa2a8aaa00a2uaab6bdaef</ID>
        <naam>Vaststelling Agenda</naam>
        <volgnummer>1</volgnummer>
        <omschrijving>De raad stelt de agenda vast.</omschrijving>
    </agendapunt>
    <agendapunt>
        <ID>202282aa200aa08200a2821eb50cf</ID>
        <naam>Mededelingen</naam>
        <volgnummer>2</volgnummer>
        <omschrijving>Mededelingen aan de raad.</omschrijving>
    </agendapunt>
</ORI-A>
```

Dit zegt:

> Er was **30 november 2023** een vergadering genaamd 'Gemeenteraad' met **twee agendapunten**. Tijdens het agendapunt met volgnummer 1 kwam de vaststelling van de agenda aan bod, en bij het volgende agendapunt was er ruimte voor mededelingen.

Een goed begin, maar nog niet heel informatief.

# Begrippenlijsten gebruiken

Meestal wil je ook weten _wie_ de vergadering heeft georganiseerd. In ORI-A doe je dit door een `<overheidsorgaan>` aan je vergadering toe te voegen:

``` xml
<vergadering>
    <ID>20a280a8a8a88220008208822f6b6b02</ID>
    <naam>Gemeenteraad</naam>
    <datum>2023-11-30</datum>
    <overheidsorgaan>
        <begripLabel>Gemeente Leiden</begripLabel>
        <begripCode>gm0546</begripCode>
        <verwijzingBegrippenlijst>
            <verwijzingID>https://identifier.overheid.nl/tooi/set/rwc_gemeenten_compleet/4</verwijzingID>
            <verwijzingNaam>Register gemeenten compleet</verwijzingNaam>
        </verwijzingBegrippenlijst>
    </overheidsorgaan>
</vergadering>
```


Wat je binnen `<overheidsorgaan>` ziet is een begrip uit een zogeheten **begrippenlijst**. Een begrippenlijst is een verzameling gerelateerde begrippen, waarin ieder begrip meestal een **korte uitleg** en eigen **identificatiecode** krijgt. In ORI-A wordt soms gevraagd een begrip uit zo'n elders gedefinieerde lijst te kiezen.  Hierboven is het gekozen begrip `Gemeente Leiden`, ook wel bekend onder de code `gm0546`.

De oorsprong van dit begrip is een begrippenlijst beheerd door het [TOOI project](https://standaarden.overheid.nl/tooi/waardelijsten/), maar [ORI-A definieert zelf ook een aantal begrippenlijsten](begrippenlijsten). Tenslotte kun je ook besluiten om zelf een begrippenlijst te onderhouden (zie hiervoor [de richtlijnen van het Nationaal Archief](https://www.nationaalarchief.nl/archiveren/mdto/begripbegrippenlijst)).

:::waarschuwing
We raden aan om in de verwijzing naar je begrippenlijst (`<verwijzingBegrippenlijst>`) een URL bij `<verwijzingID>` in te vullen. Hiermee maak je je begrippen vindbaar en valideerbaar.
:::

:::tip
**Tip:** `<overheidsorgaan>` is bedoeld voor de overheidsorganisatie die verantwoordelijk was voor de vergadering. Het specifieke **gremium** (bijvoorbeeld "Commissie Ruimte & Wonen") kun je kwijt in [`georganiseerdDoorGremium`](xml-schema#vergadering-georganiseerd-door-gremium).
:::

# Hoofd- en subagendapunten

Het is mogelijk agendapunten op te splitsen in **subagendapunten**. Dit is vooral handig als je agendapunten wilt onderverdelen in rubrieken.

Stel bijvoorbeeld dat je de volgende agenda hebt:

``` {=html}
<article class="card">
  <header>
    <p>
      <strong data-tooltip="Titel van de vergadering">Gemeenteraad</strong></p >
    <p class="muted" style="font-size: 0.85em; padding-top:0.3em; line-height: 1.0em; display: flex; align-items: top">
      <svg height="1.0em" viewBox="0 0 24 24" style="padding-right:0.1em; margin-top: 0.1em"><title>locatie-marker</title>
        <use xlink:href="locatie.svg#locatie"/>
      </svg>Raadzaal Stadhuis
      <svg height="1.0em" viewBox="0 0 24 24" style="padding-left: 0.3em; padding-right:0.2em; margin-top: 0.1em"><title>datum</title>
        <use xlink:href="kalender.svg#kalender"/>
      </svg>do. 30 november 2023
    </p>
  </header>
  <div class="hoofdagendapunt">
    <p><strong>BEËDIGINGEN EN BENOEMINGEN</strong><span class="muted"> &nbsp;(09:12)</span></p>
    <details>
        <summary class="outline contrast" role=button>8. Beëdigingen nieuw raadslid en duo-leden</summary>
        <p>Dhr. Versluijs wordt beëdigd als duo-lid.</p>
    </details>
    <details>
        <summary class="outline contrast" role=button>9. Benoeming leden Rekenkamer Leiden</summary>
        <p>Mw. Snel wordt aangesteld als lid van de Rekenkamer.</p>
    </details>
</div>
<div class="hoofdagendapunt">
    <p><strong>HAMERSTUKKEN</strong><span class="muted"> &nbsp;(12:30)</span></p>
    <details>
        <summary role="group" class="outline contrast" role=button>10. Vaststelling Regeling Regio Rijnland</summary>
        <p>De raad wordt gevraagd de 9de wijziging op de regeling Regio Rijnland vast te stellen.</p>
    </details>
</div>
</article>
```

Dan kun je dat zo in XML uitdrukken:

```xml
<agendapunt>
    <ID>202282aa200aa08200a2821eb50cf</ID>
    <naam>BEËDIGINGEN EN BENOEMINGEN</naam>
    <heeftAlsSubagendapunt>
        …
        <naam>Beëdiging nieuw raadslid</naam>
        <volgnummer>8</volgnummer>
        <omschrijving>Dhr. Versluijs wordt beëdigd als duo-lid.</omschrijving>
    </heeftAlsSubagendapunt>
    <heeftAlsSubagendapunt>
        …
        <naam>Benoeming leden Rekenkamer Leiden</naam>
        <volgnummer>9</volgnummer>
        <omschrijving>Mw. Snel wordt aangesteld als lid van de Rekenkamer.</omschrijving>
    </heeftAlsSubagendapunt>
</agendapunt>

<agendapunt>
    <ID>202282aa200aa08200a2821eb5100</ID>
    <naam>HAMERSTUKKEN</naam>
    <heeftAlsSubagendapunt>
        …
        <naam>Vaststelling Regeling Regio Rijnland (9de wijziging)</naam>
        <volgnummer>10</volgnummer>
        <omschrijving>De raad wordt gevraagd de 9de wijziging op de regeling Regio Rijnland vast te stellen.</omschrijving>
    </heeftAlsSubagendapunt>
</agendapunt>
```

:::waarschuwing
Sommige RIS-systemen beschouwen rubrieken zoals "Beëdigingen en Benoemingen" als agendapunten, maar geven ze geen volgnummers. Bij het ontbreken van volgnummers moet de volgorde van agendapunt-elementen aangeven in welke volgorde ze behandeld zijn.
:::

# Relaties tussen ORI-A entiteiten aanleggen

ORI-A kent naast vergaderingen en agendapunten een hoop andere entiteiten, zoals stemmingen, deelnemers en fracties (het [ORI-A diagram](downloads#diagram) geeft een volledig overzicht).

Deze entiteiten hebben doorgaans veel **relaties**, zowel onderling als met externe informatieobjecten. Een fractielidmaatschap heeft vanzelfsprekend betrekking op een fractie, een stemming heeft altijd betrekking op een agendapunt, en een vergadering is doorgaans vastgelegd in een mediabestand ('videotuul').

## Voorbeeld: de relaties van een stemming

Het leggen van een relatie tussen twee entiteiten --- bijvoorbeeld een stemming en een agendapunt --- gaat via een **verwijzing**.

Om een relatie tot stand te brengen, heeft de entiteit waarnaar verwezen wordt een uniek ID nodig. Dit ID kan vervolgens in `<verwijzingID>` worden ingevuld:

``` xml
<stemming>
    <ID>RV 23.0081</ID>
    <heeftBetrekkingOpAgendapunt>
        <verwijzingID>20a280a8a8a88220008208822f6b6b02</verwijzingID>
    </heeftBetrekkingOpAgendapunt>
    <heeftBetrekkingOpBesluitvormingsstuk>
        <verwijzingInformatieobject>
            <verwijzingID>0222a202</verwijzingID>
        </verwijzingInformatieobject>
    </heeftBetrekkingOpBesluitvormingsstuk>
</stemming>
```

Dit zegt:

> De stemming met ID `RV 23.0081` had betrekking op een elders gedefinieerd agendapunt met ID `2028a00aa`. Tijdens dit agendapunt werd er gestemd over een besluitvormingsstuk met ID `0222a202`. 

Voor een uitgebreide uitleg over het verwijzen **naar externe informatieobjecten** zoals besluitvormingsstukken, zie [ORI-A & MDTO combineren](#ori-a-mdto-combineren).

:::waarschuwing
Het ORI-A XML-schema checkt of alle waardes van `<ID>`'s binnen een XML boom uniek zijn. Dit vermindert de kans op ambigue verwijzingen.
:::


:::tip
**Tip:** Over de keuze voor dit verwijzingsmechanisme kun je meer lezen in [Waarom heeft ORI-A geen aggregatieniveaus?](faq#waarom-heeft-ori-a-geen-aggregatieniveaus)
:::

### Individuele stemmen

Een stem van een persoon op een `<stemming>` komt onder het _top-level_ element `<aanwezigeDeelnemer>`:

``` xml
<aanwezigeDeelnemer>
    …
    <neemtDeelAanStemming>
        <keuzeStemming>Voor</keuzeStemming>
        <gegevenOpStemming>
            <verwijzingID>RV 23.0081</verwijzingID>
        </gegevenOpStemming>
    </neemtDeelAanStemming>
</aanwezigeDeelnemer>
```

Dit betekent dat deze deelnemer "Voor"  heeft gestemd op een stemming met ID `RV 23.0081`. 

## Verwijzen met een naam

Binnen [`verwijzingGegevens`](xml-schema#verwijzing-gegevens) --- de gegevensgroep waarmee je in ORI-A van de ene naar de andere entiteit verwijst --- is alleen het element `<verwijzingID>` verplicht. Naast deze verplichte ID, heb je in deze gegevensgroep ook de mogelijkheid om de **naam** van de entiteit waarnaar je verwijst meenemen.  Dit is omdat dit...

``` xml
<heeftBetrekkingOpAgendapunt>
    <verwijzingID>2028a00aa</verwijzingID>
</heeftBetrekkingOpAgendapunt>
```

voor mensen minder duidelijk leest dan dit:

``` xml
<heeftBetrekkingOpAgendapunt>
    <verwijzingID>2028a00aa</verwijzingID>
    <verwijzingNaam>Delegatiebesluit omgevingsplan Leiden 2023</verwijzingNaam>
</heeftBetrekkingOpAgendapunt>
```

::: waarschuwing
De enige twee entiteiten in ORI-A die niet via een verwijzing gekoppeld zijn, zijn natuurlijk persoon en aanwezige deelnemer. Zie de sectie over [persoonsgegevens](hoe-werkt-ori-a#persoonsgegevens) voor meer informatie.
:::

# Persoonsgegevens

In ORI-A kun je [persoonsgegevens](xml-schema#natuurlijk-persoon) onder twee verschillende _top-level_ elementen opnemen: onder `<aanwezigeDeelnemer>`, of onder `<persoonBuitenVergadering>`. Deze opties hebben een iets andere semantiek.

## Aanwezige deelnemer


De meest gebruikelijke optie is om persoonsgegevens onder het `<isNatuurlijkPersoon>` element van een aanwezige deelnemer te zetten:

``` xml
<aanwezigeDeelnemer>
    <rolnaam>
        <begripLabel>Voorzitter</begripLabel>
        <verwijzingBegrippenlijst>
            <verwijzingID>https://ori-a.nl/begrippenlijsten#deelnemerrollen</verwijzingID>
        </verwijzingBegrippenlijst>
    </rolnaam>
    <isNatuurlijkPersoon>
        <ID>Persoon-0</ID>
        <naam>
            <achternaam>Velden</achternaam>
            <tussenvoegsel>van der</tussenvoegsel>
            <volledigeNaam>Peter van der Velden</volledigeNaam>
        </naam>
        <geslachtsaanduiding>Man</geslachtsaanduiding>
        <functie>
            <begripLabel>Burgemeester</begripLabel>
            <verwijzingBegrippenlijst>
                <verwijzingID>https://ori-a.nl/begrippenlijsten#functies</verwijzingID>
            </verwijzingBegrippenlijst>
        </functie>
    </isNatuurlijkPersoon>
</aanwezigeDeelnemer>
```

Dit zegt in essentie: 

> Peter van der Velden (de burgemeester) was in deze vergadering aanwezig als voorzitter.


## Informatie over personen buiten een vergadering

Als je informatie wilt registeren over personen die _niet_ in de vergadering aanwezig waren, kan dat in `<persoonBuitenVergadering>`. Met dit element kun je onder andere:

* De afwezigheid van raadsleden bijhouden
* Vastleggen dat een ambtenaar die zelf niet aanwezig was verantwoordelijkheid over een agendapunt droeg
* De ondertekenaars van een stuk opslaan

In onderstaande voorbeeld was Jan de Vries niet zelf aanwezig in de vergadering, maar speelde hij toch een zekere rol als behandelend ambtenaar: 

``` xml
<agendapunt>
    …
    <heeftAlsBehandelendAmbtenaar>
        <verwijzingID>persoon-016</verwijzingID>
        <verwijzingNaam>Jan de Vries</verwijzingNaam>
    </heeftAlsBehandelendAmbtenaar>
</agendapunt>

<persoonBuitenVergadering>
    <ID>persoon-016</ID>
    <naam>
        <volledigeNaam>Jan de Vries</volledigeNaam>
    </naam>
    <functie>Ambtenaar</functie>
</persoonBuitenVergadering>
```

## Naar personen verwijzen vanuit MDTO 

<!-- wat doen we met eventVerantwoordelijkeActor? imo zou dat ook betrokkeneGegevens moeten krijgen (ipv verwijzingGegevens), maar ja -->
ORI-A laat het beschrijven van **relaties tussen personen en documenten** over aan andere metadatastandaarden, zoals [MDTO](https://www.nationaalarchief.nl/archiveren/mdto). In MDTO komen gegevens over zulke relaties onder het element `<betrokkene>`.

MDTO vraagt een aantal gegevens onder `<betrokkene>`:

* Binnen `<betrokkeneTypeRelatie>` moet het **type relatie** tussen de persoon en het stuk beschreven worden, middels een begrip uit een begrippenlijst. ORI-A definieert hiervoor de [begrippenlijst 'Betrokkene-vergaderstuk relaties'](begrippenlijsten#betrokkene-vergaderstuk-relaties).
* Binnen `<betrokkeneActor>` worden de **naam en ID** van de betrokkene verwacht, bijvoorbeeld `Jan de Vries` en `persoon-016` om naar de ambtenaar uit het voorbeeld hierboven te verwijzen.

Stel bijvoorbeeld dat je wilt vastleggen dat een betrokkene een **indiener** van een stuk was, dan kun je dat zo doen:

``` xml
<MDTO>
    <naam>Voorstel bestemmingsplan Leiden-Noord</naam>
    …
    <betrokkene>
	    <betrokkeneTypeRelatie>
		    <begripLabel>Indiener</begripLabel>
		    <begripBegrippenlijst>
			    <verwijzingNaam>Betrokkene-vergaderstuk relaties</verwijzingNaam>
			    <verwijzingIdentificatie>
				    <identificatieKenmerk>https://ori-a.nl/begrippenlijsten#betrokkene-vergaderstuk-relaties</identificatieKenmerk>
				    <identificatieBron>ORI-A</identificatieBron>
			    </verwijzingIdentificatie>
		    </begripBegrippenlijstt>
	    </betrokkeneTypeRelatie>
	    <betrokkeneActor>
		    <verwijzingNaam>Jan de Vries</verwijzingNaam>
		    <verwijzingIdentificatie>
			    <identificatieKenmerk>persoon-016</identificatieKenmerk>
			    <identificatieBron>Parlaeus</identificatieBron>
		    </verwijzingIdentificatie>
	    </betrokkeneActor>
    </betrokkene>
```

# Spreekfragmenten

Een aanwezige deelnemer heeft vaak een actieve rol tijdens een vergadering, bijvoorbeeld door mee te discussiëren over een agendapunt, of in te spreken tijdens een debat. Via het element `<spreektTijdensSpreekfragment>` kan je gegevens vastleggen over deze zogeheten 'spreekfragmenten', zoals tijdens welk agendapunt er werd gesproken, en in welke taal.

``` xml
<aanwezigeDeelnemer>
    <isNatuurlijkPersoon>
        …
        <volledigeNaam>Peter van der Velden</volledigeNaam>
        …
    </isNatuurlijkPersoon>
    <spreektTijdensSpreekfragment>
        <taal>nl</taal>
        <gedurendeAgendapunt>
            <verwijzingID>2028a00aa</verwijzingID>
            <verwijzingNaam>Delegatiebesluit omgevingsplan Leiden 2023</verwijzingNaam>
        </gedurendeAgendapunt>
    </spreektTijdensSpreekfragment>
</aanwezigeDeelnemer>
```

## Tijdsaanduiding varianten

Alhoewel bovenstaande al iets verteld over wanneer er is gesproken --- namelijk tijdens een agendapunt getiteld "Delegatiebesluit omgevingsplan Leiden 2023" --- kun je nog veel gedetailleerdere chronologische informatie over spreekfragmenten opnemen.

Specifieker gezegd ondersteunt ORI-A twee verschillende manieren om aan te geven wanneer een spreekfragment begint en eindigt: een relatieve en een absolute variant. Met de relatieve variant kun je aangeven wanneer het fragment begint en eindigt relatief tot een specifieke mediabron (zoals een video-opname), en met de absolute variant kun je aangeven op welk datum en tijdstip er gesproken is.

### Absolute tijdsaanduiding

Het datum en tijdstip van een spreekfragment, ook wel een _absolute_ tijdsaanduiding, kun je vastleggen met `<aanvang>` en `<einde>` direct onder het element `<spreektTijdensSpreekfragment>`:

``` xml
<aanwezigeDeelnemer>
    …
    <spreektTijdensSpreekfragment>
        <aanvang>2023-11-30T19:32:47</aanvang>
        <einde>2023-11-30T19:35:24</einde>
        …
    </spreektTijdensSpreekfragment>
```

Dit zegt dat het spreekfragment begon om 19:32:47 op 30 november 2023, en eindigde om 19:35:24 op dezelfde dag.

### Tijdsaanduiding in relatie tot de opname

Met het element `<tijdsaanduidingMediabron>` is het mogelijk om tijdsaanduidingen van spreekfragmenten vast te leggen _in relatie tot_ een audio- en/of video-opname, ook wel 'mediabron'. ORI-A accepteert als relatieve tijdsaanduiding zowel tijdcodes (`hh:mm:ss`) als positieve getallen.

Een voorbeeld van tijdscodes als tijdsaanduiding:

``` xml
<aanwezigeDeelnemer>
    …
    <spreektTijdensSpreekfragment>
        <tijdsaanduidingMediabron>
            <aanvang>00:00:00</aanvang>
            <einde>00:02:36</einde>
        </tijdsaanduidingMediabron>
        …
    </spreektTijdensSpreekfragment>
```

De XML hierboven zegt dat het spreekfragment meteen aan het begin van de opname begint (00:00:00), en stopt op twee minuten en zesendertig seconden in de opname (00:02:36). 

Hetzelfde, maar dan uitgedrukt met positieve getallen:

``` xml
<tijdsaanduidingMediabron>
    <aanvang>0</aanvang>
    <einde>156</einde>
</tijdsaanduidingMediabron>
```

De XML hierboven zegt dat de opname meteen aan het begin van de opname begint (op seconde nul), en op 156 seconden in de opname eindigt.

### Tijdsaanduidingen aan een specifieke mediabron koppelen

Binnen `<tijdsaanduidingMediabron>` kun je gebruik maken van het element `<isRelatiefTot>`. Met dit element kun je naar de specifiecke mediabron verwijzen waar de tijdsaanduiding aan relateert.

``` xml
<tijdsaanduidingMediabron>
    <aanvang>40</aanvang>
    <einde>60</einde>
    <isRelatiefTot>
        <verwijzingInformatieobject>
            <verwijzingID>8088a20808a<verwijzingID/>
            <verwijzingNaam>Videotuul Gemeenteraad 30 november 2023</verwijzingNaam>
        </verwijzingInformatieobject>
    </isRelatiefTot>
</tijdsaanduidingMediabron>
```

Dit kan een uitkomst zijn als er meerdere opnamen zijn gemaakt van een vergadering. Als er maar één opname is gemaakt, dan is het efficiënter om de verwijzing naar de mediabron op te nemen in het element [`isVastgelegdMiddels`](xml-schema#vergadering-is-vastgelegd-middels) onder het `<vergadering>`-element, en `<isRelatiefTot>` achterwege te laten.

<!-- misschien incl. interactieve video, waarin je ook even het verschil uitlegt tussen relatieve en absolute timestamps -->

# ORI-A & MDTO combineren

ORI-A laat het beschrijven van [informatieobjecten](https://www.nationaalarchief.nl/archiveren/mdto/informatieobject) (**vergaderstukken**, **mediabestanden**, etc.) over aan [**MDTO**](https://www.nationaalarchief.nl/archiveren/mdto). Met andere woorden: ORI-A beschrijft domein*specifieke* gegevens --- raadsgegevens --- terwijl MDTO beperkt blijft tot meer generieke gegevens over documenten en bestanden, zoals hun aanmaakdatum en auteur.

::: waarschuwing
De enige _inhoudelijke_ informatie over informatieobjecten die in ORI-A wordt opgenomen is `<informatieobjectType>`. Deze informatie overlapt met `<classificatie>` binnen MDTO.  Deze informatie mag alsnog in ORI-A worden opgenomen, omdat het soms wel degelijk domeinspecifieke informatie betreft.  Voor het begrijpen van een vergadering kan het bijvoorbeeld uitmaken of een document een motie, amendement, of voorstel is.
:::

## ORI-A → MDTO verwijzingen in XML vorm

Om ORI-A gegevens aan een MDTO informatieobject te koppelen, verwijs je naar het ID van een in MDTO opgesteld informatieobject  (zie ook [`verwijzingGegevens`](xml-schema#verwijzing-gegevens)):

<!-- TODO: misschien wel mooi om het MDTO bestand ook als voorbeeld op te voeren. -->
``` xml
<agendapunt>
    …
    <heeftAlsBijlage>
        <informatieobjectType>
            <begripLabel>Motie</begripLabel>
            <verwijzingBegrippenlijst>
                <verwijzingID>https://ori-a.nl/begrippenlijsten#vergaderstuk-types</verwijzingID>
            </verwijzingBegrippenlijst>
        </informatieobjectType>
        <verwijzingInformatieobject>
            <verwijzingID>document-009</verwijzingID>
            <verwijzingNaam>Motie van lid Smit</verwijzingNaam>
        </verwijzingInformatieobject>
    </heeftAlsBijlage>
</agendapunt>

```

Het element `<verwijzingNaam>` hierboven is [slechts een hulpsteuntje](#verwijzen-met-een-naam) voor menselijke lezers --- om een verwijzing tot stand te brengen volstaat `<verwijzingID>`.

## Metadateren van een videotuul, audiotuul of transcriptie

Niet alleen metagegevens over vergaderstukken, maar ook metagegevens over de **mediabestanden** waarin een vergadering is opgenomen --- een videotuul, audiotuul of transcriptie --- komen in MDTO. 

De verwijzing naar deze mediabron komt in ORI-A onder `<vergadering>`:

``` xml
<vergadering>
    …
    <isVastgelegdMiddels>
        <informatieobjectType>
            <begripLabel>Video</begripLabel>
            <verwijzingBegrippenlijst>
                <verwijzingID>https://ori-a.nl/begrippenlijsten#mediabron-types</verwijzingID>
            </verwijzingBegrippenlijst>
        </informatieobjectType>
        <verwijzingInformatieobject>
            <verwijzingID>8088a20808a0</verwijzingID>
            <verwijzingNaam>Videotuul Gemeenteraad 30 november 2023</verwijzingNaam>
        </verwijzingInformatieobject>
    </isVastgelegdMiddels>
</vergadering>
```

::: tip
**Tip:** `<isVastgelegdMiddels>` is herhaalbaar. Door dit element te herhalen kun je een koppeling leggen met meerdere mediabronnen, bijvoorbeeld met een videotuul én een transcriptie.
:::

In je MDTO kun je eventueel de [begrippenlijst 'Mediabron types'](begrippenlijsten#mediabrontypes)  onder `mdto:classificatie` invullen, om ook daar het soort mediabron nader te specificeren.


### Ondertitelbestanden

Als je een video met een los ondertitelbestand hebt, is het meestal het makkelijkst om een **complex informatieobject** aan te maken --- oftewel, een informatieobject dat is samengesteld uit meerdere bestanden:

```bash
videotuul.mp4
videotuul.vtt # dit is het ondertitelbestand
videotuul.mdto.xml
videotuul.mp4.bestand.mdto.xml
videotuul.vtt.bestand.mdto.xml
```

In MDTO druk je dit zo uit:

``` xml
<MDTO>
    <informatieobject>
        …
        <heeftRepresentatie>
            <verwijzingNaam>videotuul.mp4</verwijzingNaam>
        </heeftRepresentatie>
        <heeftRepresentatie>
            <verwijzingNaam>videotuul.vtt</verwijzingNaam>
        </heeftRepresentatie>
        …
```

Natuurlijk kun je er ook voor kiezen om ondertitels als losse informatieobjecten te modelleren. Dit kan bijvoorbeeld handig zijn als je informatie wilt registreren over de ontstaansgeschiedenis van de ondertitels, zoals of ze automatisch gegenereerd zijn, of wie de auteursrechten in bezit heeft.
