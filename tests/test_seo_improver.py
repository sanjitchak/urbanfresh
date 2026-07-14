from __future__ import annotations

import csv
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import seo_improver  # noqa: E402


class SeoImproverTests(unittest.TestCase):
    def test_csv_loader_accepts_search_console_headers_and_percent_ctr(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "gsc.csv"
            with path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.writer(handle)
                writer.writerow(["Top queries", "Clicks", "Impressions", "CTR", "Position"])
                writer.writerow(["1121 basmati rice supplier", "4", "120", "3.33%", "9.4"])

            rows = seo_improver.load_search_console_csv(path)

        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0].query, "1121 basmati rice supplier")
        self.assertEqual(rows[0].clicks, 4)
        self.assertAlmostEqual(rows[0].ctr, 0.0333)
        self.assertEqual(rows[0].position, 9.4)

    def test_aggregate_metrics_weights_position_by_impressions(self) -> None:
        rows = [
            seo_improver.Metric("rice mill", "https://urbanfresh.in/", 1, 10, 0.1, 5),
            seo_improver.Metric("rice mill", "https://urbanfresh.in/", 3, 30, 0.1, 9),
        ]

        result = seo_improver.aggregate_metrics(rows)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].clicks, 4)
        self.assertEqual(result[0].impressions, 40)
        self.assertEqual(result[0].position, 8)

    def test_detects_striking_distance_low_ctr_and_decay(self) -> None:
        current = [
            seo_improver.Metric(
                "1121 basmati rice supplier",
                "https://urbanfresh.in/1121-basmati-rice.html",
                1,
                100,
                0.01,
                10,
            )
        ]
        previous = [
            seo_improver.Metric(
                "1121 basmati rice supplier",
                "https://urbanfresh.in/1121-basmati-rice.html",
                5,
                100,
                0.05,
                7,
            )
        ]

        opportunities = seo_improver.detect_opportunities(current, previous, "urbanfresh.in")
        kinds = {item.kind for item in opportunities}

        self.assertIn("STRIKE", kinds)
        self.assertIn("CTR", kinds)
        self.assertIn("DECAY", kinds)

    def test_snapshot_keeps_missing_seed_keywords_visible(self) -> None:
        snapshot = seo_improver.build_snapshot([], [])

        self.assertTrue(snapshot)
        self.assertTrue(all(row["status"] == "not_visible" for row in snapshot))


if __name__ == "__main__":
    unittest.main()
