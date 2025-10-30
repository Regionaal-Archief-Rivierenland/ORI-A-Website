FROM greyltc/archlinux-aur:paru

# update keyring
RUN pacman-key --init && sudo pacman -Sy --noconfirm archlinux-keyring

USER ab

WORKDIR /ori-a-website

# Install build dependencies
RUN paru -Syu --skipreview --asexplicit --removemake --cleanafter --noconfirm \
    scour ripgrep fd make git optipng sd zip mupdf-tools \
    minify-html-bin uglify-js lightningcss-cli-bin pandoc-bin npm \
    python-fonttools python-jinja python-beautifulsoup4 python-frontmatter python-setuptools python-brotli \
    texlive-basic texlive-latexextra texlive-plaingeneric texlive-latexrecommended texlive-fontsextra texlive-langeuropean 

# cleanup unused pkgs and cache
RUN paru --noconfirm -c -Rss python-setuptools 
RUN paru --noconfirm -Scc
RUN sudo pacman --noconfirm -Scc
RUN sudo pacman --noconfirm -Rs base-devel


USER root
