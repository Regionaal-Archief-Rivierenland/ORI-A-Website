# Website bewerken

Om de website te bewerken kun je simpelweg een `.md` bestand in de map `pages/` aanpassen/toevoegen.

Let er op dat je bij het aanmaken van een nieuw `.md` bestand de juiste metadata toevoegt:

``` markdown
---
title: [Naam van de pagina]
position: 3
---
```

`title` is de titel van de pagina (die zie je terug in de URL en in de navigatiebalk), `position` is de plek in de navigatiebalk waar de pagina in kwestie komt.


# Website (lokaal) bouwen

De website wordt automatisch opnieuw gebouwd en gepubliceerd na elke commit.

Het lokaal bouwen van de website komt neer op `make` runnen, mits je alle dependencies hebt.  Na `make` komt de "site" (i.e. de _build artifacts_) in de map `site/`. Omdat het bouwprocess nogal wat dependencies heeft, is het meestal aan te raden om de website te bouwen [met behulp van de speciaal hiervoor gemaakte docker container](buildtools/).


De site kun je na het bouwen raadplegen door bijv. `python -m http.server .` in de map `site/` aan te roepen.

> [!NOTE]
> Dit project gebruikt de ORI-A XSD als git submodule. Hierom moet je na `git clone https://github.com/Regionaal-Archief-Rivierenland/ORI-A-Website` ook nog `git submodule update --init --recursive` runnen.

# Wat is wat

> [!IMPORTANT]
> Als je simpelweg teksten op de website wilt wijzigen, ben je aangewezen op de bestanden in de map `pages/`

* `pages/`
  * De markdown bestanden waaruit de documentatie/documentatie website wordt opgebouwd
  * `pages/*.md.j2` bestanden zijn een combinatie van markdown en Jinja template.
* `css/`
  * Verschillende stijlregels. Het grootste gedeelte van de css is afkomstig van het [Pico](https://picocss.com/docs) project.
* `diagram/`
  * ORI-A _UML-inspired_ diagram, opgesteld in Latex; moet nog gerendered worden met jinja
* `js/`
  * Kleine stukjes javascript die op de site gebruikt worden
* `templates/`
  * Het HTML "skelet" (i.e. templates) waar de inhoud van de markdown bestanden in wordt gezet
* `buildpages.py`
  * Gebruikt Jinja om de eerder naar HTML geconverteerde bestanden in de templates te stoppen
  * Doet ook wat HTML nabewerkingen
* `buildtables.py`
  * Zet de gegevensgroep tabellen in `pages/documentatie.md.j2` en in `diagram/ORI-A-diagram.tex.j2`
* `ims/`
  * Afbeelingen
* `buildtools/`
  * Dockerfile waarmee een container wordt gebouwd die alle dependencies voor het bouwen van de website bundeld. Deze container wordt in de CI bouw-stap gebruikt omdat het sneller is dan alle dependencies los via `apt-get`, `pip`, etc. downloaden, maar is ook vooral heel handig als je de website zelf lokaal wilt bouwen, en geen zin hebt om zelf alle dependencies bij elkaar te sprokkelen!
* `fonts/`
  * `.woff2` bestanden. Zijn nog niet gesubset! Dat doet de Makefile.
* `Makefile`
  * GNU makefile die alle scripts uitvoert die nodig zijn om de website te bouwen en _resources_ te minimaliseren
  * Heeft ~~te veel~~ heel veel afhankelijkheden

# Attributies

De ORI-A website gebruikt icoontjes uit de volgende projecten:

* [iconior](https://iconoir.com/) (MIT License)
* [phosphor](https://phosphoricons.com/) (MIT License)
