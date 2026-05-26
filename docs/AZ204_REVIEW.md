# AZ204 Review Notes

Reviewed `az204/labs/function_apps`. It is directly useful for this project.

Reusable pieces:

- Timer trigger schedule for market-close reporting.
- Deduplication with `lastReportDate`.
- Market-data provider abstraction.
- Plain-text + HTML email rendering.
- Cosmos DB document shape.
- GitHub Actions deployment to Azure Functions.

Lightweight path before Azure:

1. Local JSON/CSV positions.
2. CLI report generator.
3. Optional cron/GitHub Actions scheduled run.
4. Then port into Azure Functions using the az204 pattern.
