CSS_SRC := css/
CSS_DST := site/css/

CSS_FILES := main.css pico/pico.min.css mobile.css
CSS_DST_FILES := $(addprefix $(CSS_DST),$(CSS_FILES))

SVG_SRC := $(wildcard ims/*.svg)
SVG_DST := $(patsubst ims/%,site/%,$(SVG_SRC))

JS_SRC := $(wildcard js/*.js)
JS_DST := $(patsubst js/%.js, site/%.js, $(JS_SRC))

MD_SRC := $(wildcard pages/*.md)
HTML_DST := $(patsubst pages/%.md,pages/%.html,$(MD_SRC))

MAIN_HTML = over-ori-a.html

.PHONY: all clean

# Default target
all: buildpages minify

# Create site/ directory
$(CSS_DST) $(HTML_DST): | site
site:
	mkdir -p $(CSS_DST)

# Copy CSS files to the site folder
# TODO: minimize CSS; minify-html apperently doesn't cut it
$(CSS_DST)%: $(CSS_SRC)%
	@mkdir -p $(@D)
	lightningcss --minify $< -o $@

# Minimize SVG
site/%.svg: ims/%.svg
	scour -i $< -o $@

# Convert Markdown to HTML
# NOTE: currently breaks if you use filenames with spaces
pages/%.html: pages/%.md
	@mkdir -p $(@D)
	pandoc $< -o $@

# Copy index.html
# index.html currently only redirects to something else
# site/index.html: pages/index.html | site/
# 	cp $< $@

# copy/minify js
site/%.js: js/%.js
	uglifyjs $< -o $@ -c -m

# Build HTML pages (depends on all build artifacts)
buildpages: $(HTML_DST) $(CSS_DST_FILES) $(SVG_DST) $(JS_DST)
	python buildpages.py
	ln -srf site/$(MAIN_HTML) site/index.html

# FIXME: this currently strips too much, breaking html
minify: buildpages
	minify-html $$(fd -ehtml . site/)

# Clean up
clean:
	rm -rf site
	fd . -ehtml pages/ --exclude index.html -X rm 
