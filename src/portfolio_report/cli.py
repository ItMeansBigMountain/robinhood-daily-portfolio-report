from __future__ import annotations

import argparse

from .report import calculate_rows, load_portfolio, render_text_report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("portfolio_json")
    args = parser.parse_args()
    portfolio = load_portfolio(args.portfolio_json)
    rows = calculate_rows(portfolio.get("positions", []))
    print(render_text_report(portfolio.get("reportDate", "today"), rows))


if __name__ == "__main__":
    main()
