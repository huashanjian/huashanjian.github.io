import importlib.util
import json
import tempfile
import unittest
from datetime import datetime
from pathlib import Path

from bs4 import BeautifulSoup


MODULE_PATH = Path(__file__).resolve().parents[1] / "main.py"
SPEC = importlib.util.spec_from_file_location("google_scholar_crawler_main", MODULE_PATH)
crawler = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(crawler)


SAMPLE_PROFILE_HTML = """
<html>
  <head><title>Google Scholar</title></head>
  <body>
    <div id="gsc_prf_in">Junhua Yao</div>
    <div class="gsc_prf_il">TEA Lab, Tsinghua University</div>
    <div id="gsc_prf_int">
      <a>Embodied AI</a>
      <a>Robotics</a>
    </div>
    <table id="gsc_rsb_st">
      <tr><td>Citations</td><td>42</td></tr>
      <tr><td>h-index</td><td>3</td></tr>
      <tr><td>i10-index</td><td>1</td></tr>
    </table>
    <table>
      <tr class="gsc_a_tr">
        <td>
          <a class="gsc_a_at" href="/citations?view_op=view_citation&hl=en&user=UwMitgEAAAAJ&citation_for_view=UwMitgEAAAAJ:paper-1">
            World Models for Curious Agents
          </a>
          <div class="gs_gray">Junhua Yao, Collaborator A</div>
          <div class="gs_gray">Conference on Embodied Intelligence</div>
        </td>
        <td class="gsc_a_c">
          <a class="gsc_a_ac">7</a>
        </td>
        <td class="gsc_a_y">2025</td>
      </tr>
    </table>
  </body>
</html>
"""


class GoogleScholarCrawlerTests(unittest.TestCase):
    def test_build_author_payload_parses_profile_basics_and_publications(self) -> None:
        soup = BeautifulSoup(SAMPLE_PROFILE_HTML, "html.parser")

        author = crawler.build_author_payload(
            scholar_id="UwMitgEAAAAJ",
            soup=soup,
            resolved_url="https://scholar.google.com/citations?hl=en&user=UwMitgEAAAAJ",
            fetched_at=datetime(2026, 3, 30, 10, 15, 0),
        )

        self.assertEqual(author["name"], "Junhua Yao")
        self.assertEqual(author["affiliation"], "TEA Lab, Tsinghua University")
        self.assertEqual(author["interests"], ["Embodied AI", "Robotics"])
        self.assertEqual(author["citedby"], 42)
        self.assertEqual(author["hindex"], 3)
        self.assertEqual(author["i10index"], 1)
        self.assertEqual(
            author["publications"]["UwMitgEAAAAJ:paper-1"]["bib"]["title"],
            "World Models for Curious Agents",
        )
        self.assertEqual(
            author["publications"]["UwMitgEAAAAJ:paper-1"]["num_citations"],
            7,
        )
        self.assertEqual(author["updated"], "2026-03-30T10:15:00")

    def test_run_uses_cached_results_when_fetch_fails(self) -> None:
        cached_author = {
            "scholar_id": "UwMitgEAAAAJ",
            "name": "Junhua Yao",
            "updated": "2026-03-26T21:03:23",
            "profile_url": "https://scholar.google.com/citations?hl=en&user=UwMitgEAAAAJ",
            "affiliation": "TEA Lab, Tsinghua University",
            "interests": ["Embodied AI"],
            "publications": {},
            "citedby": 12,
            "hindex": 2,
            "i10index": 1,
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            results_dir = Path(temp_dir)
            crawler.write_results(results_dir, cached_author)

            def failing_fetcher(_: str) -> tuple[BeautifulSoup, str]:
                raise RuntimeError("blocked")

            mode = crawler.run(
                raw_scholar_id="UwMitgEAAAAJ",
                results_dir=results_dir,
                fetcher=failing_fetcher,
            )

            self.assertEqual(mode, "cache")
            persisted_author = json.loads((results_dir / "gs_data.json").read_text(encoding="utf-8"))
            self.assertEqual(persisted_author, cached_author)


if __name__ == "__main__":
    unittest.main()
