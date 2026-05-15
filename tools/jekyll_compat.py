from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml
from dateutil import parser as date_parser
from jinja2 import DictLoader, Environment
from markdown import markdown


ROOT = Path(__file__).resolve().parents[1]
BUILD_DIR = ROOT / ".pelican-build"
CONTENT_DIR = BUILD_DIR / "content"
THEME_DIR = BUILD_DIR / "theme"
OUTPUT_DIR = ROOT / ".pelican-output"

COLLECTIONS = {
    "_case-studies": ("case_studies", "case-studies", "case-study"),
    "_help": ("help", "help", "help-article"),
    "_publications": ("publications", "publications", "publication"),
}

TOP_LEVEL_PAGE_EXTENSIONS = {".html", ".md", ".markdown"}
STATIC_DIRS = ["img", "js", "_uploads"]
STATIC_FILES = ["CNAME", "favicon.ico", "africa.geojson", "google31ad17a90935c519.html"]


class Obj(dict):
    """Small mapping object with Liquid-like attribute access."""

    def __getattr__(self, key: str) -> Any:
        try:
            return self[key]
        except KeyError:
            return None

    def __str__(self) -> str:
        return str(self.get("content", ""))


def objify(value: Any) -> Any:
    if isinstance(value, dict):
        return Obj({key: objify(val) for key, val in value.items()})
    if isinstance(value, list):
        return [objify(val) for val in value]
    return value


def parse_front_matter(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text()
    if text.startswith("---\n"):
        _, front_matter, body = text.split("---", 2)
        return yaml.safe_load(front_matter) or {}, body.lstrip("\n")
    return {}, text


def strip_front_matter(text: str) -> tuple[dict[str, Any], str]:
    if text.startswith("---\n"):
        _, front_matter, body = text.split("---", 2)
        return yaml.safe_load(front_matter) or {}, body.lstrip("\n")
    return {}, text


def parse_date(value: Any) -> dt.datetime | None:
    if not value:
        return None
    if isinstance(value, dt.datetime):
        return value
    if isinstance(value, dt.date):
        return dt.datetime.combine(value, dt.time())
    return date_parser.parse(str(value))


def sort_date(value: Any) -> dt.datetime:
    date = parse_date(value)
    if not date:
        return dt.datetime.min
    if date.tzinfo is not None:
        return date.astimezone(dt.timezone.utc).replace(tzinfo=None)
    return date


def dated_slug(path: Path) -> tuple[dt.datetime, str]:
    match = re.match(r"(\d{4})-(\d{2})-(\d{2})-(.+)", path.stem)
    if not match:
        raise ValueError(f"Post filename must start with YYYY-MM-DD: {path}")
    year, month, day, slug = match.groups()
    return dt.datetime(int(year), int(month), int(day)), slug


def save_as_to_url(save_as: str) -> str:
    if save_as == "index.html":
        return "/"
    if save_as.endswith("/index.html"):
        return "/" + save_as[: -len("index.html")]
    return "/" + save_as


def normalise_template(layout: str | None) -> str:
    return (layout or "simple").replace("/", "_")


def collection_item(path: Path, collection: str, public_dir: str, default_layout: str) -> Obj:
    meta, body = parse_front_matter(path)
    rel = path.relative_to(ROOT / collection)
    save_as = str((Path(public_dir) / rel).with_suffix(".html"))
    item_id = "/" + str((Path(public_dir) / rel).with_suffix("")).replace(os.sep, "/")
    meta.setdefault("layout", default_layout)
    meta.setdefault("header_class", "bg-lawsafrica-pale-red")
    if collection == "_help":
        meta.setdefault("navbar_item", "help")
        meta.setdefault("help_section", "api" if rel.parts[0] == "api" else "edit")
    if collection == "_people":
        meta.setdefault("position", 9999)
    if "date" in meta:
        meta["date"] = parse_date(meta["date"])
    return objify(
        {
            **meta,
            "id": item_id,
            "slug": f"{public_dir}-{str(rel.with_suffix('')).replace(os.sep, '-')}",
            "source_path": str(path.relative_to(ROOT)),
            "save_as": save_as,
            "url": save_as_to_url(save_as),
            "content": body,
        }
    )


def post_item(path: Path) -> Obj:
    meta, body = parse_front_matter(path)
    file_date, slug = dated_slug(path)
    date = parse_date(meta.get("date")) or file_date
    save_as = f"{date:%Y/%m/%d}/{slug}.html"
    meta.setdefault("layout", "blog-post")
    meta.setdefault("header_class", "bg-lawsafrica-pale-red")
    if isinstance(meta.get("author"), list):
        meta["author"] = " ".join(str(part) for part in meta["author"])
    return objify(
        {
            **meta,
            "date": date,
            "slug": slug,
            "id": f"/{date:%Y/%m/%d}/{slug}",
            "source_path": str(path.relative_to(ROOT)),
            "save_as": save_as,
            "url": save_as_to_url(save_as),
            "content": body,
        }
    )


def page_item(path: Path) -> Obj:
    meta, body = parse_front_matter(path)
    rel = path.relative_to(ROOT)
    save_as = str(rel.with_suffix(".html"))
    meta.setdefault("layout", "simple")
    meta.setdefault("header_class", "bg-lawsafrica-pale-red")
    meta.setdefault("title", "")
    if "date" in meta:
        meta["date"] = parse_date(meta["date"])
    return objify(
        {
            **meta,
            "id": "/" + str(rel.with_suffix("")).replace(os.sep, "/"),
            "slug": str(rel.with_suffix("")).replace(os.sep, "-"),
            "source_path": str(rel),
            "save_as": save_as,
            "url": save_as_to_url(save_as),
            "content": body,
        }
    )


def load_layout_metadata() -> dict[str, dict[str, Any]]:
    metadata: dict[str, dict[str, Any]] = {}
    for path in (ROOT / "_layouts").rglob("*.html"):
        rel = path.relative_to(ROOT / "_layouts")
        name = str(rel.with_suffix("")).replace(os.sep, "/")
        meta, _ = parse_front_matter(path)
        metadata[name] = meta
    return metadata


def build_site() -> Obj:
    data = {}
    data_dir = ROOT / "_data"
    if data_dir.exists():
        for path in data_dir.glob("*.json"):
            data[path.stem] = json.loads(path.read_text())

    posts = sorted((post_item(path) for path in (ROOT / "_posts").glob("*.*")), key=lambda item: item.date, reverse=True)

    collections: dict[str, list[Obj]] = {}
    for source_dir, (key, public_dir, layout) in COLLECTIONS.items():
        collections[key] = sorted(
            (
                collection_item(path, source_dir, public_dir, layout)
                for path in (ROOT / source_dir).rglob("*")
                if path.suffix in TOP_LEVEL_PAGE_EXTENSIONS
            ),
            key=lambda item: sort_date(item.date),
            reverse=True,
        )

    people = sorted(
        (
            collection_item(path, "_people", "people", "simple")
            for path in (ROOT / "_people").glob("*.*")
            if path.suffix in TOP_LEVEL_PAGE_EXTENSIONS
        ),
        key=lambda item: item.get("position", 9999),
    )

    return objify(
        {
            "title": "Laws.Africa",
            "name": "Laws.Africa",
            "description": "Laws.Africa unlocks the value of African digital legal information in support of the rule of law, access to justice, and innovation.",
            "url": "https://laws.africa",
            "timezone": "Africa/Johannesburg",
            "hiring": True,
            "hiring_contributors": False,
            "data": data,
            "posts": posts,
            "case_studies": collections["case_studies"],
            "help": collections["help"],
            "publications": collections["publications"],
            "people": people,
        }
    )


def liquid_expr(expr: str) -> str:
    expr = expr.replace("site.case-studies", "site.case_studies")
    expr = re.sub(r"\|\s*date\s*:\s*(\"[^\"]+\"|'[^']+')", r"|strftime(\1)", expr)
    expr = re.sub(r"\|\s*sort\s*:\s*(\"[^\"]+\"|'[^']+')", r"|sort(attribute=\1)", expr)
    expr = re.sub(r"\|\s*where\s*:\s*(\"[^\"]+\"|'[^']+')\s*,\s*([^|%]+)", r"|where(\1, \2)", expr)
    expr = re.sub(r"\|\s*xml_escape", "|xml_escape", expr)
    expr = re.sub(r"\|\s*markdownify", "|markdownify", expr)
    return expr


def liquid_to_jinja(text: str) -> str:
    text = text.replace("site.case-studies", "site.case_studies")
    text = re.sub(r"(\w+)\.size", r"\1|length", text)
    text = re.sub(r"\{\{\s*(.*?)\s*\}\}", lambda m: "{{ " + liquid_expr(m.group(1)) + " }}", text, flags=re.S)
    text = re.sub(r"\{%\s*assign\s+(\w+)\s*=\s*(.*?)\s*%\}", lambda m: "{% set " + m.group(1) + " = " + liquid_expr(m.group(2)) + " %}", text)
    text = re.sub(r"\{%\s*include\s+([^\s%]+)(?:\s+[^%]*)?%\}", r'{% include "\1" %}', text)
    text = re.sub(r"\{%\s*for\s+(\w+)\s+in\s+(.+?)\s+reversed\s*%\}", r"{% for \1 in \2|reverse %}", text)
    text = re.sub(r"\{%\s*for\s+(\w+)\s+in\s+(.+?)\s+limit\s*:\s*(\d+)\s*%\}", r"{% for \1 in \2[:\3] %}", text)
    text = re.sub(r"\{%\s*unless\s+forloop\.first\s*%\}", "{% if not loop.first %}", text)
    text = re.sub(r"\{%\s*endunless\s*%\}", "{% endif %}", text)
    return text


def strftime_filter(value: Any, fmt: str) -> str:
    if not value:
        return ""
    date = parse_date(value)
    if not date:
        return ""
    unpadded_day_token = "__JEKYLL_UNPADDED_DAY__"
    fmt = fmt.replace("%e", unpadded_day_token)
    return date.strftime(fmt).replace(unpadded_day_token, str(date.day))


def where_filter(items: list[Any], key: str, expected: Any) -> list[Any]:
    return [item for item in items if getattr(item, key, None) == expected or item.get(key) == expected]


def markdownify_filter(value: Any) -> str:
    return markdown(str(value or ""), extensions=["extra"])


def xml_escape_filter(value: Any) -> str:
    return html.escape(str(value or ""), quote=True)


def reverse_filter(value: Any) -> list[Any]:
    return list(reversed(list(value or [])))


def jinja_env(site: Obj, includes: dict[str, str] | None = None) -> Environment:
    env = Environment(loader=DictLoader(includes or {}), autoescape=False, finalize=finalize_none)
    env.filters.update(
        {
            "strftime": strftime_filter,
            "where": where_filter,
            "markdownify": markdownify_filter,
            "xml_escape": xml_escape_filter,
            "reverse": reverse_filter,
        }
    )
    env.globals["site"] = site
    return env


def finalize_none(value: Any) -> Any:
    return "" if value is None else value


def serialise_meta(value: Any) -> Any:
    if isinstance(value, dt.datetime):
        return value.isoformat()
    if isinstance(value, dt.date):
        return value.isoformat()
    if isinstance(value, Obj):
        return {key: serialise_meta(val) for key, val in value.items()}
    if isinstance(value, dict):
        return {key: serialise_meta(val) for key, val in value.items()}
    if isinstance(value, list):
        return [serialise_meta(val) for val in value]
    return value


def write_content_item(item: Obj, kind: str, env: Environment) -> None:
    page = objify(dict(item))
    rendered = env.from_string(liquid_to_jinja(item.content)).render(site=env.globals["site"], page=page)
    rel_dir = "articles" if kind == "article" else "pages"
    stem = Path(item.save_as).with_suffix("")
    out_path = CONTENT_DIR / rel_dir / stem.with_suffix(".md")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    meta = {key: val for key, val in item.items() if key not in {"content", "source_path", "id", "layout"}}
    meta["template"] = normalise_template(item.layout)
    meta["save_as"] = item.save_as
    meta["url"] = item.url
    if kind == "article":
        meta.setdefault("category", "blog")
    text = "---\n" + yaml.safe_dump(serialise_meta(meta), sort_keys=False, allow_unicode=True) + "---\n\n" + rendered
    out_path.write_text(text)


def load_converted_includes() -> dict[str, str]:
    includes = {}
    for path in (ROOT / "_includes").glob("*.html"):
        includes[path.name] = liquid_to_jinja(path.read_text())
    return includes


def write_theme_template(name: str, body: str, parent: str | None, block_name: str, content_block: str | None = None) -> None:
    out_path = THEME_DIR / "templates" / f"{normalise_template(name)}.html"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    body = liquid_to_jinja(body)
    if content_block:
        body = re.sub(r"\{\{\s*content\s*\}\}", content_block, body)
    else:
        body = re.sub(r"\{\{\s*content\s*\}\}", "{{ page.content }}", body)
    prefix = "{% set page = article if article is defined else page %}\n"
    if parent:
        prefix += f'{{% extends "{normalise_template(parent)}.html" %}}\n{{% block {block_name} %}}\n'
        suffix = f"\n{{% endblock %}}\n"
    else:
        suffix = ""
    out_path.write_text(prefix + body + suffix)


def build_theme() -> None:
    templates_dir = THEME_DIR / "templates"
    templates_dir.mkdir(parents=True, exist_ok=True)
    for path in (ROOT / "_includes").glob("*.html"):
        (templates_dir / path.name).write_text(liquid_to_jinja(path.read_text()))

    layout_bodies: dict[str, tuple[dict[str, Any], str]] = {}
    for path in (ROOT / "_layouts").rglob("*.html"):
        rel = path.relative_to(ROOT / "_layouts")
        name = str(rel.with_suffix("")).replace(os.sep, "/")
        layout_bodies[name] = strip_front_matter(path.read_text())

    base_meta, base_body = layout_bodies["base"]
    del base_meta
    write_theme_template("base", base_body, None, "base_content", "{% block base_content %}{% endblock %}")

    _, simple_body = layout_bodies["simple"]
    write_theme_template("simple", simple_body, "base", "base_content", "{% block content %}{{ page.content }}{% endblock %}")

    _, slim_body = layout_bodies["slim"]
    write_theme_template("slim", slim_body, "simple", "content", "{% block slim_content %}{{ page.content }}{% endblock %}")

    for name, (meta, body) in layout_bodies.items():
        if name in {"base", "simple", "slim"}:
            continue
        parent = meta.get("layout", "simple")
        if parent == "slim":
            write_theme_template(name, body, "slim", "slim_content")
        else:
            write_theme_template(name, body, parent, "content")

    feed = liquid_to_jinja((ROOT / "feed.xml").read_text())
    _, feed_body = strip_front_matter(feed)
    (templates_dir / "feed.xml").write_text(feed_body)


def build_content() -> None:
    site = build_site()
    includes = load_converted_includes()
    env = jinja_env(site, includes)
    layout_meta = load_layout_metadata()

    for post in site.posts:
        write_content_item(post, "article", env)

    for key in ("case_studies", "help", "publications"):
        for item in site[key]:
            merged = Obj(dict(layout_meta.get(item.layout, {})) | dict(item))
            write_content_item(merged, "page", env)

    top_pages = [
        path
        for path in ROOT.iterdir()
        if path.is_file()
        and path.suffix in TOP_LEVEL_PAGE_EXTENSIONS
        and path.name not in {"README.md", "feed.xml", *STATIC_FILES}
    ]
    for folder in ("api", "services", "indigo"):
        top_pages.extend(path for path in (ROOT / folder).rglob("*") if path.suffix in TOP_LEVEL_PAGE_EXTENSIONS)

    for path in sorted(top_pages):
        item = page_item(path)
        merged = Obj(dict(layout_meta.get(item.layout, {})) | dict(item))
        write_content_item(merged, "page", env)


def run_pelican(settings: str) -> None:
    command = [sys.executable, "-m", "pelican", str(CONTENT_DIR), "-s", settings]
    subprocess.run(command, cwd=ROOT, check=True)


def copy_static() -> None:
    for directory in STATIC_DIRS:
        source = ROOT / directory
        if not source.exists():
            continue
        dest_name = "uploads" if directory == "_uploads" else directory
        dest = OUTPUT_DIR / dest_name
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(source, dest, ignore=shutil.ignore_patterns(".DS_Store"))
    for filename in STATIC_FILES:
        source = ROOT / filename
        if source.exists():
            shutil.copy2(source, OUTPUT_DIR / filename)


def compile_sass() -> None:
    css_dir = OUTPUT_DIR / "css"
    css_dir.mkdir(parents=True, exist_ok=True)
    temp_scss = BUILD_DIR / "main.scss"
    _, scss = strip_front_matter((ROOT / "css" / "main.scss").read_text())
    temp_scss.write_text(scss)
    output = css_dir / "main.css"

    commands = [
        ["sassquatch", "--load-path", str(ROOT / "_sass"), f"{temp_scss}:{output}"],
        ["sass", "--load-path", str(ROOT / "_sass"), str(temp_scss), str(output)],
    ]
    for command in commands:
        if shutil.which(command[0]):
            subprocess.run(command, cwd=ROOT, check=True)
            return

    fallback = ROOT / "_site" / "css" / "main.css"
    if fallback.exists():
        shutil.copy2(fallback, output)
        print("WARNING: Sass compiler not found; copied existing _site/css/main.css", file=sys.stderr)
        return
    raise RuntimeError("No Sass compiler found. Install sassquatch or Dart Sass.")


def write_clean_url_aliases() -> None:
    """Write /path/index.html aliases for page files published as /path.html."""
    for source in OUTPUT_DIR.glob("*.html"):
        if source.name in {"index.html", "404.html"}:
            continue
        alias_dir = OUTPUT_DIR / source.stem
        alias_dir.mkdir(exist_ok=True)
        shutil.copy2(source, alias_dir / "index.html")

    for source in (OUTPUT_DIR / "api").glob("*.html"):
        if source.name == "index.html":
            continue
        alias_dir = source.parent / source.stem
        alias_dir.mkdir(exist_ok=True)
        shutil.copy2(source, alias_dir / "index.html")

    for source in (OUTPUT_DIR / "help").rglob("*.html"):
        if source.name == "index.html":
            continue
        alias_dir = source.parent / source.stem
        alias_dir.mkdir(exist_ok=True)
        shutil.copy2(source, alias_dir / "index.html")


def clean_build_dirs() -> None:
    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)
    BUILD_DIR.mkdir(parents=True)


def generate(settings: str) -> None:
    clean_build_dirs()
    build_theme()
    build_content()
    run_pelican(settings)
    copy_static()
    compile_sass()
    write_clean_url_aliases()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--settings", default="pelicanconf.py")
    args = parser.parse_args()
    generate(args.settings)


if __name__ == "__main__":
    main()
