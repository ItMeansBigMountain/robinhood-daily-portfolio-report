import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))

from portfolio_report.report import calculate_rows, render_text_report, summarize


class PortfolioReportTests(unittest.TestCase):
    def test_calculates_daily_and_total_performance(self):
        rows = calculate_rows([
            {"symbol": "aapl", "shares": 2, "avgCost": 100, "previousClose": 120, "current": 125},
            {"symbol": "msft", "shares": 1, "avgCost": 200, "previousClose": 210, "current": 205},
        ])
        totals = summarize(rows)
        self.assertEqual(totals["marketValue"], 455)
        self.assertEqual(totals["dailyChange"], 5)
        self.assertEqual(totals["totalChange"], 55)
        report = render_text_report("2026-05-25", rows)
        self.assertIn("Daily Portfolio Report", report)
        self.assertIn("AAPL", report)


if __name__ == '__main__':
    unittest.main()
