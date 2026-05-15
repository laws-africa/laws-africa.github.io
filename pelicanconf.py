from __future__ import annotations

from tools.jekyll_compat import (
    OUTPUT_DIR,
    THEME_DIR,
    build_site,
    finalize_none,
    markdownify_filter,
    reverse_filter,
    strftime_filter,
    where_filter,
    xml_escape_filter,
)


AUTHOR = "Laws.Africa"
SITENAME = "Laws.Africa"
SITEURL = "https://laws.africa"
TIMEZONE = "Africa/Johannesburg"
DEFAULT_LANG = "en"

PATH = ".pelican-build/content"
OUTPUT_PATH = str(OUTPUT_DIR)
THEME = str(THEME_DIR)
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["yaml_frontmatter_reader"]

ARTICLE_PATHS = ["articles"]
PAGE_PATHS = ["pages"]
STATIC_PATHS = []
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = "blog"
WITH_FUTURE_DATES = True
DELETE_OUTPUT_DIRECTORY = True

ARTICLE_URL = "{date:%Y}/{date:%m}/{date:%d}/{slug}.html"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{date:%d}/{slug}.html"
PAGE_URL = "{slug}.html"
PAGE_SAVE_AS = "{slug}.html"

DIRECT_TEMPLATES = []
TEMPLATE_PAGES = {"feed.xml": "feed.xml"}

FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TAG_SAVE_AS = ""
TAGS_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
ARCHIVES_SAVE_AS = ""

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {
            "permalink": False,
            "separator": "-",
        },
    },
    "output_format": "html5",
}

SITE = build_site()
JINJA_GLOBALS = {"site": SITE}
JINJA_ENVIRONMENT = {"trim_blocks": True, "lstrip_blocks": True, "finalize": finalize_none}
JINJA_FILTERS = {
    "strftime": strftime_filter,
    "where": where_filter,
    "markdownify": markdownify_filter,
    "xml_escape": xml_escape_filter,
    "reverse": reverse_filter,
}
