# laws.africa website

This is a GitHub Pages website for [laws.africa](https://laws.africa).

# Changing content

It's easiest to make content changes through [Siteleaf](https://manage.siteleaf.com/sites/5c138a462dde9749d7d61d1c/pages). You can also click the `edit` link at the bottom right corner of a page.

Be sure to read the [Siteleaf documentation](https://learn.siteleaf.com/) if you're not sure how to use the Siteleaf editor.

You will need to be added to the website in Siteleaf, ask someone on the team.

# Local development

To make code or style changes, you'll need to edit the site locally.

1. Clone the repo
2. Create or activate the Python virtualenv: `source .venv/bin/activate`
3. Install dependencies: `python -m pip install -e .`
4. Build the site: `build-pelican-site -s pelicanconf.py`
5. Preview the output: `python -m http.server 8000 --directory .pelican-output`
6. Visit [http://localhost:8000](http://localhost:8000)

During the migration, the existing Jekyll source files are kept in place. The
Pelican build generates `.pelican-build/` from those files, then writes the final
site to `.pelican-output/`.

# Updating stats on the legislation commons

Every night, GitHub Actions runs and updates `_data/commons.json` with stats from Laws.Africa and commits it back into the master branch, which updates the website.
