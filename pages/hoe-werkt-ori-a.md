---
title: Hoe werkt ORI-A?
position: 4
---

<!-- misschien 'De basics: een vergadering & agendapunten', of gewoon 'Een vergadering & agendapunten'-->
# Een simpele vergadering

Een simpel ORI-A XML bestand ziet er zo uit:

``` xml
<ORI-A>
    <vergadering>
        <ID>20a280a8a8a88220008208822f6b6b02</ID>
        <naam>Gemeenteraad</naam>
        <vergaderdatum>2023-11-30</vergaderdatum>
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

Duidelijk, maar nog niet super informatief.

# Begrippenlijsten gebruiken

Meestal wil je ook nog weten wie de vergadering heeft georganiseerd. In ORI-A doe je dit door een `<bestuurslaag>` aan je vergadering toe te voegen:

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


Wat je binnen `<bestuurslaag>` ziet is een zogeheten **begrippenlijst**. Een begrippenlijst is een lijst met keuzewaardes, waarbinnen iedere keuze meestal geassocieerd is met een korte uitleg en eigen identificatiecode. De gekozen waarde is hier `Gemeente Leiden`, ook wel bekende onder de code `gm0546`.


<!-- Misschien nog iets toevoegen over het duurzaam bewaren van online begrippenlijsten -->
:::waarschuwing
Het is sterk aangeraden om in de verwijzing naar je begrippenlijst (`<verwijzingBegrippenlijst>`) een duurzame URL op te nemen. Hiermee blijven je begrippen vindbaar en interpreteerbaar, zelfs in de toekomst.
:::

De oorsprong van de begrippenlijst hierboven is het [TOOI project](https://standaarden.overheid.nl/tooi/waardelijsten/), maar [ORI-A definieert zelf ook een aantal begrippenlijsten](begrippenlijsten). Daarnaast kun je er voor kiezen om zelf een begrippenlijst te onderhouden (zie hierover [de richtlijnen van het Nationaal Archief](https://www.nationaalarchief.nl/archiveren/mdto/begripbegrippenlijst)).

# Hoofd- en subagendapunten

Het is mogelijk een agendapunt op te splitsen in **subagendapunten**. Dit is vooral handig als je agendapunten wilt onderverdelen in rubrieken.

Stel bijvoorbeeld dat je de volgende agenda hebt:

``` {=html}
<article id="agenda-example">
  <header>
    <p><strong>🗓️ Agenda</strong></p>
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
        <ID>a8a80088a2aaa2812</ID>
        <titel>Beëdiging nieuw raadslid</titel>
        <volgnummer>8</volgnummer>
        <omschrijving>Dhr. Versluijs wordt beëdigd als duo-lid.</omschrijving>
    </heeftAlsSubagendapunt>
    <heeftAlsSubagendapunt>
        <ID>a8a80088a2aaa2813</ID>
        <titel>Benoeming leden Rekenkamer Leiden</titel>
        <volgnummer>9</volgnummer>
        <omschrijving>Mw. Snel wordt aangesteld als lid van de Rekenkamer.</omschrijving>
    </heeftAlsSubagendapunt>
</agendapunt>

<agendapunt>
    <ID>202282aa200aa08200a2821eb5100</ID>
    <titel>HAMERSTUKKEN</titel>
    <heeftAlsSubagendapunt>
        <ID>a8a80088a2aaa2814</ID>
        <titel>Vaststelling Regeling Regio Rijnland (9de wijziging)</titel>
        <volgnummer>10</volgnummer>
        <omschrijving>De raad wordt gevraagd de 9de wijziging op de regeling Regio Rijnland vast te stellen.</omschrijving>
    </heeftAlsSubagendapunt>
</agendapunt>
```

<!-- raden we dit aan, of schrijven we dit voor? -->
:::waarschuwing
Veel RIS systemen beschouwen rubrieken zoals "Beëdigingen en Benoemingen"  als agendapunten, maar geven ze geen volgnummers. Hierom is in ORI-A de volgorde van de `<(sub)agendapunt>` elementen leidend voor de volgorde van de agenda.
:::


# Relaties tussen ORI-A entiteiten aanleggen

ORI-A kent naast een vergadering en agendapunten nog een andere hele hoop entiteiten, zoals stemmingen, deelnemers en fracties (het ORI-A diagram geeft een volledig overzicht<!-- todo: add link-->). 

ORI-A entiteiten hebben doorgaans een hoop **relaties**, zowel onderling als met externe informatieobjecten. Een fractie lidmaatschap heeft vanzelfsprekend betrekking op een fractie,  een stemming gaat altijd over een bepaald agendapunt, en een vergadering is doorgaans vastgelegd in een mediabestand ("videotuul").


## Voorbeeld: de relaties van een stemming

<!-- todo: documenteer ook wanneer je nest? -->
Een koppelingen maken tussen twee entiteiten --- bijv. een stemming en een agendapunt --- gaat via een een **verwijzing**<!-- (tenminste, zolang de entiteit waarnaar verwezen wordt in principe herhaaldelijk aangehaald zou kunnen worden) -->. 

Om een koppeling tot stand te brengen, heeft de entiteit waarnaar verwezen wordt een uniek ID-waarde nodig. Deze waarde kan vervolgens in `verwijzingID` worden ingevuld:

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

> De stemming met ID `RV 23.0081` had betrekking op agendapunt met ID `2028a00aa`. Tijdens dit agendapunt werdt er gestemd over een besluitvormingsstuk met ID `0222a202 `. 

:::waarschuwing
De ORI-A XSD checkt of alle waardes van `<ID>`'s binnen een XML boom uniek zijn.
:::


Voor een uitgebreide uitleg over het verwijzen naar externe informatieobject zoals besluitvormingsstukken, zie "ORI-A & MDTO combineren".

Over de keuze voor dit verwijzingsmechanisme kun je meer lezen in ["Waarom heeft ORI-A geen aggregatieniveaus" de in veelgestelde vragen](faq).

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

Naast personen, kunnen ook fracties een stem uitbrengn. Zie hiervoor `stemResultaatPerfractieGegevens`<!-- todo: link-->.

# Persoonsgegevens

In ORI-A kun je [persoonsgegevens](documentatie#natuurlijk-persoon-gegevens) onder twee verschillende _top-level_ elementen opnemen:  onder `<aanwezigeDeelnemer>`, of onder `<persoonBuitenvErgadering>`. Deze opties hebben een iets ander semantiek.

## Aanwezige deelnemer


De meest gebruikelijke optie is om persoonsgegevens onder het `<isNatuurlijkPersoon>` van een aanwezige deelnemer te zetten:

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

Als je informatie wilt registeren over personen die niet in de vergadering aanwezig waren, kan dat in `<persoonBuitenVergadering>`. Met dit element kun je bijvoorbeeld…

* De afwezigheid van raadsleden registeren
* Vastleggen dat een ambtenaar die zelf niet aanwezig was verantwoordelijkheid over een agendapunt droeg
* De ondertekenaars van een stuk opslaa

In onderstaande voorbeeld was Jan de Vries niet zelf aanwezig in de vergadering, maar speelde hij toch een zekere rol als behandeld ambtenaar: 

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
    <naam>
        <volledigeNaam>Jan de Vries</volledigeNaam>
    </naam>
</persoonBuitenVergadering>
```

## Naar personen verwijzen vanuit MDTO 

ORI-A laat het beschrijven van **relaties tussen personen en documenten** over aan andere metadatastandaarden, zoals MDTO. Dit doe je het ID van een persoon opgemaakt in ORI-A — bijv. `persoon-76` — te gebruiken binnen het [`verwijzingIdentificatie` element van MDTO](https://www.nationaalarchief.nl/archiveren/mdto/verwijzingIdentificatie): 


``` xml
<MDTO>
    …
    <betrokkene>
	    <betrokkeneTypeRelatie>
		    <begripLabel>Indiener</begripLabel>
		    <begripBegrippenlijst>
			    <verwijzingNaam>ORI-A Begrippenlijst Betrokkene-vergaderstuk relaties</verwijzingNaam>
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

ORI-A laat het beschrijven van informatieobjecten (**vergaderstukken**, **mediabestanden**, etc.) over aan **MDTO**. Met andere woorden: ORI-A beschrijft domein*specifieke* gegevens — raadsgegevens — terwijl MDTO beperkt blijft tot meer generieke gegevens over documenten en bestanden, zoals hun aanmaakdatum en auteur.

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

Het element `<verwijzingNaam>` hierboven is slechts een hulp steuntje voor menselijke lezers — om een verwijzing tot stand te brengen volstaat `<verwijzingID>`.

## Metadateren van een videotuul 

