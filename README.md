# Guitar Doug Report: Seattle Edition (mirror)

A mirror of [douggarceau/seattlesinner](https://github.com/douggarceau/seattlesinner). Every 15 minutes, and on every push here, a GitHub Actions job:

1. Copies the public seattlesinner site.
2. Swaps in the Seattle Edition masthead (`overlay/img/masthead-edition.png`).
3. Publishes the result to GitHub Pages.

All content, including stories, headlines, calendar and directory, comes from seattlesinner. Never edit content here.

**Domain:** once guitardougreport.com is bought and its DNS points to GitHub Pages, set `MIRROR_DOMAIN` in `.github/workflows/mirror.yml` and add the domain under Settings → Pages.
