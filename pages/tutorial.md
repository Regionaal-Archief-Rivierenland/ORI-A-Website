---
title: Hoe werkt ORI-A?
position: 4
---

# Een vergadering beschrijven

Het simpelst mogelijke ORI-A XML bestand bestaat uit een **vergadering** met een lijst **agendapunten**.

``` {=html}
<article class="card">
  <header>
    <p>
      <strong data-tooltip="Titel van de vergadering">Gemeenteraad</strong></p >
    <p class="muted" style="font-size: 0.85em; padding-top:0.3em; line-height: 1.0em; display: flex; align-items: top">
      <svg xmlns="http://www.w3.org/2000/svg" height="1.0em" viewBox="0 0 24 24" style="padding-right:0.1em; margin-top: 0.1em"><title>locatie-marker</title><path d="M12,11.5A2.5,2.5 0 0,1 9.5,9A2.5,2.5 0 0,1 12,6.5A2.5,2.5 0 0,1 14.5,9A2.5,2.5 0 0,1 12,11.5M12,2A7,7 0 0,0 5,9C5,14.25 12,22 12,22C12,22 19,14.25 19,9A7,7 0 0,0 12,2Z" /></svg>
      Raadzaal Stadhuis
      <svg xmlns="http://www.w3.org/2000/svg" height="1.0em" viewBox="0 0 24 24" style="padding-left: 0.3em; padding-right:0.2em; margin-top: 0.1em"><title>kalender</title><path d="M19,19H5V8H19M16,1V3H8V1H6V3H5C3.89,3 3,3.89 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5C21,3.89 20.1,3 19,3H18V1M17,12H12V17H17V12Z" /></svg>
      do. 30 november 2023
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


Neem bijvoorbeeld de vergadering hierboven, met de ietwat onoriginele titel 'Gemeenteraad'. In ORI-A XML zou je deze vergadering zo uitdrukken:

``` xml
<ORI-A>
    <vergadering>
        <ID>20a280a8a8a88220008208822f6b6b02</ID>
        <naam>Gemeenteraad</naam>
        <vergaderdatum>2023-11-30</vergaderdatum>
        <locatie>Raadzaal Stadhuis</locatie>
    </vergadering>
    <agendapunt>
        <ID>2028a00aaa2a8aaa00a2uaab6bdaef</ID>
        <volgnummer>1</volgnummer>
        <titel>Vaststelling Agenda</titel>
        <omschrijving>De raad stelt de agenda vast.</omschrijving>
    </agendapunt>
    <agendapunt>
        <ID>202282aa200aa08200a2821eb50cf</ID>
        <volgnummer>2</volgnummer>
        <titel>Mededelingen</titel>
        <omschrijving>Mededelingen aan de raad.</omschrijving>
    </agendapunt>
</ORI-A>
```

Dit zegt:

> Er was **30 november 2023** een vergadering genaamd 'Gemeenteraad' met **twee agendapunten**. Tijdens het agendapunt met volgnummer 1 kwam de vaststelling van de agenda aan bod, en bij het volgende agendapunt was er ruimte voor mededelingen.

Een goed begin, maar nog niet super informatief.

# Begrippenlijsten gebruiken

Meestal wil je ook nog weten _wie_ de vergadering heeft georganiseerd. In ORI-A doe je dit door een `<bestuurslaag>` aan je vergadering toe te voegen:

``` xml
<vergadering>
    <ID>20a280a8a8a88220008208822f6b6b02</ID>
    <naam>Gemeenteraad</naam>
    <vergaderdatum>2023-11-30</vergaderdatum>
    <bestuurslaag>
        <begripLabel>Gemeente Leiden</begripLabel>
        <begripCode>gm0546</begripCode>
        <verwijzingBegrippenlijst>
            <verwijzingID>https://identifier.overheid.nl/tooi/set/rwc_gemeenten_compleet/4</verwijzingID>
            <verwijzingNaam>Register gemeenten compleet</verwijzingNaam>
        </verwijzingBegrippenlijst>
    </bestuurslaag>
</vergadering>
```


Wat je binnen `<bestuurslaag>` ziet is een begrip uit een zogeheten **begrippenlijst**. Een begrippenlijst is een verzameling gerelateerde begrippen, waarin ieder begrip meestal een **korte uitleg** en eigen **identificatiecode** krijgt. In ORI-A wordt soms gevraagd een begrip uit zo'n elders gedefinieerde lijst te kiezen.  Hierboven is het gekozen begrip `Gemeente Leiden`, ook wel bekend onder de code `gm0546`.

De oorsprong van dit begrip is een begrippenlijst beheerd door het [TOOI project](https://standaarden.overheid.nl/tooi/waardelijsten/), maar [ORI-A definieert zelf ook een aantal begrippenlijsten](begrippenlijsten). Ten slotte kun je ook besluiten om zelf een begrippenlijst te onderhouden (zie hiervoor [de richtlijnen van het Nationaal Archief](https://www.nationaalarchief.nl/archiveren/mdto/begripbegrippenlijst)).


:::waarschuwing
We raden aan om in de verwijzing naar je begrippenlijst (`<verwijzingBegrippenlijst>`) een URL bij `<verwijzingID>` in te vullen. Hiermee maak je je begrippen vindbaar en valideerbaar.
:::

:::tip
**Tip:** `<bestuurslaag>` is bedoeld voor de overheidslaag die verantwoordelijk was voor de vergadering. Het specifieke **gremium** (bijvoorbeeld "Commissie Ruimte & Wonen") kun je kwijt in `<georganiseerdDoorGremium>`.
:::


# Hoofd- en subagendapunten

Het is mogelijk een agendapunt op te splitsen in **subagendapunten**. Dit is vooral handig als je agendapunten wilt onderverdelen in rubrieken.

Stel bijvoorbeeld dat je de volgende agenda hebt:

``` {=html}
<article class="card">
  <header>
    <p>
      <strong data-tooltip="Titel van de vergadering">Gemeenteraad</strong></p >
    <p class="muted" style="font-size: 0.85em; padding-top:0.3em; line-height: 1.0em; display: flex; align-items: top">
      <svg xmlns="http://www.w3.org/2000/svg" height="1.0em" viewBox="0 0 24 24" style="padding-right:0.1em; margin-top: 0.1em"><title>locatie-marker</title><path d="M12,11.5A2.5,2.5 0 0,1 9.5,9A2.5,2.5 0 0,1 12,6.5A2.5,2.5 0 0,1 14.5,9A2.5,2.5 0 0,1 12,11.5M12,2A7,7 0 0,0 5,9C5,14.25 12,22 12,22C12,22 19,14.25 19,9A7,7 0 0,0 12,2Z" /></svg>
      Raadzaal Stadhuis
      <svg xmlns="http://www.w3.org/2000/svg" height="1.0em" viewBox="0 0 24 24" style="padding-left: 0.3em; padding-right:0.2em; margin-top: 0.1em"><title>kalender</title><path d="M19,19H5V8H19M16,1V3H8V1H6V3H5C3.89,3 3,3.89 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5C21,3.89 20.1,3 19,3H18V1M17,12H12V17H17V12Z" /></svg>
      do. 30 november 2023
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
        <summary role="group" class="outline contrast" role=button>10. Vaststelling Regeling Regio Rijnland (9de wijziging)</summary>
        <p>De raad wordt gevraagd de 9de wijziging op de regeling Regio Rijnland vast te stellen.</p>
    </details>
</div>
</article>
```

Dan kun je dat zo in XML uitdrukken:

```xml
<agendapunt>
    <ID>202282aa200aa08200a2821eb50cf</ID>
    <titel>BEËDIGINGEN EN BENOEMINGEN</titel> 
    <heeftAlsSubagendapunt>
        …
        <titel>Beëdiging nieuw raadslid</titel>
        <volgnummer>8</volgnummer>
        <omschrijving>Dhr. Versluijs wordt beëdigd als duo-lid.</omschrijving>
    </heeftAlsSubagendapunt>
    <heeftAlsSubagendapunt>
        …
        <titel>Benoeming leden Rekenkamer Leiden</titel>
        <volgnummer>9</volgnummer>
        <omschrijving>Mw. Snel wordt aangesteld als lid van de Rekenkamer.</omschrijving>
    </heeftAlsSubagendapunt>
</agendapunt>

<agendapunt>
    <ID>202282aa200aa08200a2821eb5100</ID>
    <titel>HAMERSTUKKEN</titel>
    <heeftAlsSubagendapunt>
        …
        <titel>Vaststelling Regeling Regio Rijnland (9de wijziging)</titel>
        <volgnummer>10</volgnummer>
        <omschrijving>De raad wordt gevraagd de 9de wijziging op de regeling Regio Rijnland vast te stellen.</omschrijving>
    </heeftAlsSubagendapunt>
</agendapunt>
```

<!-- raden we dit aan, of schrijven we dit voor? -->
:::waarschuwing
Veel RIS systemen beschouwen rubrieken zoals "Beëdigingen en Benoemingen"  als agendapunten, maar geven ze geen volgnummers. Hierom is in ORI-A de volgorde van de `<(sub)agendapunt>`-elementen leidend voor de volgorde van de agenda.
:::


# Relaties tussen ORI-A entiteiten aanleggen

ORI-A kent naast vergaderingen en agendapunten een hoop andere entiteiten, zoals stemmingen, deelnemers en fracties (het ORI-A diagram geeft een volledig overzicht<!-- todo: add link-->).

Deze entiteiten hebben doorgaans veel **relaties**, zowel onderling als met externe informatieobjecten. Een fractielidmaatschap heeft vanzelfsprekend betrekking op een fractie, een stemming heeft altijd betrekking op een agendapunt, en een vergadering is doorgaans vastgelegd in een mediabestand ('videotuul').

## Voorbeeld: de relaties van een stemming

<!-- todo: documenteer ook wanneer je nest? -->
Het aanmaken van een relatie tussen twee entiteiten --- bijvoorbeeld een stemming en een agendapunt --- gaat via een **verwijzing**<!-- (tenminste, zolang de entiteit waarnaar verweze—n wordt in principe herhaaldelijk aangehaald zou kunnen worden) -->.

Om een relatie tot stand te brengen, heeft de entiteit waarnaar verwezen wordt een uniek ID nodig. Dit ID kan vervolgens in `<verwijzingID>` worden ingevuld:

``` xml
<stemming>
    <ID>RV 23.0081</ID>
    <heeftBetrekkingOpAgendapunt>
        <verwijzingID>2028a00aa</verwijzingID>
    </heeftBetrekkingOpAgendapunt>
    <heeftBetrekkingOpBesluitvormingsstuk>
        <verwijzingInformatieobject>
            <verwijzingID>0222a202</verwijzingID>
        </verwijzingInformatieobject>
    </heeftBetrekkingOpBesluitvormingsstuk>
</stemming>
```

Dit zegt:

> De stemming met ID `RV 23.0081` had betrekking op een elders gedefinieerd agendapunt met ID `2028a00aa`. Tijdens dit agendapunt werdt er gestemd over een besluitvormingsstuk met ID `0222a202 `. 

Voor een uitgebreide uitleg over het verwijzen **naar externe informatieobjecten** zoals besluitvormingsstukken, zie [ORI-A & MDTO combineren](hoe-werkt-ori-a#ori-a-mdto-combineren).

:::waarschuwing
De ORI-A XSD checkt of alle waardes van `<ID>`'s binnen een XML boom uniek zijn.
:::


:::tip
**Tip:** Over de keuze voor dit verwijzingsmechanisme kun je meer lezen in ["Waarom heeft ORI-A geen aggregatieniveaus" in de veelgestelde vragen](faq).
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

Naast personen, kunnen ook fracties een stem uitbrengen. Zie hiervoor [`stemResultaatPerFractieGegevens`](xml-schema#stemrestulaat-per-fractie-gegevens).

## Verwijzen met een naam

Binnen [`verwijzingGegevens`](#verwijzing-gegevens) --- de gegevensgroep waarmee je in ORI-A van de ene naar de andere entiteit verwijst --- is alleen het element `<verwijzingID>` verplicht. Naast deze verplichte ID, heb je in deze gegevensgroep ook de mogelijkheid om de **naam** van de entiteit waarnaar je verwijst meenemen.  Dit is omdat dit...

``` xml
<heeftBetrekkingOpAgendapunt>
    <verwijzingID>2028a00aa</verwijzingID>
</heeftBetrekkingOpAgendapunt>
```

voor mensen minder duidelijk leest dan dit:

``` xml
<heeftBetrekkingOpAgendapunt>
    <verwijzingID>2028a00aa</verwijzingID>
    <verwijzingNaam>Delegatiebesluit Omgevingsplan Leiden 2023</verwijzingNaam>
</heeftBetrekkingOpAgendapunt>
```

# Persoonsgegevens

In ORI-A kun je [persoonsgegevens](documentatie#natuurlijk-persoon-gegevens) onder twee verschillende _top-level_ elementen opnemen: onder `<aanwezigeDeelnemer>`, of onder `<persoonBuitenVergadering>`. Deze opties hebben een iets andere semantiek.

## Aanwezige deelnemer


De meest gebruikelijke optie is om persoonsgegevens onder het `<isNatuurlijkPersoon>` element van een aanwezige deelnemer te zetten:

``` xml
<aanwezigeDeelnemer>
    <rolnaam>Voorzitter</rolnaam>
    <isNatuurlijkPersoon>
        <ID>Persoon-0</ID>
        <geslachtsaanduiding>Man</geslachtsaanduiding>
        <functie>Burgemeester</functie>
        <naam>
            <achternaam>Velden</achternaam>
            <tussenvoegsel>van der</tussenvoegsel>
            <volledigeNaam>Peter van der Velden</volledigeNaam>
        </naam>
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
        <verwijzingID>persoon-076</verwijzingID>
        <verwijzingNaam>Jan de Vries</verwijzingNaam>
    </heeftAlsBehandelendAmbtenaar>
</agendapunt>

<persoonBuitenVergadering>
    <ID>persoon-076</ID>
    <functie>Ambtenaar</functie>
    <naam>
        <volledigeNaam>Jan de Vries</volledigeNaam>
    </naam>
</persoonBuitenVergadering>
```

## Naar personen verwijzen vanuit MDTO 

<!-- wat doen we met eventVerantwoordelijkeActor? imo zou dat ook betrokkeneGegevens moeten krijgen (ipv verwijzingGegevens), maar ja -->
ORI-A laat het beschrijven van **relaties tussen personen en documenten** over aan andere metadatastandaarden, zoals [MDTO](https://www.nationaalarchief.nl/archiveren/mdto). In MDTO komen gegevens over zulke relaties onder het element `<betrokkene>`.

MDTO vraagt een aantal gegevens onder `<betrokkene>`:

* Binnen `<betrokkeneTypeRelatie>` moet het **type relatie** tussen de persoon en het stuk beschreven worden, middels een begrip uit een begrippenlijst. ORI-A definieert hiervoor de [begrippenlijst 'Betrokkene-vergaderstuk relaties'](begrippenlijsten#betrokkene-vergaderstuk-relaties).
* Binnen `<betrokkeneActor>` worden de **naam en ID** van de betrokkene verwacht, bijvoorbeeld `Jan de Vries` en `persoon-076` om naar de ambtenaar uit het voorbeeld hierboven te verwijzen.


Stel bijvoorbeeld dat je wilt vastleggen dat een betrokkene een **indiener** van een stuk was, dan kun je dat zo doen:


``` xml
<MDTO>
    <naam>Voorstel bestemmingsplan Leiden-Noord</naam>
    …
    <betrokkene>
	    <betrokkeneTypeRelatie>
		    <begripLabel>Indiener</begripLabel>
		    <begripBegrippenlijst>
			    <verwijzingNaam>ORI-A Betrokkene-vergaderstuk relaties</verwijzingNaam>
			    <verwijzingIdentificatie>
				    <identificatieKenmerk>https://ori-a.nl/begrippenlijsten#betrokkene-vergaderstuk-relaties</identificatieKenmerk>
				    <identificatieBron>ORI-A</identificatieBron>
			    </verwijzingIdentificatie>
		    </begripBegrippenlijst>
	    </betrokkeneTypeRelatie>
	    <betrokkeneActor>
		    <verwijzingNaam>Jan de Vries</verwijzingNaam>
		    <verwijzingIdentificatie>
			    <identificatieKenmerk>Persoon-76</identificatieKenmerk>
			    <identificatieBron>Parlaeus</identificatieBron>
		    </verwijzingIdentificatie>
	    </betrokkeneActor>
    </betrokkene>
    …
```


# Spreekfragmenten

TODO

<!-- misschien incl. interactieve video, waarin je ook even het verschil uitlegt tussen relatieve en absolute timestamps -->

# ORI-A & MDTO combineren

ORI-A laat het beschrijven van [informatieobjecten](https://www.nationaalarchief.nl/archiveren/mdto/informatieobject) (**vergaderstukken**, **mediabestanden**, etc.) over aan **MDTO**. Met andere woorden: ORI-A beschrijft domein*specifieke* gegevens --- raadsgegevens --- terwijl MDTO beperkt blijft tot meer generieke gegevens over documenten en bestanden, zoals hun aanmaakdatum en auteur.

::: waarschuwing
De enige _inhoudelijke_ informatie over informatieobjecten die in ORI-A wordt opgenomen is `<informatieobjectType>`. Deze informatie overlapt met `<classificatie>` binnen MDTO.  Deze informatie mag alsnog in ORI-A worden opgenomen, omdat het soms wel degelijk domeinspecifieke informatie betreft.  Voor het begrijpen van een vergadering kan het bijvoorbeeld uitmaken of een document een motie, amendement, of voorstel is.
:::

## ORI-A → MDTO verwijzingen in XML vorm

Om ORI-A gegevens aan een MDTO informatieobject te koppelen, verwijs je naar het ID van een in MDTO opgesteld informatieobject  (zie ook [`verwijzingGegevens`](#verwijzing-gegevens)):

<!-- TODO: misschien wel mooi om het MDTO bestand ook als voorbeeld op te voeren. -->
``` xml
<heeftAlsBijlage> 
    <informatieobjectType>Motie</informatieobjectType>
    <verwijzingInformatieobject>
        <verwijzingID>document-009</verwijzingID>
        <verwijzingNaam>Motie van lid Smit</verwijzingNaam>
    </verwijzingInformatieobject>
</heeftAlsBijlage>
```

Het element `<verwijzingNaam>` hierboven is [slechts een hulpsteuntje](#verwijzen-met-een-naam) voor menselijke lezers --- om een verwijzing tot stand te brengen volstaat `<verwijzingID>`.

## Metadateren van een videotuul, audiotuul of transcriptie

Metadata over de **mediabestanden** waarin een vergadering is opgenomen --- een videotuul, audiotuul of transcriptie --- komt in MDTO (zie ook de voorbeeldbestanden<!-- todo: add link-->). 

<!-- stukje over subtitles -->
