---
title: Begrippenlijsten
position: 4
---

# Begrippenlijsten gebruiken

<!-- Het lijkt me een goed idee om te beginnen met een algemeen stuk over het hoe en waarom van begrippenlijsten en hun nut bij standaardisatie. Eventueel met link naar de MDTO en TOOI begrippenlijsten. -->

Een begrippenlijst roep je zo aan:

``` xml
<vergaderstukType>
    <begripLabel>Motie</begripLabel>
    <begrippenlijstVerwijzing>
        <verwijzingID>www.ori-a.nl/begrippenlijsten#vergaderstuk-types</verwijzingID>
        <verwijzingNaam>ORI-A Begrippenlijst Vergaderstuk Types</verwijzingNaam>
    </begrippenlijstVerwijzing>
</vergaderstukType>
```

Alle begrippenlijsten die onderdeel zijn van **ORI•A** worden hieronder gedocumenteerd.

## TOOI Begrippenlijsten

Een paar begrippenlijsten die van toepassing zijn op **ORI•A** worden beheerd door **TOOI**, [een standaardisatie project opgezet door de Rijksoverheid](https://standaarden.overheid.nl/tooi/doc/tooi-registers/):

* [Begrippenlijst Gemeentes](https://identifier.overheid.nl/tooi/set/rwc_gemeenten_compleet/4)
* [Begrippenlijst Waterschappen](https://identifier.overheid.nl/tooi/set/rwc_gemeenten_compleet/4)
* [Begrippenlijst Provincie](https://identifier.overheid.nl/tooi/set/rwc_gemeenten_compleet/4)

# Vergaderstuk types

Binnen ORI-A zijn de volgende vergaderstuktypes gedefinieerd. Deze types kunnen worden toegevoegd bij een verwijzing naar een informatieobject, zoals `<heeftAlsBijlage>`. Voor meer informatie, zie [Gebruik van ORI-A met MDTO](tutorial#gebruik-van-ori-a-met-mdto).

| Label      | Definitie                                                                      |
|:-----------|:-------------------------------------------------------------------------------|
| Voorstel   | Een plan waarover een besluit genomen kan worden.                              |
| Motie      | Een gemotiveerde verklaring waardoor een mening of verzoek wordt uitgesproken. |
| Amendement | Een voorstel om een bestaand voorstel te wijzigen.                             |
| Toezegging | Een toezegging van een gedeputeerde of raadslid.                               |
| Vraag      | Een vraag aan de raad.                                                         |
| Antwoord   | Een antwoord op een vraag aan de raad.                                         |


# Deelnemerrollen

Binnen ORI-A zijn de volgende deelnemerrollen gedefinieerd. Deze rollen horen bij `<aanwezigeDeelnemer>`. 


| Label              | Definitie                                                                             |
|:-------------------|:--------------------------------------------------------------------------------------|
| Voorzitter         | De voorzitter van de vergadering.                                                     |
| Griffier           | Secretaris van de raad.                                                               |
| Inspreker          | Een belanghebbende/betrokkene die inspreekt tijdens een agendapunt.                   |
| Portefeuillehouder | De ambtenaar die de verantwoordelijk draagt over het besproken onderwerp/agendapunt.  |
| Raadslid           | Gekozen volksvertegenwoordiger.                                                       |
| Griffier           | Hoofd van het griffie.                                                                |


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


