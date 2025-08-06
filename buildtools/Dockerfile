FROM greyltc/archlinux-aur:paru

USER ab

WORKDIR /ori-a-website

# Install build dependencies
RUN paru -Syu --skipreview --removemake --cleanafter --noconfirm \
    scour ripgrep fd make git \
    minify-html-bin uglify-js lightningcss-cli-bin pandoc-bin \
    python-fonttools python-jinja python-beautifulsoup4 python-frontmatter python-setuptools python-brotli \
    texlive-basic texlive-latexextra texlive-plaingeneric texlive-latexrecommended texlive-fontsextra texlive-langeuropean 

# cleanup unused pkgs and cache
RUN paru --noconfirm -c -Rss python-setuptools 
RUN paru --noconfirm -Scc
RUN yes | sudo pacman -Scc 

USER root
