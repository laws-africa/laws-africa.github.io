# laws.africa website

This is a GitHub Pages website for [laws.africa](https://laws.africa).

# Changing content

Pages live under `content/pages/`, blog posts under `content/articles/`, shared
data under `data/`, and templates under `theme/lawsafrica/templates/`.

## Choosing Markdown or a Template

Use Markdown content when the page is primarily prose and only needs Markdown or
very small inline HTML. For example, `about.md` is content-first and can stay as
Markdown.

Use a dedicated template when the page needs structured layout, Bootstrap-heavy
HTML, includes, loops, conditionals, scripts, or data from front matter / `site`.
For example, `scanstations.md` keeps scan-station metadata in front matter and
the page layout lives in `theme/lawsafrica/templates/scanstations.html`.

For a normal Markdown page, create a Markdown file in `content/pages/` and use
one of the existing page templates, usually `simple` or `slim`:

```markdown
---
title: Example
slug: example
save_as: example/index.html
url: /example/
template: simple
---

Page content goes here.
```

For a page that is mostly custom HTML, or that needs loops over site data such as
posts, publications, case studies, page front matter, or shared data files,
prefer a dedicated template:

1. Create a small page file in `content/pages/` for routing and metadata.
2. Set `template:` to the matching template name.
3. Put the custom HTML and Jinja logic in `theme/lawsafrica/templates/`.

For example:

```markdown
---
title: Resources
navbar_item: resources
slug: resources
save_as: resources/index.html
url: /resources/
template: resources
---
```

Then create `theme/lawsafrica/templates/resources.html`:

```jinja2
{% set page = article if article is defined else page %}
{% extends "simple.html" %}
{% block content %}
<article>
  <h1>{{ page.title }}</h1>

  {% for publication in site.publications %}
    <a href="{{ publication.url }}">{{ publication.title }}</a>
  {% endfor %}
</article>
{% endblock %}
```

This keeps the content file readable, lets Pelican rebuild dynamic listings from
current data, and avoids checking generated HTML snapshots into source files.

For pages that are full custom HTML, keep the page file as metadata only and put
the full HTML body in the page-specific template. That template can then include
partials directly:

```jinja2
{% set case_study_key = "kenyalaw" %}
{% include "_case_study_by_key.html" %}
```

`_case_study_by_key.html` looks up the case study in `site.case_studies` and then
includes `_case_study_mini_card.html`. The key is the case-study output filename
without `.html`, such as `aga`, `c4ads`, `kenyalaw`, or `spoton`.

Pelican does not evaluate Jinja inside Markdown page content by default. If a
card must appear in the middle of a full-HTML page, put that page body in the
template, set the page's `template:` front matter to that template, and do the
include from the template.

## Template site data

Templates can use a custom `site` object. This is built by
`tools/pelican_support.py` and exposed to Jinja from `pelicanconf.py` as
`JINJA_GLOBALS = {"site": SITE}`. This is project-specific compatibility data,
not native Pelican data.

Available values:

- `site.title`: the site title, currently `Laws.Africa`.
- `site.name`: the site name, currently `Laws.Africa`.
- `site.description`: the default site description used in metadata.
- `site.url`: the canonical production URL, currently `https://laws.africa`.
- `site.timezone`: the site timezone, currently `Africa/Johannesburg`.
- `site.hiring`: boolean used by templates that show hiring notices.
- `site.hiring_contributors`: boolean used by templates that show contributor
  hiring notices.
- `articles`: Pelican's native list of Markdown posts from `content/articles/`,
  sorted newest first. Use this directly in templates for blog listings, recent
  posts, and feeds.
- `site.publications`: all pages whose `save_as` starts with `publications/`,
  sorted newest first.
- `site.case_studies`: all pages whose `save_as` starts with `case-studies/`,
  sorted newest first.
- `site.help`: all pages whose `save_as` starts with `help/`, sorted by
  `position`.
- `site.people`: entries from `data/people.yml`, sorted by `position`.
- `site.data`: shared data loaded from files in `data/`. JSON and YAML files
  are exposed by filename, so `data/commons.json` is available as
  `site.data.commons`.

Items in `articles`, `site.publications`, `site.case_studies`, and `site.help`
are built from each file's front matter. Common fields include
`title`, `url`, `save_as`, `date`, `lead`, `image`, `author`, and `content`,
depending on what the source file defines.

# Local development

To make code or style changes, you'll need to edit the site locally.

1. Clone the repo
2. Create or activate the Python virtualenv: `source .venv/bin/activate`
3. Install dependencies: `python -m pip install -e .`
4. Build the site: `build-pelican-site`
5. Preview the output: `python -m http.server 8000 --directory .pelican-output`
6. Visit [http://localhost:8000](http://localhost:8000)

The source content lives in `content/`, the Pelican theme lives in
`theme/lawsafrica/`, and build output is written to `.pelican-output/`.

# Updating stats on the legislation commons

Every night, GitHub Actions runs and updates `data/commons.json` with stats from Laws.Africa and commits it back into the master branch, which updates the website.
