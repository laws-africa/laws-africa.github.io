# laws.africa website

This is a GitHub Pages website for [laws.africa](https://laws.africa).

# Changing content

Pages live under `content/pages/`, blog posts under `content/articles/`, shared
data under `data/`, and templates under `theme/lawsafrica/templates/`.

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
