CSS_SRC := css/
CSS_DST := site/

CSS_FILES := main.css pico/pico.min.css mobile.css
CSS_DST_FILES := $(addprefix $(CSS_DST),$(CSS_FILES))

SVG_SRC := $(wildcard ims/*.svg)
SVG_DST := $(patsubst ims/%,site/%,$(SVG_SRC))

JS_SRC := $(wildcard js/*.js)
JS_DST := $(patsubst js/%.js, site/%.js, $(JS_SRC))

PDF_SRC := $(wildcard pdfs/*.pdf)
PDF_DST := $(patsubst pdfs/%.pdf, site/%.pdf, $(PDF_SRC))

MD_SRC := $(wildcard pages/*.md)
HTML_DST := $(patsubst pages/%.md,pages/%.html,$(MD_SRC))

MAIN_HTML = over-ori-a.html

FONT_TITLE := lato.woff2
FONT_TITLE_BOLD := lato-bold.woff2
FONT_MONOSPACE := CommitMonoVariable.woff2

FONT_INPUTS := fonts/$(FONT_TITLE) fonts/$(FONT_TITLE_BOLD) fonts/$(FONT_MONOSPACE)
FONT_OUTPUTS := site/$(FONT_TITLE) site/$(FONT_TITLE_BOLD) site/$(FONT_MONOSPACE)

TABLE_SRC := pages/documentatie.md.j2 templates/gegevensgroep_table.html
TABLE_DST := pages/documentatie.md

.PHONY: all clean

# Default target
all: generate-tables buildpages minify subset-fonts

# Create site/ directory
$(CSS_DST) $(HTML_DST): | site
site:
	mkdir -p $(CSS_DST)

# to strip unused css: 
# ./node_modules/purgecss/bin/purgecss.js --content "site/*.html" "js/*.js" --css $@ --output $@
# (but this seems to be buggy)

# Minize CSS
$(CSS_DST)%: $(CSS_SRC)%
	@mkdir -p $(@D)
	lightningcss --minify $< -o $@

# Minimize SVG
site/%.svg: ims/%.svg
	scour --strip-xml-prolog --no-line-breaks --enable-comment-stripping -i $< -o $@

site/%.pdf: pdfs/%.pdf
	cp $< $@

# Convert Markdown to HTML
# NOTE: currently breaks if you use filenames with spaces
pages/%.html: pages/%.md
	@mkdir -p $(@D)
	pandoc $< -o $@

subset-fonts: $(FONT_OUTPUTS)

$(FONT_OUTPUTS): $(MD_SRC) $(FONT_INPUTS)
    # Use titles and headers to subset lato
	titles_and_headers=$$(rg -e '^title: (.*)' -e '^\#(.*)' -r '$$1$$2' --no-filename pages/*md); \
	pyftsubset fonts/$(FONT_TITLE) \
        --drop-tables=FFTM,feat,meta \
		--flavor=woff2 --layout-features="kern,liga" \
		--text="Open raadsinformatie Archiefstandaard$$titles_and_headers" \
		--output-file=site/$(FONT_TITLE) ; \
	pyftsubset fonts/$(FONT_TITLE_BOLD) \
        --drop-tables=FFTM,feat,meta \
		--flavor=woff2 --layout-features="kern,liga" \
		--text="$$titles_and_headers" \
		--output-file=site/$(FONT_TITLE_BOLD)

    # Subset monospace font based on text between pairs of "```"/"`"
    # removing the name table as above creates problems,
    # for some reason
    # Capital letter 'Y' is needed for a tooltip
	code_snippets=$$( \
		rg --no-filename -U --multiline-dotall '```[^\n]*\n(.*?)```' -r '$$1' pages/*md; \
		rg --no-filename -o '[^`]`(.*)`' -r '$$1' pages/*md \
	); \
	pyftsubset fonts/$(FONT_MONOSPACE) \
        --drop-tables=FFTM,feat,meta \
		--flavor=woff2 --layout-features="kern" \
		--text="$$code_snippets""Y" \
		--output-file=site/$(FONT_MONOSPACE)

# copy/minify js
site/%.js: js/%.js
	uglifyjs $< -o $@ -c -m

generate-tables: $(TABLE_DST)

$(TABLE_DST): $(TABLE_SRC)
	python3 buildtables.py

# Build HTML pages (depends on all build artifacts)
buildpages: $(TABLE_DST) $(HTML_DST) $(CSS_DST_FILES) $(SVG_DST) $(JS_DST) $(PDF_DST)
	python3 buildpages.py
	ln -srf site/$(MAIN_HTML) site/index.html

minify: buildpages
	minify-html --minify-js $$(fd -ehtml . site/)

# Clean up
clean:
	rm -rf site
	rm pages/documentatie.md
	fd . -ehtml pages/ --exclude index.html -X rm 
