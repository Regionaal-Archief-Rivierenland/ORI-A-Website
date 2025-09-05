---
title: Begrippenlijsten
title-icon: lijst.svg
position: 4
---

Hier vind je informatie over de momenten waarop ORI-A gebruik maakt van begrippenlijsten. Een begrippenlijst is een manier om gegevens te relateren aan een extern vastgestelde (gecontroleerde) lijst van waarden. ORI-A volgt de definitie, semantiek en toepassing van begrippenlijsten zoals die ook in [MDTO](https://www.nationaalarchief.nl/archiveren/mdto/begripbegrippenlijst) worden gehanteerd.

Waar mogelijk maakt ORI-A gebruik van begrippenlijsten van **TOOI**, [een standaardisatieproject opgezet door de Rijksoverheid](https://standaarden.overheid.nl/tooi/doc/tooi-registers/). In andere gevallen beheert ORI-A voorlopig eigen begrippenlijsten.

# Begrippenlijsten gebruiken

Een begrippenlijst roep je zo aan:

``` xml
<vergaderstukType>
    <begripLabel>Motie</begripLabel>
    <verwijzingBegrippenlijst>
        <verwijzingID>www.ori-a.nl/begrippenlijsten#vergaderstuk-types</verwijzingID>
        <verwijzingNaam>ORI-A Begrippenlijst Vergaderstuk Types</verwijzingNaam>
    </verwijzingBegrippenlijst>
</vergaderstukType>
```

Alle begrippenlijsten die onderdeel zijn van **ORI-A** worden hieronder gedocumenteerd.

## TOOI Begrippenlijsten

Een paar begrippenlijsten die van toepassing zijn op **ORI-A** worden beheerd door **TOOI**, [een standaardisatieproject opgezet door de Rijksoverheid](https://standaarden.overheid.nl/tooi/doc/tooi-registers/):

* [Begrippenlijst Gemeentes](https://identifier.overheid.nl/tooi/set/rwc_gemeenten_compleet/4)
* [Begrippenlijst Waterschappen](https://identifier.overheid.nl/tooi/set/rwc_gemeenten_compleet/4)
* [Begrippenlijst Provincie](https://identifier.overheid.nl/tooi/set/rwc_gemeenten_compleet/4)

# Vergaderstuktypes

Binnen ORI-A zijn de volgende vergaderstuktypes gedefinieerd. Deze types kunnen worden toegevoegd bij een verwijzing naar een informatieobject, zoals `<heeftAlsBijlage>`. Voor meer informatie, zie [Gebruik van ORI-A met MDTO](tutorial#gebruik-van-ori-a-met-mdto).

| Label      | Definitie                                                                  |
|:-----------|:---------------------------------------------------------------------------|
| Voorstel   | Plan waarover een besluit genomen kan worden.                              |
| Motie      | Gemotiveerde verklaring waardoor een mening of verzoek wordt uitgesproken. |
| Amendement | Voorstel om een bestaand voorstel te wijzigen.                             |
| Toezegging | Toezegging van een gedeputeerde of raadslid.                               |
| Vraag      | Vraag aan de raad.                                                         |
| Antwoord   | Antwoord op een vraag aan de raad.                                         |


# Deelnemerrollen

Binnen ORI-A zijn de enkele rollen waarin een `<aanwezigeDeelnemer>` in een vergadering aanwezig kan zijn gedefinieerd:



| Label                 | Definitie                                                                  |
|:----------------------|:---------------------------------------------------------------------------|
| Voorzitter            | De voorzitter van de vergadering.                                          |
| Vice-voorzitter       | De vice-voorzitter van de vergadering.                                     |
| Portefeuillehouder    | Ambtenaar die de verantwoordelijkheid draagt over een besproken onderwerp. |
| Griffier              | Hoofd van de griffie.                                                     |
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

# Betrokkene-vergaderstuk relaties

Een lijst met verschillende soorten relaties tussen personen en vergaderstukken. Relevant binnen MDTO om het soort relatie tussen een `<betrokkene>` en een informatieobject vast te leggen (zie [`mdto:betrokkeneTypeRelatie`](https://www.nationaalarchief.nl/archiveren/mdto/betrokkeneTypeRelatie)).



<!-- ``` xml
<informatieobject>
    ...
    <betrokkene>
        <betrokkeneTypeRelatie>
			<begripLabel>Indiener</begripLabel>
			<begripBegrippenlijst>
				<verwijzingNaam>Betrokkene-vergaderstuk relaties</verwijzingNaam>
				<verwijzingIdentificatie>
                    <identificatieKenmerk>https://www.ori-a.nl/begrippenlijsten#betrokkene-vergaderstuk-relaties</identificatieKenmerk>
                    <identificatieBron>ORI-A</identificatieBron>
                </verwijzingIdentificatie>
			</begripBegrippenlijst>
		</betrokkeneTypeRelatie>
        <betrokkeneActor>
            <verwijzingNaam>J. De Vries</verwijzingNaam>
            <verwijzingIdentificatie>
                <identificatieKenmerk>n208</identificatieKenmerk>
                <identificatieBron>ORI-A/Parleaus</identificatieBron>
            </verwijzingIdentificatie>
        </betrokkeneActor>
    </betrokkene>
</informatieobject>
```
-->


| Label              | Definitie                                                    |
|:-------------------|:-------------------------------------------------------------|
| Indiener           | Indiener van een vergaderstuk (herkomst: VNG's ORI).         |
| Ondertekenaar      | Ondertekenaar van een vergaderstuk (herkomst: VNG's ORI).    |
| Portefeuillehouder | De portefeuillehouder van een voorstel (herkomst: VNG's ORI) |

# Mediabrontypes

Deze lijst beschrijft de meest gangbare mediaformaten waarin vergaderingen worden vastgesteld. Deze waardes kun je gebruiken onder `<informatieobjectType>`, als het informatieobject waarnaar je verwijst een mediabron is.


| Label        | Definitie                                                                 |
|:-------------|:--------------------------------------------------------------------------|
| Video        | Een audiovisuele opname van een vergadering. Ook wel 'videotuul'.         |
| Audio        | Een geluidsopname van een vergadering. Ook wel 'audiotuul'.               |
| Transcriptie | Een schriftelijke uitwerking van de gesproken inhoud van een vergadering. |


