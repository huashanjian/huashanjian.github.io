import json
from datetime import datetime
import os
from pathlib import Path
import re
import sys
import time
from typing import Callable
from urllib.parse import parse_qs, urlparse

import requests
from bs4 import BeautifulSoup

AUTHOR_URL = "https://scholar.google.com/citations?hl=en&user={scholar_id}"
BASE_DIR = Path(__file__).resolve().parent
REQUEST_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}


def resolve_scholar_id(raw_value: str) -> str:
    value = raw_value.strip()
    if not value:
        raise ValueError("GOOGLE_SCHOLAR_ID is empty.")

    if value.startswith("http://") or value.startswith("https://"):
        parsed = urlparse(value)
        value = parse_qs(parsed.query).get("user", [""])[0].strip()

    if not re.fullmatch(r"[A-Za-z0-9_-]+", value):
        raise ValueError(
            "GOOGLE_SCHOLAR_ID must be a Google Scholar user ID or a full citations URL."
        )

    return value


def looks_blocked(html: str) -> bool:
    lowered = html.lower()
    return any(
        needle in lowered
        for needle in (
            "unusual traffic",
            "not a robot",
            "captcha",
            "/sorry/",
            "detected unusual traffic",
        )
    )


def fetch_profile_page(scholar_id: str) -> tuple[BeautifulSoup, str]:
    session = requests.Session()
    session.headers.update(REQUEST_HEADERS)
    url = AUTHOR_URL.format(scholar_id=scholar_id)
    last_error: Exception | None = None

    for attempt in range(3):
        try:
            response = session.get(url, timeout=30)
            response.raise_for_status()
        except requests.RequestException as exc:
            last_error = exc
        else:
            soup = BeautifulSoup(response.text, "html.parser")
            if soup.find("div", id="gsc_prf_in"):
                return soup, response.url

            title = soup.title.get_text(" ", strip=True) if soup.title else "unknown"
            snippet = " ".join(soup.get_text(" ", strip=True).split())[:200]
            if looks_blocked(response.text):
                last_error = RuntimeError(
                    "Google Scholar blocked the request or returned a verification page. "
                    f"Page title: {title!r}. Snippet: {snippet!r}"
                )
            else:
                last_error = RuntimeError(
                    "Google Scholar returned a page that does not look like an author profile. "
                    f"Page title: {title!r}. Snippet: {snippet!r}"
                )

        if attempt < 2:
            time.sleep(attempt + 1)

    raise RuntimeError(f"Unable to fetch Google Scholar profile {scholar_id!r}") from last_error


def parse_int(text: str) -> int:
    digits = re.sub(r"[^\d]", "", text)
    return int(digits) if digits else 0


def parse_publications(soup: BeautifulSoup) -> dict[str, dict]:
    publications: dict[str, dict] = {}

    for row in soup.select("tr.gsc_a_tr"):
        title_link = row.select_one("a.gsc_a_at")
        if not title_link:
            continue

        href = title_link.get("href", "")
        publication_id = parse_qs(urlparse(href).query).get("citation_for_view", [""])[0]
        if not publication_id:
            continue

        citation_cell = row.select_one("a.gsc_a_ac, .gsc_a_ac")
        year_cell = row.select_one(".gsc_a_y")
        authors_text = " ".join(
            item.get_text(" ", strip=True) for item in row.select(".gs_gray")
        )

        publications[publication_id] = {
            "author_pub_id": publication_id,
            "bib": {
                "title": title_link.get_text(" ", strip=True),
                "author": authors_text,
            },
            "num_citations": parse_int(citation_cell.get_text(" ", strip=True) if citation_cell else ""),
            "year": parse_int(year_cell.get_text(" ", strip=True) if year_cell else ""),
        }

    return publications


def parse_counts(soup: BeautifulSoup) -> dict[str, int]:
    counts = {"citedby": 0, "hindex": 0, "i10index": 0}
    stats_table = soup.find("table", id="gsc_rsb_st")
    if not stats_table:
        return counts

    for row in stats_table.select("tr"):
        cells = [cell.get_text(" ", strip=True) for cell in row.select("td")]
        if len(cells) < 2:
            continue

        label = cells[0].lower().replace("-", "")
        value = parse_int(cells[1])
        if label == "citations":
            counts["citedby"] = value
        elif label == "hindex":
            counts["hindex"] = value
        elif label == "i10index":
            counts["i10index"] = value

    return counts


def build_author_payload(
    scholar_id: str,
    soup: BeautifulSoup,
    resolved_url: str,
    fetched_at: datetime | None = None,
) -> dict:
    name_node = soup.find("div", id="gsc_prf_in")
    counts = parse_counts(soup)
    fetched_at = fetched_at or datetime.now()

    return {
        "scholar_id": scholar_id,
        "name": name_node.get_text(" ", strip=True) if name_node else "",
        "updated": fetched_at.isoformat(timespec="seconds"),
        "profile_url": resolved_url,
        "affiliation": (
            soup.find("div", class_="gsc_prf_il").get_text(" ", strip=True)
            if soup.find("div", class_="gsc_prf_il")
            else ""
        ),
        "interests": [
            item.get_text(" ", strip=True) for item in soup.select("#gsc_prf_int a")
        ],
        "publications": parse_publications(soup),
        **counts,
    }


def write_results(results_dir: Path, author: dict) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    with open(results_dir / "gs_data.json", "w", encoding="utf-8") as outfile:
        json.dump(author, outfile, ensure_ascii=False)

    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": f"{author['citedby']}",
    }
    with open(results_dir / "gs_data_shieldsio.json", "w", encoding="utf-8") as outfile:
        json.dump(shieldio_data, outfile, ensure_ascii=False)


def has_cached_results(results_dir: Path) -> bool:
    return (
        (results_dir / "gs_data.json").exists()
        and (results_dir / "gs_data_shieldsio.json").exists()
    )


def load_cached_author(results_dir: Path) -> dict:
    with open(results_dir / "gs_data.json", "r", encoding="utf-8") as infile:
        return json.load(infile)


def run(
    raw_scholar_id: str | None = None,
    results_dir: Path | None = None,
    fetcher: Callable[[str], tuple[BeautifulSoup, str]] = fetch_profile_page,
) -> str:
    scholar_id = resolve_scholar_id(
        raw_scholar_id if raw_scholar_id is not None else os.getenv("GOOGLE_SCHOLAR_ID", "")
    )
    output_dir = Path(results_dir) if results_dir is not None else BASE_DIR / "results"

    try:
        soup, resolved_url = fetcher(scholar_id)
    except Exception as exc:
        if not has_cached_results(output_dir):
            raise

        cached_author = load_cached_author(output_dir)
        print(
            "Using cached Google Scholar stats because fresh fetch failed: "
            f"{exc}",
            file=sys.stderr,
        )
        print(json.dumps(cached_author, indent=2, ensure_ascii=False))
        return "cache"

    author = build_author_payload(
        scholar_id=scholar_id,
        soup=soup,
        resolved_url=resolved_url,
    )
    print(json.dumps(author, indent=2, ensure_ascii=False))
    write_results(output_dir, author)
    return "fresh"


def main() -> int:
    run()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
