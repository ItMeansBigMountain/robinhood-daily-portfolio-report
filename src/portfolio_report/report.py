from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_portfolio(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(path).read_text())


def calculate_rows(positions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows = []
    for item in positions:
        symbol = str(item.get("symbol", "")).strip().upper()
        shares = float(item.get("shares", 0) or 0)
        avg_cost = float(item.get("avgCost", 0) or 0)
        prev = float(item.get("previousClose", 0) or 0)
        current = float(item.get("current", 0) or 0)
        if not symbol or shares <= 0 or current <= 0:
            continue
        market_value = shares * current
        cost_basis = shares * avg_cost
        daily_change = shares * (current - prev) if prev else 0.0
        total_change = market_value - cost_basis
        rows.append({
            "symbol": symbol,
            "shares": shares,
            "current": round(current, 2),
            "marketValue": round(market_value, 2),
            "dailyChange": round(daily_change, 2),
            "totalChange": round(total_change, 2),
            "totalChangePct": round((total_change / cost_basis * 100), 2) if cost_basis else 0.0,
        })
    return sorted(rows, key=lambda row: row["symbol"])


def summarize(rows: list[dict[str, Any]]) -> dict[str, float]:
    return {
        "marketValue": round(sum(row["marketValue"] for row in rows), 2),
        "dailyChange": round(sum(row["dailyChange"] for row in rows), 2),
        "totalChange": round(sum(row["totalChange"] for row in rows), 2),
    }


def render_text_report(report_date: str, rows: list[dict[str, Any]]) -> str:
    totals = summarize(rows)
    lines = [
        f"Daily Portfolio Report — {report_date}",
        f"Value: ${totals['marketValue']:.2f} | Day: {format_money(totals['dailyChange'])} | Total: {format_money(totals['totalChange'])}",
        "",
        "Symbol | Shares | Current | Value | Day | Total",
    ]
    for row in rows:
        lines.append(
            f"{row['symbol']} | {row['shares']:g} | ${row['current']:.2f} | "
            f"${row['marketValue']:.2f} | {format_money(row['dailyChange'])} | "
            f"{format_money(row['totalChange'])} ({row['totalChangePct']:+.2f}%)"
        )
    return "\n".join(lines)


def format_money(value: float) -> str:
    sign = "+" if value >= 0 else "-"
    return f"{sign}${abs(value):.2f}"
