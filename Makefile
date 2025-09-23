CSS_SRC := css/
CSS_DST := site/

CSS_FILES := main.css pico/pico.min.css mobile.css
CSS_DST_FILES := $(addprefix $(CSS_DST),$(CSS_FILES))

SVG_SRC := $(wildcard ims/*.svg)
SVG_DST := $(patsubst ims/%,site/%,$(SVG_SRC))

PNG_SRC := $(wildcard ims/*.png)
PNG_DST := $(patsubst ims/%,site/%,$(PNG_SRC))

JS_SRC := $(wildcard js/*.js)
JS_DST := site/concat.js

PDF_SRC := $(wildcard pdfs/*.pdf)
PDF_DST := $(patsubst pdfs/%.pdf, site/%.pdf, $(PDF_SRC))

MD_SRC := $(wildcard pages/*.md)
HTML_DST := $(patsubst pages/%.md,pages/%.html,$(MD_SRC))

# we're not compiling this everytime, because the pipeline kind of sucks. Like this pulls inkscape
# VALIDATIE_DIAGRAM_DST := site/validatie.svg
# VALIDATIE_DIAGRAM_TEX := diagram/validatie.tex
# # validatie.tex depends on specific svgs to compile
# VALIDATIE_DIAGRAM_DEPS := $(VALIDATIE_DIAGRAM_TEX) diagram/empty-page.svg diagram/window-xml.svg diagram/xmark-solid.svg diagram/check-solid.svg 

MAIN_HTML = over-ori-a.html

FONT_TITLE := lato.woff2
FONT_TITLE_BOLD := lato-bold.woff2
FONT_TITLE_HEAVY := lato-black.woff2
FONT_MONOSPACE := CommitMonoVariable.woff2

FONT_INPUTS := fonts/$(FONT_TITLE) fonts/$(FONT_TITLE_BOLD) fonts/$(FONT_TITLE_HEAVY) fonts/$(FONT_MONOSPACE)
FONT_OUTPUTS := site/$(FONT_TITLE) site/$(FONT_TITLE_BOLD) site/$(FONT_TITLE_HEAVY) site/$(FONT_MONOSPACE)

TABLE_SRC := pages/xml-schema.md.j2 templates/gegevensgroep_table.html ORI-A-XSD/ORI-A.xsd diagram/ORI-A-diagram.tex.j2
TABLE_DST := pages/xml-schema.md diagram/ORI-A-diagram.tex

VOORBEELDZIP := site/ORI-A\ voorbeeldbestanden.zip
PRESERVICAZIP := site/Preservica_documentatieset.zip

.PHONY: all clean update-submodule

# Default target
all: generate-tables buildpages minify subset-fonts

update-submodule:
	git submodule update --recursive --remote

$(VOORBEELDZIP): $(shell fd . -tfile 'ORI-A-XSD/Voorbeelden')
	ln -sf ORI-A-XSD/Voorbeelden "ORI-A voorbeeldbestanden" && \
	zip -r "$@" "ORI-A voorbeeldbestanden" && \
	unlink "ORI-A voorbeeldbestanden"

$(PRESERVICAZIP): misc/Preservica_documentatieset.zip
	cp $< $@

site/ORI-A.xsd: ORI-A-XSD/ORI-A.xsd
	cp ORI-A-XSD/ORI-A.xsd site/

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
	scour --enable-id-stripping --protect-ids-list=$$(rg -I 'svg.*#(\w+)' -r '$$1' -o pages/* | sd '\n' ',') --remove-descriptive-elements --strip-xml-prolog --no-line-breaks --enable-comment-stripping --indent=none -i $< -o $@

site/%.png: ims/%.png
	optipng -clobber -o3 $< -out $@

# TODO: optimize pdfs?
site/%.pdf: pdfs/%.pdf
	cp $< $@

# Convert Markdown to HTML
# NOTE: currently breaks if you use filenames with spaces
pages/%.html: pages/%.md
	@mkdir -p $(@D)
	pandoc --wrap=none -f markdown-native_divs $< -o $@

subset-fonts: $(FONT_OUTPUTS)

$(FONT_OUTPUTS): $(MD_SRC) $(FONT_INPUTS)
    # Use titles and headers to subset lato
	@titles=$$(rg '^title: (.*)' -r '$$1' --no-filename pages/*md) ; \
	headers=$$(rg '^\#(.*?)(\{.*\})?$$' -r '$$1' --no-filename pages/*md) ; \
	headers_h2h3=$$(rg '^\#\#? ([A-z].*?)(\{.*\})?$$' -r '$$1' --no-filename pages/*md) ; \
	headers_sans_dropdowns=$$(rg '^\#.*' --no-filename pages/*md | grep -v dropdown) ; \
	pyftsubset fonts/$(FONT_TITLE) \
        --drop-tables=FFTM,feat,meta \
		--flavor=woff2 --layout-features="kern,liga" \
		--text="Open raadsinformatie • Archiefstandaard$$headers_h2h3" \
		--output-file=site/$(FONT_TITLE) ; \
	pyftsubset fonts/$(FONT_TITLE_BOLD) \
        --drop-tables=FFTM,feat,meta \
		--flavor=woff2 --layout-features="kern,liga" \
		--text="$$titles$$headers_sans_dropdowns" \
		--output-file=site/$(FONT_TITLE_BOLD) ; \
	pyftsubset fonts/$(FONT_TITLE_HEAVY) \
        --drop-tables=FFTM,feat,meta \
		--flavor=woff2 --layout-features="kern" \
		--text="$$titles</>" \
		--output-file=site/$(FONT_TITLE_HEAVY) ; \

    # Subset monospace font based on text between pairs of "```"/"`"
    # removing the name table as above creates problems,
    # for some reason
    # Capital letter 'Y' is needed for a tooltip
    # the first cmd gets all code blocks, and uses sd to remove full pairs whose opening ``` contains {
	code_snippets=$$( \
		rg -U -I --multiline-dotall '```.*?```' pages/*md | sd -f s '``` ?\{.*?\}.*?```' '' | rg -v '```'; \
		rg -I -o '[^`]`(.*?)`' -r '$$1' pages/*md \
	); \
	pyftsubset fonts/$(FONT_MONOSPACE) \
        --drop-tables=FFTM,feat,meta \
		--flavor=woff2 --layout-features="kern" \
		--text="$$code_snippets""YURI" \
		--output-file=site/$(FONT_MONOSPACE)

# copy/minify js
$(JS_DST): $(JS_SRC)
	uglifyjs js/*.js -o $@ -c -m --toplevel --rename


$(VALIDATIE_DIAGRAM_DST): $(VALIDATIE_DIAGRAM_DEPS)
	pdflatex --shell-escape $(VALIDATIE_DIAGRAM_TEX)
	mutool draw -o $@ diagram/validatie.pdf

generate-tables: $(TABLE_DST)

$(TABLE_DST): $(TABLE_SRC)
	python3 buildtables.py
	pdflatex -output-dir pdfs diagram/ORI-A-diagram.tex

prepare-site: $(TABLE_DST) $(HTML_DST) $(CSS_DST_FILES) $(SVG_DST) $(PNG_DST) $(JS_DST) $(PDF_DST) $(VOORBEELDZIP) site/ORI-A.xsd $(PRESERVICAZIP)

# Build HTML pages (depends on all build artifacts)
buildpages: prepare-site
	python3 buildpages.py
	ln -srf site/$(MAIN_HTML) site/index.html
    # replace normal hyphens by non-breaking ones
    # todo: do this in more places
	sd  -F 'Wanneer gebruik je ORI-A' 'Wanneer gebruik je ORI‑A' site/faq.html

minify: buildpages
	minify-html --minify-js $$(fd -ehtml . site/)
    # purge unused css (with custom script, since the purgecss cli acted weird)
	./purge.mjs

PANDOCFLAGS = -V geometry:margin=3.5cm -V papersize:a4 -H /tmp/linenumbers.tex

pdf: buildpages
    # generate markdown variant of xml-schema
	python buildtables.py markdown

	printf '%s\n' '\usepackage{lineno}' '\linenumbers' > /tmp/linenumbers.tex

	pandoc ${PANDOCFLAGS} pages/over-ori-a.md -o /tmp/over-ori-a.pdf
	pandoc ${PANDOCFLAGS} --pdf-engine xelatex pages/downloads.md -o /tmp/downloads.pdf
	pandoc ${PANDOCFLAGS} pages/xml-schema.md -o /tmp/xml-schema.pdf
	pandoc ${PANDOCFLAGS} pages/begrippenlijsten.md -o /tmp/begrippenlijsten.pdf
	pandoc ${PANDOCFLAGS} pages/hoe-werkt-ori-a.md -o /tmp/hoe-werkt-ori-a.pdf
	pandoc ${PANDOCFLAGS} pages/colofon.md -o /tmp/colofon.pdf
	pandoc ${PANDOCFLAGS} pages/faq.md -o /tmp/faq.pdf

    # cleanup artifacts
	rm pages/xml-schema.md site/xml-schema.html

# Clean up
clean:
	rm -rf site
	rm -f pages/xml-schema.md
	fd . -ehtml pages/ --exclude index.html -X rm
