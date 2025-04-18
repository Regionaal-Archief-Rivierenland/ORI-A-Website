---
title: Begrippenlijsten
position: 2
---

# Begrippenlijsten gebruiken

Een begrippenlijst roep je zo aan:

``` xml
<vergaderstukType>
    <begripLabel>Motie</begripLabel>
    <begrippenlijstVerwijzing>
        <verwijzingID>www.ori-archiefstandaard.nl/begrippenlijsten/vergaderstuk-types</verwijzingID>
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

# Vergaderstuktypes

Binnen ORI-A zijn de volgende vergaderstuktypes gedefinieerd. Deze types worden toegevoegd bij een verwijzing naar een informatieobject, zoals `<heeftAlsBijlage>`. Zie meer hierover onder [Documentatie](https://regionaal-archief-rivierenland.github.io/ORI-A-Website/documentatie.html).

| Label      | Definitie                                                                      |
|:-----------|:-------------------------------------------------------------------------------|
| Voorstel   | Een plan waarover een besluit genomen kan worden.                              |
| Motie      | Een gemotiveerde verklaring waardoor een mening of verzoek wordt uitgesproken. |
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
