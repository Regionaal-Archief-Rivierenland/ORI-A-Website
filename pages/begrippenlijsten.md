---
title: Begrippenlijsten
title-icon: lijst.svg
position: 4
---

Hier vind je een overzicht van alle begrippenlijsten die door ORI-A worden beheerd en met raadsinformatie te maken hebben. Een begrippenlijst is een manier om gegevens te relateren aan een extern vastgestelde lijst van waarden. ORI-A volgt de definitie, semantiek en toepassing van begrippenlijsten zoals die ook in [MDTO](https://www.nationaalarchief.nl/archiveren/mdto/begripbegrippenlijst) worden gehanteerd.

Waar mogelijk maakt ORI-A gebruik van begrippenlijsten van **TOOI**, [een standaardisatieproject opgezet door de Rijksoverheid](https://standaarden.overheid.nl/tooi/doc/tooi-registers/). In andere gevallen beheert ORI-A voorlopig eigen begrippenlijsten. 


# Begrippenlijsten gebruiken

Vanuit ORI-A XML kun je op volgende manier naar een begrippenlijst verwijzen (in dit geval naar de begrippenlijst 'Vergaderstuktypes', waar het begrip 'Motie' wordt verklaard):

``` xml
<informatieobjectType>
    <begripLabel>Motie</begripLabel>
    <verwijzingBegrippenlijst>
        <verwijzingID>https://ori-a.nl/begrippenlijsten#vergaderstuktypes</verwijzingID>
        <verwijzingNaam>ORI-A Vergaderstuktypes</verwijzingNaam>
    </verwijzingBegrippenlijst>
</informatieobjectType>
```

Zie [Hoe werkt ORI-A?](hoe-werkt-ori-a#begrippenlijsten-gebruiken) voor een uitgebreider voorbeeld.

::: tip
**Tip:** Alhoewel we aanraden bestaande begrippenlijsten te gebruiken of [suggesties te doen om ze completer te maken](https://github.com/Regionaal-Archief-Rivierenland/ORI-A-Website/issues/new), kun je er ook voor kiezen zelf een begrippenlijsten te starten. Dit kan bijvoorbeeld nuttig zijn als een instantie unieke werkprocessen hanteert.

Zorg in dat geval wel dat deze begrippenlijst [duurzaam wordt beheerd](https://www.nationaalarchief.nl/archiveren/mdto/begripbegrippenlijst).
:::

# Vergaderstuktypes

Binnen ORI-A zijn de volgende vergaderstuktypes gedefinieerd. Deze types kunnen worden toegevoegd bij een verwijzing naar een informatieobject, zoals in `<heeftAlsBijlage>` onder [`agendapunt`](xml-schema#agendapunt). Voor meer informatie, zie [Gebruik van ORI-A met MDTO](hoe-werkt-ori-a#ori-a-mdto-combineren).

ORI-A onderscheidt verschillende soorten moties. Als het soort motie bekend is, zet je het soort achter het `|`-teken:

``` xml
<informatieobjectType>
   <begripLabel>Motie | Wantrouwen</begripLabel>
   <verwijzingBegrippenlijst>
       <verwijzingID>https://ori-a.nl/begrippenlijsten#vergaderstuktypes</verwijzingID>
   …
```

Als het soort motie onbekend is laat je dit achtervoegsel weg --- `<begripLabel>` is in dat geval gewoon gelijk aan `Motie`.


| Label               | Definitie                                                                  |
|:--------------------|:---------------------------------------------------------------------------|
| Voorstel            | Plan waarover een besluit genomen kan worden.                              |
| Motie               | Gemotiveerde verklaring waardoor een mening of verzoek wordt uitgesproken. |
| Motie \| Voorstel   | Motie met een voorstel tot handelen.                                       |
| Motie \| Wantrouwen | Motie van wantrouwen.                                                      |
| Motie \| Treurnis   | Motie van treurnis.                                                        |
| Motie \| Afkeuring  | Motie van afkeuring.                                                       |
| Motie \| Vreemd     | Motie over een onderwerp dat niet op de agenda staat.                      |
| Amendement          | Voorstel om een bestaand voorstel te wijzigen.                             |
| Toezegging          | Toezegging van een gedeputeerde of raadslid.                               |
| Vraag               | Vraag aan de raad.                                                         |
| Antwoord            | Antwoord op een vraag aan de raad.                                         |
| Ingekomen stuk      | Een stuk gericht aan de raad.                                              |
| Mededeling          | Een mededeling.                                                            |


# Deelnemerrollen

Binnen ORI-A zijn enkele rollen waarin een `<aanwezigeDeelnemer>` in een vergadering aanwezig kan zijn gedefinieerd:

| Label                 | Definitie                                                                  |
|:----------------------|:---------------------------------------------------------------------------|
| Voorzitter            | De voorzitter van de vergadering.                                          |
| Vice-voorzitter       | De vice-voorzitter van de vergadering.                                     |
| Portefeuillehouder    | Ambtenaar die de verantwoordelijkheid draagt over een besproken onderwerp. |
| Griffier              | Hoofd van de griffie.                                                      |
| Raadslid              | Gekozen volksvertegenwoordiger binnen een gemeente.                        |
| Statenlid             | Gekozen volksvertegenwoordiger binnen een provincie.                       |
| Kamerlid              | Gekozen volksvertegenwoordiger binnen de Eerste of Tweede Kamer.           |
| Dagelijks bestuurslid | Lid van een dagelijks bestuur.                                             |
| Algemeen bestuurslid  | Lid van een algemeen bestuur.                                              |
| Inspreker             | Niet-lid dat inspreekt tijdens de vergadering.                             |
| <del>Overig</del>     | -                                                                          |

::: waarschuwing
De rol "Overig" bestaat om compatibiliteit met het oorspronkelijke ORI informatiemodel te garanderen. Het gebruik van deze rol wordt afgeraden. Als de bestaande rollen niet toereikend zijn, heb je twee opties:

* Een uitbreiding op deze begrippenlijst [aanvragen](https://github.com/Regionaal-Archief-Rivierenland/ORI-A-Website/issues/new)
* Een nieuwe begrippenlijst starten
:::

# Mediabrontypes

Deze lijst beschrijft de meest gangbare mediaformaten waarin vergaderingen worden vastgesteld. Deze waardes kun je gebruiken onder `<informatieobjectType>`, als het informatieobject waarnaar je verwijst een mediabron is.

| Label        | Definitie                                                                 |
|:-------------|:--------------------------------------------------------------------------|
| Video        | Een audiovisuele opname van een vergadering. Ook wel 'videotuul'.         |
| Audio        | Een geluidsopname van een vergadering. Ook wel 'audiotuul'.               |
| Transcriptie | Een schriftelijke uitwerking van de gesproken inhoud van een vergadering. |

::: waarschuwing
Tradionele notulen kun je vastleggen via `isGenotuleerdIn` onder [`vergadering`](xml-schema#vergadering).
:::

# Betrokkene-vergaderstuk relaties

In het ORI-informatiemodel bestaan een aantal relaties tussen personen en vergaderstukken. In ORI-A is geen plek voor deze informatie gemaakt, omdat deze informatie het best in MDTO kan worden uitgedrukt --- het is immers contextinformatie over een informatieobject.

De onderstaande begrippenlijst **kan binnen MDTO** worden gebruikt om het soort relatie tussen een `<betrokkene>` en een informatieobject vast te leggen (zie ook "[Naar personen verwijzen vanuit MDTO](hoe-werkt-ori-a#naar-personen-verwijzen-vanuit-mdto)" en [`mdto:betrokkeneTypeRelatie`](https://www.nationaalarchief.nl/archiveren/mdto/betrokkeneTypeRelatie)).


| Label              | Definitie                               |
|:-------------------|:----------------------------------------|
| Indiener           | Indiener van een vergaderstuk.          |
| Ondertekenaar      | Ondertekenaar van een vergaderstuk.     |
| Portefeuillehouder | De portefeuillehouder van een voorstel. |

# Vergaderingstypes

Met de begrippen uit deze lijst kan het type van een [`vergadering`](xml-schema#vergadering) worden vastgelegd:


| Label                         | Definitie                              |
|:------------------------------|:---------------------------------------|
| Raadsvergadering              | Vergadering van een gemeenteraad.      |
| Commissievergadering          | Vergadering van een commissie.         |
| Collegevergadering            | Vergadering van een college.           |
| Statenvergadering             | Vergadering van Provinciale Staten.    |
| Algemene bestuursvergadering  | Vergadering van een algemeen bestuur.  |
| Dagelijks bestuursvergadering | Vergadering van een dagelijks bestuur. |
| Presidium                     | Vergadering van een presidium.         |

# Dagelijks bestuur types

Met de begrippen uit deze lijst kan het type van een [`dagelijksBestuur`](xml-schema#dagelijksBestuur) worden vastgelegd:

| Label                                  | Definitie                                                                  |
|:---------------------------------------|:---------------------------------------------------------------------------|
| College van burgemeester en wethouders | Dagelijks bestuur van een gemeente.                                        |
| College van Gedeputeerde Staten        | Dagelijks bestuur van een provincie.                                       |
| College van dijkgraaf en heemraden     | Dagelijks bestuur van een waterschap. Ook van toepassing op hoogheemraden. |
| Dagelijks bestuur                      | Dagelijks bestuur van een overheidsorgaan.                                 |

# Functies

Met de begrippen uit deze lijst kan de functie of ambt van een [`natuurlijkPersoon`](xml-schema#natuurlijk-persoon) worden vastgelegd:

| Label                     | Definitie                                                                                     |
|:--------------------------|:----------------------------------------------------------------------------------------------|
| Commissaris van de Koning | Voorzitter van het algemeen en dagelijks bestuur van een provincie.                           |
| Burgemeester              | Voorzitter van het algemeen en dagelijks bestuur van een gemeente.                            |
| Dijkgraaf                 | Voorzitter van het algemeen en dagelijks bestuur van een waterschap.                          |
| Raadslid                  | Lid van het algemeen bestuur van een gemeente (gemeenteraad)                                  |
| Statenlid                 | Lid van het algemeen bestuur van een provincie.                                              |
| Algemeen bestuurslid      | Lid van een algemeen bestuur.                                                                 |
| Gedeputeerde              | Lid van het dagelijks bestuur van een provincie.                                              |
| Wethouder                 | Lid van het dagelijks bestuur van een gemeente.                                               |
| Heemraad                  | Lid van het dagelijks bestuur van een waterschap. Soms bekend als 'hoogheemraad'.             |
| Dagelijks bestuurslid     | Lid van een dagelijks bestuur.                                                                |
| Griffier                  | Secretaris van het algemeen bestuur van een gemeente of provincie.                            |
| Secretaris-directeur      | Secretaris van het algemeen en dagelijks bestuur van een waterschap.                          |
| Provinciesecretaris       | Secretaris van het dagelijks bestuur van een provincie.                                       |
| Gemeentesecretaris        | Secretaris van het dagelijks bestuur van een gemeente.                                        |
| Burgerlid                 | Door het algemeen bestuur van een overheidsorgaan benoemd lid van een commissie of werkgroep. |
| Ambtenaar/medewerker      | Een overheidsmedewerker.                                                                      |
| Adviseur of deskundige    | Een door de overheid ingehuurde adviseur of deskundige.                                       |
| <del>Overig</del>         | -                                                                                             |

::: waarschuwing
De functie "Overig" bestaat om compatibiliteit met het oorspronkelijke ORI informatiemodel te garanderen. Het gebruik van deze functieaanduiding wordt afgeraden. Als de bestaande functies niet toereikend zijn, heb je twee opties:

* Een uitbreiding op deze begrippenlijst [aanvragen](https://github.com/Regionaal-Archief-Rivierenland/ORI-A-Website/issues/new)
* Een nieuwe begrippenlijst starten
:::
