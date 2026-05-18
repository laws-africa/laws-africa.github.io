# Repository Guidelines

## Project Structure & Module Organization

This repository builds the Laws.Africa GitHub Pages site with Pelican. Markdown
pages live in `content/pages/`; blog posts live in `content/articles/YYYY/MM/DD/`.
Static assets are under `content/static/`, with images in `img/`, uploads in
`uploads/`, and JavaScript in `js/`. Jinja templates and theme styles live in
`theme/lawsafrica/templates/` and `theme/lawsafrica/static/scss/`. Shared data is
in `data/`, and Pelican support code is in `tools/`.

## Build, Test, and Development Commands

- `source .venv/bin/activate`: activate the local Python environment.
- `python -m pip install -e .`: install Pelican and project tooling.
- `npm install`: install Bootstrap and Bootstrap Icons assets used by the theme.
- `build-pelican-site`: compile Sass, render Pelican content, and write
  `.pelican-output/`.
- `python -m http.server 8000 --directory .pelican-output`: preview the built
  site at `http://localhost:8000`.

## Coding Style & Naming Conventions

Use concise Markdown front matter with existing fields such as `title`, `slug`,
`save_as`, `url`, `template`, `date`, and `navbar_item`. Prefer prose-only
Markdown pages for content-heavy pages, and add a matching template when a page
needs Bootstrap layout, Jinja loops, includes, or `site` data. Keep Jinja
partials prefixed with `_`, such as `_navbar.html`.

## Layout & Visual Style

Use Bootstrap 5 components and utilities as the default design language. Keep
layouts simple: `container`, `row`, `col-*`, `card`, `lead`, `table`, `btn`, and
spacing utilities. Avoid elaborate custom design, decorative effects, or new
component systems. Most pages start with a `<header>`
using `py-5` and `bg-lawsafrica-pale-red` (`$pale-red: #fad7d5`), containing an
`h1.display-4` and one short `.lead` sub-heading. Use `bg-light` or existing
`bg-*` classes for zebra striping between sections, usually with `py-5`.
Import SCSS through `main.scss`.

## Testing Guidelines

There is no separate automated test suite. Treat `build-pelican-site` as the
required validation step. After building, preview affected routes locally and
check browser console errors for JavaScript or layout changes.

## Commit & Pull Request Guidelines

Recent history uses short, imperative or descriptive commit subjects such as
`fix build`, `bootstrap icons`, and `Updated commons stats`. Keep commits focused
on one change area. Pull requests should summarize the user-visible change,
list validation performed, and include screenshots for visual changes. Mention
touched content paths, templates, or data files.

## Security & Configuration Tips

Do not commit secrets or local credentials. The scheduled stats workflow expects
`INDIGO_API_TOKEN` from GitHub Actions secrets and updates only
`data/commons.json`. Keep generated directories such as `.pelican-output/`,
`.pelican-build/`, virtualenvs, and dependency folders out of source edits.
