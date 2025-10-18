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

Een goed begin, maar nog niet heel informatief.

# Begrippenlijsten gebruiken

Meestal wil je ook weten _wie_ de vergadering heeft georganiseerd. In ORI-A doe je dit door een `<bestuurslaag>` aan je vergadering toe te voegen:

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

De oorsprong van dit begrip is een begrippenlijst beheerd door het [TOOI project](https://standaarden.overheid.nl/tooi/waardelijsten/), maar [ORI-A definieert zelf ook een aantal begrippenlijsten](begrippenlijsten). Tenslotte kun je ook besluiten om zelf een begrippenlijst te onderhouden (zie hiervoor [de richtlijnen van het Nationaal Archief](https://www.nationaalarchief.nl/archiveren/mdto/begripbegrippenlijst)).

:::waarschuwing
We raden aan om in de verwijzing naar je begrippenlijst (`<verwijzingBegrippenlijst>`) een URL bij `<verwijzingID>` in te vullen. Hiermee maak je je begrippen vindbaar en valideerbaar.
:::

:::tip
**Tip:** `<bestuurslaag>` is bedoeld voor de overheidslaag die verantwoordelijk was voor de vergadering. Het specifieke **gremium** (bijvoorbeeld "Commissie Ruimte & Wonen") kun je kwijt in `<georganiseerdDoorGremium>`.
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

:::waarschuwing
Veel RIS-systemen beschouwen rubrieken zoals "Beëdigingen en Benoemingen" als agendapunten, maar geven ze geen volgnummers. Bij het ontbreken van volgnummers moet de volgorde van agendapunt-elementen aangeven in welke volgorde ze behandeld zijn.
:::

# Relaties tussen ORI-A entiteiten aanleggen

ORI-A kent naast vergaderingen en agendapunten een hoop andere entiteiten, zoals stemmingen, deelnemers en fracties (het [ORI-A diagram](downloads#diagram) geeft een volledig overzicht).

Deze entiteiten hebben doorgaans veel **relaties**, zowel onderling als met externe informatieobjecten. Een fractielidmaatschap heeft vanzelfsprekend betrekking op een fractie, een stemming heeft altijd betrekking op een agendapunt, en een vergadering is doorgaans vastgelegd in een mediabestand ('videotuul').

## Voorbeeld: de relaties van een stemming

<!-- todo: documenteer ook wanneer je nest? -->
Het leggen van een relatie tussen twee entiteiten --- bijvoorbeeld een stemming en een agendapunt --- gaat via een **verwijzing**<!-- (tenminste, zolang de entiteit waarnaar verwezen wordt in principe herhaaldelijk aangehaald zou kunnen worden) -->.

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

Naast personen, kunnen ook fracties een stem uitbrengen. Zie hiervoor [`stemResultaatPerFractieGegevens`](xml-schema#stemresultaat-per-fractie).

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

# Persoonsgegevens

In ORI-A kun je [persoonsgegevens](xml-schema#natuurlijk-persoon) onder twee verschillende _top-level_ elementen opnemen: onder `<aanwezigeDeelnemer>`, of onder `<persoonBuitenVergadering>`. Deze opties hebben een iets andere semantiek.

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
        <verwijzingID>persoon-016</verwijzingID>
        <verwijzingNaam>Jan de Vries</verwijzingNaam>
    </heeftAlsBehandelendAmbtenaar>
</agendapunt>

<persoonBuitenVergadering>
    <ID>persoon-016</ID>
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

Een belangrijke functionaliteit binnen digitale raadsinformatie is de mogelijkheid om te navigeren naar momenten in de opname dat een specifieke spreker aan het woord is tijdens een agendapunt. In ORI-A gebeurt dat via het element Spreekfragment. Spreekfragmenten relateren een <aanwezigeDeelnemer> aan een <Agendapunt>.


``` xml
<MDTO>
    <aanwezigeDeelnemer>
        …
        <isNatuurlijkPersoon>
            …
            <naam>
                …
                <volledigeNaam>Peter van der Velden</volledigeNaam>
            </naam>
        <spreektTijdensSpreekfragment>
            <videoTijdsaanduidingAanvang>00:00:00</videoTijdsaanduidingAanvang>
            <videoTijdsaanduidingEinde>00:02:36</videoTijdsaanduidingEinde>
            <isVastgelegdIn>
                <verwijzingInformatieobject>
                    <verwijzingID>8088a20808a0280002a000280b25219e</verwijzingID>
                    <verwijzingNaam>Videotuul Gemeenteraad 30 november 2023</verwijzingNaam>
                </verwijzingInformatieobject>
            <isVastgelegdIn>
            <spreektTijdensAgendapunt>
                <verwijzingID>2028a00aaa2a8aaa00a2aab6bdaef</verwijzingID>
                <verwijzingNaam>RV 23.0081 Delegatiebesluit Omgevingsplan Leiden 2023</verwijzingNaam>
            </spreektTijdensAgendapunt>
        </spreektTijdensSpreekfragment>
    </aanwezigeDeelnemer>
```

Het element <Spreekfragment> biedt veel ruimte om informatie over het spreekfragment op te nemen, zoals de <taal>, <titel> en de uitgeschreven <tekst> van het fragment. Ook is het via het element <isVastgelegdIn> mogelijk om direct naar het informatieobject te verwijzen waarin het spreekfragment is opgenomen. Dit kan een uitkomst zijn als er meerdere opnamen zijn gemaakt in een vergadering, bijvoorbeeld als een deel besloten is. Dan zijn spreekfragmenten altijd aan de juiste opname te relateren.

De essentie van een spreekfragment zijn de tijdsaanduidingen van het spreekfragment. Deze zogenoemde timestamps definiëren de tijdsspanne waarin het spreekfragment plaatsvindt in de opname. ORI-A kan zowel absolute als relatieve timestamps vastleggen.

## Absolute tijdsaanduiding

Met de elementen <aanvang> en <einde> kan het absolute moment waarop het spreekfragment in de tijd plaatsvond worden vastgelegd, dus de datum en het tijdstip.

``` xml
<MDTO>
    <aanwezigeDeelnemer>
        …
        <spreektTijdensSpreekfragment>
            <aanvang>2023-11-30T19:32:47</aanvang>
            <einde>2023-11-30T19:35:24</einde>
            …
        </spreektTijdensSpreekfragment>
    </aanwezigeDeelnemer>
```

## Tijdsaanduiding in relatie tot de opname
In ORI-A kan je ook tijdsaanduidingen van spreekfragmenten vastleggen die relateren aan een audio- en/of video-opname. Hier zijn verschillende elementen voor ingericht, die hieronder te zien zijn. ORI-A accepteert als relatieve tijdsaanduiding zowel tijdcodes (hh:mm:ss) als positieve integers. Die laatste gebruik je als de tijdsaanduiding van het spreekfragment in seconden sinds het startpunt van de opname is vastgelegd. 

``` xml
<MDTO>
    <aanwezigeDeelnemer>
        …
        <spreektTijdensSpreekfragment>
            …
            <videoTijdsaanduidingAanvang>00:00:00</videoTijdsaanduidingAanvang>
            <videoTijdsaanduidingEinde>00:02:36</videoTijdsaanduidingEinde>
            …
        </spreektTijdensSpreekfragment>
    </aanwezigeDeelnemer>
```

``` xml
<MDTO>
    <aanwezigeDeelnemer>
        …
        <spreektTijdensSpreekfragment>
            …
            <audioTijdsaanduidingAanvang>0</audioTijdsaanduidingAanvang>
            <audioTijdsaanduidingEinde>156</audioTijdsaanduidingEinde>
            …
        </spreektTijdensSpreekfragment>
    </aanwezigeDeelnemer>
```

<!-- misschien incl. interactieve video, waarin je ook even het verschil uitlegt tussen relatieve en absolute timestamps -->

# ORI-A & MDTO combineren

ORI-A laat het beschrijven van [informatieobjecten](https://www.nationaalarchief.nl/archiveren/mdto/informatieobject) (**vergaderstukken**, **mediabestanden**, etc.) over aan **MDTO**. Met andere woorden: ORI-A beschrijft domein*specifieke* gegevens --- raadsgegevens --- terwijl MDTO beperkt blijft tot meer generieke gegevens over documenten en bestanden, zoals hun aanmaakdatum en auteur.

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
            <verwijzingID>8088a20808a0…</verwijzingID>
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
