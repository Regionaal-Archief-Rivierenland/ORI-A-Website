---
title: Begrippenlijsten
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

Een paar begrippenlijsten die van toepassing zijn op **ORI•A** worden beheerd door **TOOI**, [een standaardisatie project opgezet door de rijksoverheid](https://standaarden.overheid.nl/tooi/doc/tooi-registers/):

* [Begrippenlijst Gemeentes](https://identifier.overheid.nl/tooi/set/rwc_gemeenten_compleet/4)
* [Begrippenlijst Waterschappen](https://identifier.overheid.nl/tooi/set/rwc_gemeenten_compleet/4)
* [Begrippenlijst Provincie](https://identifier.overheid.nl/tooi/set/rwc_gemeenten_compleet/4)

# Vergaderstuk types

Van belang bij bijv. `<heeftAlsBijlage>`.

| Label      | Definitie                                                                      |
|:-----------|:-------------------------------------------------------------------------------|
| Voorstel   | Een plan waarover een besluit genomen kan worden.                              |
| Motie      | Een gemotiveerde verklaring waardoor een mening of verzoek wordt uitgesproken. |
| Toezegging | Een toezegging van een gedeputeerde of raadslid.                               |
| Vraag      | Een vraag aan de raad.                                                         |
| Antwoord   | Een antwoord op een vraag aan de raad.                                         |


# Deelnemer rollen

Hoort bij `<aanwezigeDeelnemer>`. Donec vitae dolor.  Donec at pede. 


| Label              | Definitie                                                                             |
|:-------------------|:--------------------------------------------------------------------------------------|
| Voorzitter         | De voorzitter van de vergadering.                                                     |
| Griffier           | Secretaris van de raad.                                                               |
| Inspreker          | Een belanghebbende/betrokkene die inspreekt tijdens een agendapunt.                   |
| Portefeuillehouder | De ambetenaar die de verantwoordelijk draagt over het besproken onderwerp/agendapunt. |
| Raadslid           | Gekozen volksvertegenwoordiger.                                                       |
| Griffier           | Hoofd van het griffie.                                                                |
