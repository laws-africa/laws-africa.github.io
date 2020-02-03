# laws.africa website

This is a GitHub Pages website for [laws.africa](https://laws.africa).

# Changing content

It's easiest to make content changes through [Siteleaf](https://manage.siteleaf.com/sites/5c138a462dde9749d7d61d1c/pages). You can also click the `edit` link at the bottom right corner of a page.

Be sure to read the [Siteleaf documentation](https://learn.siteleaf.com/) if you're not sure how to use the Siteleaf editor.

You will need to be added to the website in Siteleaf, ask someone on the team.

# Local development

To make code or style changes, you'll need to edit the site locally.

1. Clone the repo
2. You'll need to have a modern Ruby installation
3. Ensure Bundler is installed: `gem install bundler`
4. Install dependencies: `bundle install`
5. Run the webserver: `jekyll server --watch`
6. Visit [http://localhost:4000](http://localhost:4000)

# Updating stats on the legislation commons

Every night, the Travis runs the `build` branch which updates `_data/commons.json` with stats from Laws.Africa.
See [https://github.com/laws-africa/gazettes-africa/tree/build](the build branch README.md) for details.
