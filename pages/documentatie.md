---
title: Documentatie
position: 2
---


**Rijnder <mark>Opmerking</mark>**: Ik denk dat deze pagina uiteindelijk is bedoeld voor technische documentatie. Een beetje iets als dit, maar dan met meer XML voorbeelden: <https://vng-realisatie.github.io/ODS-Open-Raadsinformatie/catalog>


# Voorbeeldbestanden

Je kan de voorbeeldbestanden hier downloaden:

# Visuele weergave

Hier komt de visuele weergave van ORI-A te staan.

<!-- ![ORI-A Diagram](ORI-A-diagram.svg) -->

<!-- <div style="width: 100%; height: 600px; overflow: auto; border: 1px solid #ccc;"> -->
<!--   <iframe src="ORI-A-diagram.svg" style="width: 100%; height: 100%; border: none;"></iframe> -->
<!-- </div> -->


# Gebruik van ORI-A met MDTO

ORI-A is zo opgesteld dat een gezamenlijk gebruik met MDTO zo min mogelijk dubbele data zou moeten opleveren. Alle verwijzingen  __ORI-A --> MDTO__  nemen de volgende vorm aan:

``` xml
<informatieobjectGegevens>
    <informatieobjectType>Motie</informatieobjectType>
    <verwijzingInformatieobject>
        <verwijzingID>1234</verwijzingID>
        <verwijzingNaam>Motie_van_lid_Smit</verwijzingNaam>
    </verwijzingInformatieobject>
<informatieobjectGegevens>
```
De verwijzing naar MDTO of ToPX gebeurt op het niveau van informatieobjecten en niet van bestanden. De verwijzing tussen informatieobjecten en bestanden kan in MDTO worden uitgedrukt. Daarbij biedt ORI-A de mogelijkheid om te verwijzen door middel van een ID (verplicht) en/of een naam (niet verplicht).

De enige inhoudelijke informatie over informatieobjecten die in ORI-A wordt opgenomen is het `<informatieobjectType>`. Dit heeft enige inhoudelijke overlap met `<classificatie>` binnen MDTO en ToPX. De reden waarom het alsnog in ORI-A is opgenomen is dat dit domeinspecifieke informatie betreft die in de context van een vergadering relevant is. Een gebruiker die alleen ORI-A data zou raadplegen, zou in dat geval alsnog de rol die het informatieobject heeft gespeeld binnen een vergadering kunnen afleiden.

Vanuit de volgende ORI-A elementen wordt er verwezen naar MDTO/ToPX:

| ORI-A element | Verwijzing             | MDTO element      |
|:--------------|:-----------------------|:------------------|
| Mediabron     | isvastgelegdIn         | Informatieobject  |
| Mediabron     | heeftOndertitelbestand | Informatieobject  |
| Vergadering   | isgenotuleerdIn        | Informatieobject  |
| Vergadering   | heeftalsBijlage        | Informatieobject  |
| Agendapunt    | heeftalsBijlage        | Informatieobject  |
| Stemming      | heeftbetrekkingOp      | Informatieobject  |

# Verplichte elementen in ORI-A

ORI-A kent relatief weinig verplichte elementen. Iedere ORI-A XML moet ten minste één `<vergadering>`, `<agendapunt>` en `<mediabron>` bevatten. Dit is vanuit de gedachte dat er altijd een vergadering moet zijn geweest waar data over is gegenereerd, deze vergadering altijd minstens één agendapunt moet hebben gehad en er altijd een audio en/of visueel verslag moet zijn opgesteld om te kunnen worden gearchiveerd.

# Vormgeving van ORI-A XML-bestanden

Het ORI-A XML-schema is zo opgesteld dat er maximaal één vergadering per ORI-A XML-bestand wordt uitgedrukt. Hierdoor konden de interne verwijzingen tussen andere ORI-A elementen en `<vergadering>` simpel worden gehouden. 

Het ORI-A XML-schema staat overigens toe dat gegevens over één vergadering over meerdere ORI-A XML-bestanden worden verspreid. Uit opnametests is gebleken dat sommige e-depots metagegevens (zoals ORI-A data) direct aan mappen of digitale bestanden koppelen. In dat geval kan het wenselijk zijn om de ORI-A XML-bestanden op te knippen in meerdere bestanden, zodat ze makkelijk aan het juiste niveau kunnen worden gerelateerd.
