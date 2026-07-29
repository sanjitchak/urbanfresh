#!/usr/bin/env python3
"""Local, zero-cost technical SEO checks for the UrbanFresh static site."""

from __future__ import annotations

import csv
import json
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
DOMAIN = "urbanfresh.in"
SITEMAP_NAMESPACE = "http://www.sitemaps.org/schemas/sitemap/0.9"
IMAGE_SITEMAP_NAMESPACE = "http://www.google.com/schemas/sitemap-image/1.1"


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.in_title = False
        self.in_h1 = False
        self.in_jsonld = False
        self.title_parts: list[str] = []
        self.h1_parts: list[str] = []
        self.h1_count = 0
        self.description = ""
        self.canonical = ""
        self.robots = ""
        self.links: list[str] = []
        self.hreflangs: dict[str, str] = {}
        self.images_missing_alt: list[str] = []
        self.jsonld_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "title":
            self.in_title = True
        elif tag == "h1":
            self.in_h1 = True
            self.h1_count += 1
        elif tag == "meta":
            name = values.get("name", "").lower()
            if name == "description":
                self.description = values.get("content", "") or ""
            elif name == "robots":
                self.robots = values.get("content", "") or ""
        elif tag == "link" and "canonical" in (values.get("rel", "") or "").lower():
            self.canonical = values.get("href", "") or ""
        elif tag == "link" and "alternate" in (values.get("rel", "") or "").lower() and values.get("hreflang"):
            self.hreflangs[values["hreflang"] or ""] = values.get("href", "") or ""
        elif tag == "a" and values.get("href"):
            self.links.append(values["href"] or "")
        elif tag == "img" and "alt" not in values:
            self.images_missing_alt.append(values.get("src", "unknown image") or "unknown image")
        elif tag == "script" and values.get("type", "").lower() == "application/ld+json":
            self.in_jsonld = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False
        elif tag == "h1":
            self.in_h1 = False
        elif tag == "script" and self.in_jsonld:
            self.in_jsonld = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)
        if self.in_h1:
            self.h1_parts.append(data)
        if self.in_jsonld:
            self.jsonld_parts.append(data)


def clean(parts: list[str]) -> str:
    return re.sub(r"\s+", " ", "".join(parts)).strip()


def internal_target(source: Path, href: str) -> Path | None:
    if not href or href.startswith(("#", "mailto:", "tel:", "javascript:")):
        return None
    parsed = urlsplit(href)
    if parsed.scheme or parsed.netloc:
        return None
    path = parsed.path
    if not path:
        return None
    target = (source.parent / path).resolve()
    if target.is_dir():
        target /= "index.html"
    return target


def json_objects(value: object):
    if isinstance(value, dict):
        yield value
        for nested in value.values():
            yield from json_objects(nested)
    elif isinstance(value, list):
        for nested in value:
            yield from json_objects(nested)


def unsupported_product_snippets(data: object) -> list[str]:
    unsupported: list[str] = []
    for node in json_objects(data):
        node_type = node.get("@type")
        types = node_type if isinstance(node_type, list) else [node_type]
        if "Product" not in types:
            continue
        if any(node.get(required) for required in ("offers", "review", "aggregateRating")):
            continue
        unsupported.append(str(node.get("name", "unnamed Product")))
    return unsupported


def datasets_missing_license(data: object) -> list[str]:
    missing: list[str] = []
    for node in json_objects(data):
        node_type = node.get("@type")
        types = node_type if isinstance(node_type, list) else [node_type]
        if "Dataset" not in types:
            continue
        if node.get("license"):
            continue
        missing.append(str(node.get("name", "unnamed Dataset")))
    return missing


def sitemap_page_name(url: str) -> str | None:
    parsed = urlsplit(url)
    if parsed.scheme != "https" or parsed.netloc.casefold() != DOMAIN or parsed.query or parsed.fragment:
        return None
    relative = parsed.path.lstrip("/")
    return relative or "index.html"


def orphan_pages(
    indexable_pages: set[str],
    outgoing_by_page: dict[str, set[str]],
) -> list[str]:
    incoming: dict[str, set[str]] = {page: set() for page in indexable_pages}
    for source, targets in outgoing_by_page.items():
        if source not in indexable_pages:
            continue
        for target in targets:
            if target in indexable_pages and target != source:
                incoming[target].add(source)
    return sorted(
        page
        for page, sources in incoming.items()
        if page != "index.html" and not sources
    )


def keyword_map_issues(sitemap_pages: set[str], path: Path) -> list[str]:
    issues: list[str] = []
    if not path.exists():
        return ["keyword map missing"]

    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        required = {"page", "primary_search_intent", "buyer_stage", "conversion_action"}
        if not reader.fieldnames or not required.issubset(reader.fieldnames):
            return ["keyword map is missing required columns"]
        rows = list(reader)

    mapped_pages: set[str] = set()
    intent_owners: dict[str, str] = {}
    for row in rows:
        page = str(row.get("page", "")).strip()
        intent = str(row.get("primary_search_intent", "")).strip()
        if not page:
            issues.append("keyword map contains a row without a page")
            continue
        if page in mapped_pages:
            issues.append(f"keyword map contains duplicate page {page}")
        mapped_pages.add(page)
        if not intent:
            issues.append(f"keyword map has no primary intent for {page}")
        if not str(row.get("buyer_stage", "")).strip():
            issues.append(f"keyword map has no buyer stage for {page}")
        if not str(row.get("conversion_action", "")).strip():
            issues.append(f"keyword map has no conversion action for {page}")
        for phrase in re.split(r"\s*/\s*", intent):
            key = phrase.casefold().strip()
            if not key:
                continue
            owner = intent_owners.get(key)
            if owner and owner != page:
                issues.append(
                    f'keyword intent "{phrase}" is assigned to both {owner} and {page}'
                )
            else:
                intent_owners[key] = page

    for page in sorted(sitemap_pages - mapped_pages):
        issues.append(f"keyword map is missing sitemap page {page}")
    for page in sorted(mapped_pages - sitemap_pages):
        issues.append(f"keyword map page is absent from sitemap: {page}")
    return issues


def audit() -> int:
    pages = sorted(ROOT.glob("*.html"))
    errors: list[str] = []
    warnings: list[str] = []
    canonicals: dict[str, str] = {}
    canonical_by_page: dict[str, str] = {}
    indexable_pages: set[str] = set()
    outgoing_by_page: dict[str, set[str]] = {}
    page_hreflangs: dict[str, dict[str, str]] = {}

    for page in pages:
        parser = PageParser()
        parser.feed(page.read_text(encoding="utf-8"))
        title = clean(parser.title_parts)
        h1 = clean(parser.h1_parts)
        label = page.name

        if not title:
            errors.append(f"{label}: missing title")
        elif not 30 <= len(title) <= 65:
            warnings.append(f"{label}: title length {len(title)} (aim 30-65)")
        if not parser.description:
            errors.append(f"{label}: missing meta description")
        elif not 110 <= len(parser.description) <= 170:
            warnings.append(f"{label}: description length {len(parser.description)} (aim 110-170)")
        if parser.h1_count != 1:
            errors.append(f"{label}: expected one H1, found {parser.h1_count}")
        if not h1:
            errors.append(f"{label}: H1 is empty")
        if not parser.canonical:
            errors.append(f"{label}: missing canonical")
        elif parser.canonical in canonicals:
            errors.append(f"{label}: duplicate canonical also used by {canonicals[parser.canonical]}")
        else:
            canonicals[parser.canonical] = label
            canonical_by_page[label] = parser.canonical
            page_hreflangs[parser.canonical] = parser.hreflangs
        robots_tokens = {
            token.strip().casefold()
            for token in parser.robots.split(",")
            if token.strip()
        }
        if "noindex" not in robots_tokens:
            indexable_pages.add(label)
        if parser.images_missing_alt:
            errors.append(f"{label}: image(s) missing alt: {', '.join(parser.images_missing_alt)}")
        if not clean(parser.jsonld_parts):
            warnings.append(f"{label}: no JSON-LD structured data")
        else:
            try:
                structured_data = json.loads(clean(parser.jsonld_parts))
                unsupported = unsupported_product_snippets(structured_data)
                if unsupported:
                    errors.append(
                        f"{label}: Product markup lacks offers, review or aggregateRating: "
                        f"{', '.join(unsupported)}"
                    )
                unlicensed_datasets = datasets_missing_license(structured_data)
                if unlicensed_datasets:
                    errors.append(
                        f"{label}: Dataset markup lacks license: "
                        f"{', '.join(unlicensed_datasets)}"
                    )
            except json.JSONDecodeError as exc:
                errors.append(f"{label}: invalid JSON-LD ({exc.msg})")

        outgoing_targets: set[str] = set()
        for href in parser.links:
            target = internal_target(page, href)
            if target and ROOT in target.parents and not target.exists():
                errors.append(f"{label}: broken internal link {href}")
            elif target and ROOT in target.parents and target.suffix == ".html":
                outgoing_targets.add(target.name)
        outgoing_by_page[label] = outgoing_targets

    sitemap = ROOT / "sitemap.xml"
    robots = ROOT / "robots.txt"
    sitemap_pages: set[str] = set()
    if not sitemap.exists():
        errors.append("site: sitemap.xml missing")
    else:
        try:
            sitemap_root = ET.fromstring(sitemap.read_text(encoding="utf-8"))
        except ET.ParseError as exc:
            errors.append(f"site: sitemap.xml is invalid XML ({exc})")
        else:
            namespace = {"sm": SITEMAP_NAMESPACE, "image": IMAGE_SITEMAP_NAMESPACE}
            for entry in sitemap_root.findall("sm:url", namespace):
                location = entry.findtext("sm:loc", default="", namespaces=namespace).strip()
                page_name = sitemap_page_name(location)
                if not page_name:
                    errors.append(f"site: sitemap has invalid page URL {location or '(missing loc)'}")
                    continue
                if page_name in sitemap_pages:
                    errors.append(f"site: sitemap contains duplicate page {page_name}")
                    continue
                sitemap_pages.add(page_name)
                page_path = ROOT / page_name
                if not page_path.exists():
                    errors.append(f"site: sitemap page does not exist: {page_name}")
                elif canonical_by_page.get(page_name) != location:
                    errors.append(
                        f"{page_name}: sitemap URL does not match canonical "
                        f"{canonical_by_page.get(page_name, '(missing)')}"
                    )

                image_nodes = entry.findall("image:image", namespace)
                if not image_nodes:
                    errors.append(f"{page_name}: sitemap has no image entry")
                for image_node in image_nodes:
                    image_location = image_node.findtext(
                        "image:loc", default="", namespaces=namespace
                    ).strip()
                    parsed_image = urlsplit(image_location)
                    if (
                        parsed_image.scheme != "https"
                        or parsed_image.netloc.casefold() != DOMAIN
                        or not parsed_image.path
                    ):
                        errors.append(
                            f"{page_name}: sitemap has invalid image URL "
                            f"{image_location or '(missing image:loc)'}"
                        )
                        continue
                    image_path = ROOT / parsed_image.path.lstrip("/")
                    if not image_path.exists():
                        errors.append(
                            f"{page_name}: sitemap image does not exist: {image_location}"
                        )

            for page_name in sorted(indexable_pages - sitemap_pages):
                errors.append(f"site: indexable page missing from sitemap: {page_name}")
            for page_name in sorted(sitemap_pages - indexable_pages):
                errors.append(f"site: sitemap includes missing or noindex page: {page_name}")

            for page_name in orphan_pages(indexable_pages, outgoing_by_page):
                errors.append(f"{page_name}: indexable page has no inbound internal link")

            for issue in keyword_map_issues(
                sitemap_pages,
                ROOT / "seo" / "keyword-map.csv",
            ):
                errors.append(f"site: {issue}")
    if not robots.exists():
        errors.append("site: robots.txt missing")

    hreflang_map = ROOT / "seo" / "hreflang-map.json"
    if hreflang_map.exists():
        try:
            pairs = json.loads(hreflang_map.read_text(encoding="utf-8")).get("pairs", [])
        except (json.JSONDecodeError, AttributeError):
            errors.append("site: invalid seo/hreflang-map.json")
            pairs = []
        for pair in pairs:
            if not isinstance(pair, dict) or set(pair) != {"en-IN", "en"}:
                errors.append("site: each hreflang pair must contain en-IN and en")
                continue
            local_urls = [url for url in pair.values() if urlsplit(url).netloc == DOMAIN]
            if len(local_urls) != 1:
                errors.append(f"site: hreflang pair must contain exactly one {DOMAIN} URL")
                continue
            local_url = local_urls[0]
            actual = page_hreflangs.get(local_url)
            if actual is None:
                errors.append(f"site: hreflang local page missing from generated canonicals: {local_url}")
            elif actual != pair:
                errors.append(f"{canonicals[local_url]}: hreflang declarations do not match reciprocal map")

    print(f"UrbanFresh SEO audit: {len(pages)} HTML pages")
    if errors:
        print("\nERRORS")
        for item in errors:
            print(f"- {item}")
    if warnings:
        print("\nWARNINGS")
        for item in warnings:
            print(f"- {item}")
    if not errors and not warnings:
        print("PASS: all local checks passed")
    elif not errors:
        print("\nPASS with advisory warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(audit())
