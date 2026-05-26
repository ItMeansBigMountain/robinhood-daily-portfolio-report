# Robinhood Daily Portfolio Report

Lightweight daily stock performance report inspired by the `az204` Azure Function App lab.

## Why this exists

The old `robinhood-email-reports` concept should become a small production-ready service that emails a daily portfolio performance report directly tied to your holdings.

## Reviewed source

`/opt/data/HeRmEz/projects/az204/labs/function_apps/` already contains a useful Function App pattern:

- Timer-triggered daily report after market close.
- Cosmos DB user/portfolio documents.
- Market data provider abstraction.
- SMTP email delivery.
- GitHub Actions deployment workflow.

This repo starts lighter: local JSON/CSV portfolio in, daily report out. Azure Functions can be added using the az204 pattern when ready.

## MVP

- Store positions in `data/portfolio.example.json`.
- Fetch/accept latest prices.
- Calculate daily and total performance.
- Render text report suitable for email/SMS/Discord.
- Later: Azure Timer Function, Cosmos/SQLite, email automation, brokerage import/export parsing.

## Not financial advice

This is tracking/reporting software, not investment advice.
