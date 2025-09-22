#!/bin/node

import { PurgeCSS } from "purgecss";
import fs from 'fs';
import path from "path";

const results = await new PurgeCSS().purge({
    // content: ["**/*.html", '*.html', './*.html'],
    content: ['site/*.html'],
    // css: ["**/*.css"],
    css: ["site/pico/pico.min.css", "site/main.css", "site/mobile.css"],
    safelist: {
        standard: [
            "[data-theme=dark]",    // keep dark theme block
            "[data-theme=light]",
            "[role=button]",
            "[role=link]"
        ],

        // regexes to match selectors that contain these substrings.
        // if a selector contains any of these the whole selector is preserved.
        deep: [
            /:hover/,            // keep hover variants
            /:focus/,            // keep focus variants
            /:active/,           // keep active variants
            /:visited/,          // keep visited link styles
            /:focus-visible/,    // keep focus-visible rules
            /:focus-within/,    // keep focus-visible rules
            /:is\(/,             // keep selectors using :is(...) combos
            /:where\(/,          // selectors starting with :where(...)
            /:where/,          // selectors starting with :where(...)
            /\[role=button/,
            /:where\(a:not/,
            /\[data-tooltip\]/,  // keep tooltip related rules
            /\[data-theme=/      // keep attribute-theme selectors anywhere
        ],

    }
});

for (const { css, file } of results) {
  const outPath = path.join("site/", path.basename(file));
  fs.mkdirSync(path.dirname(outPath), { recursive: true });
  fs.writeFileSync(outPath, css, "utf8");
  console.log(`Purged unused css from ${outPath}`);
}
