from __future__ import annotations

import argparse
import datetime as dt
import json
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml
from dateutil import parser as date_parser
from markdown import markdown


ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIR = ROOT / "content"
OUTPUT_DIR = ROOT / ".pelican-output"
THEME_DIR = ROOT / "theme" / "lawsafrica"

STATIC_DIRS = ["img", "js", "_uploads"]
STATIC_FILES = ["CNAME", "favicon.ico", "africa.geojson", "google31ad17a90935c519.html"]


class Obj(dict):
    """Mapping object with attribute access for template data."""

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


def content_item(path: Path) -> Obj:
    meta, body = parse_front_matter(path)
    if "date" in meta:
        meta["date"] = parse_date(meta["date"])
    meta["content"] = body
    return objify(meta)


def load_data() -> Obj:
    data: dict[str, Any] = {}
    data_dir = ROOT / "data"
    for path in data_dir.glob("*.json"):
        data[path.stem] = json.loads(path.read_text())
    for path in data_dir.glob("*.yml"):
        data[path.stem] = yaml.safe_load(path.read_text()) or []
    return objify(data)


def build_site() -> Obj:
    data = load_data()
    posts = sorted(
        (content_item(path) for path in (CONTENT_DIR / "articles").rglob("*.md")),
        key=lambda item: sort_date(item.date),
        reverse=True,
    )
    pages = [content_item(path) for path in (CONTENT_DIR / "pages").rglob("*.md")]
    publications = sorted(
        (page for page in pages if str(page.save_as or "").startswith("publications/")),
        key=lambda item: sort_date(item.date),
        reverse=True,
    )
    case_studies = sorted(
        (page for page in pages if str(page.save_as or "").startswith("case-studies/")),
        key=lambda item: sort_date(item.date),
        reverse=True,
    )
    help_pages = sorted(
        (page for page in pages if str(page.save_as or "").startswith("help/")),
        key=lambda item: item.get("position", 9999),
    )
    people = sorted(data.people or [], key=lambda item: item.get("position", 9999))

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
            "publications": publications,
            "case_studies": case_studies,
            "help": help_pages,
            "people": people,
        }
    )


def strftime_filter(value: Any, fmt: str) -> str:
    if not value:
        return ""
    date = parse_date(value)
    if not date:
        return ""
    unpadded_day_token = "__JEKYLL_UNPADDED_DAY__"
    fmt = fmt.replace("%e", unpadded_day_token)
    return date.strftime(fmt).replace(unpadded_day_token, str(date.day))


def markdownify_filter(value: Any) -> str:
    return markdown(str(value or ""), extensions=["extra"])


def finalize_none(value: Any) -> Any:
    return "" if value is None else value


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
    temp_scss = ROOT / ".pelican-main.scss"
    scss = (ROOT / "css" / "main.scss").read_text()
    if scss.startswith("---\n"):
        _, _, scss = scss.split("---", 2)
        scss = scss.lstrip("\n")
    temp_scss.write_text(scss)
    output = css_dir / "main.css"

    try:
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
    finally:
        temp_scss.unlink(missing_ok=True)


def run_pelican(settings: str) -> None:
    command = [sys.executable, "-m", "pelican", str(CONTENT_DIR), "-s", settings]
    subprocess.run(command, cwd=ROOT, check=True)


def build(settings: str) -> None:
    run_pelican(settings)
    copy_static()
    compile_sass()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--settings", default="pelicanconf.py")
    args = parser.parse_args()
    build(args.settings)


if __name__ == "__main__":
    main()
