# Website bewerken

Om de website te bewerken kun je simpelweg een `.md` bestand in de map `pages/` aanpassen/toevoegen.

Let er op dat je bij het aanmaken van een nieuw `.md` bestand de juiste metadata toevoegt:

``` markdown
---
title: [Naam van de pagina]
position: 3
---
```

`title` is de titel van de pagina (die zie je terug in de URL en in de navigatiebalk), `position` is de plek in de navigatienbalk/PDF waar de pagina in kwestie komt.


# Website (lokaal) bouwen

TBA; maar in principe gewoon `make` runnen. Na `make` komt de "site" (i.e. de _build artifacts_) in de map `site/`. 

Die kun je vervolgens raadplegen door bijv. `python -m http.server` in die map aan te roepen.

# Wat is wat

* `pages/`
  * De markdown bestanden waaruit de documentatie/documentatie website wordt opgebouwd
* `css/`
  * Verschillende stijlregels. Het grootste gedeelte van de css is afkomstig van het [Pico](https://picocss.com/docs) project.
* `templates/`
  * Het HTML "skelet" (i.e. templates)  waar de markdown bestanden in worden gezet
* `buildpages.py`
  * Gebruikt Jinja2 om de eerder naar HTML geconverteerde bestanden in de templates te stoppen
  * Doet ook wat HTML nabewerkingen
* `ims/`
  * Afbeelingen
* `fonts/`
  * `.woff2` bestanden. Zijn nog niet gesubset! Dat doet de Makefile.
* `Makefile`
  * GNU makefile die alle scripts uitvoert die nodig zijn om de website te bouwen en _resources_ te minimaliseren
  * Heeft ~~te veel~~ heel veel afhankelijkheden
