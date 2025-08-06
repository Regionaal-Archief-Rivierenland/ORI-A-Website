FROM greyltc/archlinux-aur:paru

# create new user because paru may not be run as root
RUN useradd -m -G wheel builder && \
    echo 'builder ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers
RUN mkdir -p /ori-a-website
RUN chgrp wheel /ori-a-website
RUN chmod -R g+rxw /ori-a-website

USER builder

WORKDIR ori-a-website

# Install build dependencies
RUN paru -Syu --skipreview --removemake --cleanafter --noconfirm \
    scour ripgrep fd make git sudo \
    minify-html-bin uglify-js lightningcss-cli-bin pandoc-bin \
    python-fonttools python-jinja python-beautifulsoup4 python-frontmatter python-setuptools python-brotli \
    texlive-basic texlive-latexextra texlive-plaingeneric texlive-latexrecommended texlive-fontsextra texlive-langeuropean 

# cleanup unused pkgs and cache
RUN paru --noconfirm -c -Rs python-setuptools gcc
RUN paru --noconfirm -Scc
