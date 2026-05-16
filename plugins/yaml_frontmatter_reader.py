from __future__ import annotations

import datetime as dt

import yaml
from markdown import Markdown
from pelican import signals
from pelican.readers import MarkdownReader, Readers


class YAMLFrontMatterMarkdownReader(MarkdownReader):
    file_extensions = ["md", "markdown"]

    def read(self, source_path):
        self._source_path = source_path
        self._md = Markdown(**self.settings["MARKDOWN"])
        with open(source_path, encoding="utf-8") as handle:
            text = handle.read()

        metadata = {}
        if text.startswith("---\n"):
            _, front_matter, text = text.split("---", 2)
            metadata = yaml.safe_load(front_matter) or {}
            text = text.lstrip("\n")

        content = self._md.convert(text)
        return content, self._parse_yaml_metadata(metadata)

    def _parse_yaml_metadata(self, metadata):
        parsed = {}
        for name, value in metadata.items():
            key = name.lower()
            if isinstance(value, dt.datetime):
                value = value.isoformat()
            elif isinstance(value, dt.date):
                value = value.isoformat()

            if key in {"date", "modified", "author", "authors", "tags", "category", "save_as", "url"}:
                parsed[key] = self.process_metadata(key, value)
            else:
                parsed[key] = value
        return parsed


def add_reader(readers):
    readers.reader_classes["md"] = YAMLFrontMatterMarkdownReader
    readers.reader_classes["markdown"] = YAMLFrontMatterMarkdownReader


def register():
    signals.readers_init.connect(add_reader)
