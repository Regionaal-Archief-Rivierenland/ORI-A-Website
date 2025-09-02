---
title: Begrippenlijsten
position: 4
---

<!-- Het lijkt me een goed idee om te beginnen met een algemeen stuk over het hoe en waarom van begrippenlijsten en hun nut bij standaardisatie. Eventueel met link naar de MDTO en TOOI begrippenlijsten. -->

Op deze pagina is informatie te vinden over de momenten waarop ORI-A gebruik maakt van begrippenlijsten. Een begrippenlijst is een manier om gegevens te relateren aan een extern vastgestelde (gecontroleerde) lijst van waarden. ORI-A volgt de definitie, semantiek en toepassing van begrippenlijsten zoals die ook in [MDTO](https://www.nationaalarchief.nl/archiveren/mdto/begripbegrippenlijst) worden gehanteerd.

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

Een paar begrippenlijsten die van toepassing zijn op **ORI-A** worden beheerd door **TOOI**, [een standaardisatie project opgezet door de Rijksoverheid](https://standaarden.overheid.nl/tooi/doc/tooi-registers/):

* [Begrippenlijst Gemeentes](https://identifier.overheid.nl/tooi/set/rwc_gemeenten_compleet/4)
* [Begrippenlijst Waterschappen](https://identifier.overheid.nl/tooi/set/rwc_gemeenten_compleet/4)
* [Begrippenlijst Provincie](https://identifier.overheid.nl/tooi/set/rwc_gemeenten_compleet/4)

# Vergaderstuk types

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

::: waarschuwing
De rol "Overig" bestaat om compatibiliteit met het oorspronkelijke ORI informatiemodel te garanderen. Het gebruik van deze rol wordt afgeraden. Als de bestaande rollen niet toereikend zijn, heb je drie opties:

1. Een uitbreiding op deze begrippenlijst [aanvragen](https://github.com/Regionaal-Archief-Rivierenland/ORI-A-Website/issues/new)
2. Een nieuwe begrippenlijst starten
3. Deze begrippenlijst uitbreiden

:::


| Label                 | Definitie                                                              |
|:----------------------|:-----------------------------------------------------------------------|
| Voorzitter            | De voorzitter van de vergadering.                                      |
| Vice-voorzitter       | De vice-voorzitter van de vergadering.                                 |
| Portefeuillehouder    | Ambtenaar die de verantwoordelijk draagt over een besproken onderwerp. |
| Griffier              | Hoofd van het griffie.                                                 |
| Raadslid              | Gekozen volksvertegenwoordiger binnen een gemeente.                    |
| Statenlid             | Gekozen volksvertegenwoordiger binnen een provincie.                   |
| Kamerlid              | Gekozen volksvertegenwoordiger binnen de eerst of tweede kamer.        |
| Dagelijks bestuurslid | Lid van een dagelijks bestuur.                                         |
| Algemeen bestuurslid  | Lid van het algemeen bestuur van een waterschap.                       |
| Inspreker             | Niet-lid dat inspreekt tijdens de vergadering.                         |
| <del>Overig</del>     | -                                                                      |

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

# Mediabron types

Deze lijst beschrijft de meest gangbare mediaformaten waarin vergaderingen worden vastgesteld. Deze waardes kun je gebruiken onder `<informatieobjectType>`, als het informatieobject waarnaar je verwijst een mediabron is.


| Label        | Definitie                                                                   |
|:-------------|:----------------------------------------------------------------------------|
| Video        | Een audiovisuele opname van een vergadering. Ookwel 'videotuul'.            |
| Audio        | Een geluidsopname van een vergadering. Ookwel 'audiotuul'.                   |
| Transcriptie | Een schriftelijk uitverwerking van de gesproken inhoud van een vergadering. |


