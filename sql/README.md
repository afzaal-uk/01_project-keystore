# SQL Queries — Keystore Project

This folder contains the SQL queries used to analyse the Keystore retail sales
data. The queries were written and run in **DBeaver** against a **Firebird**
database, and each one answers a real business question about sales, products and profit.

## Database

The source is a Firebird EPOS database. The main table is `SALES_HISTORY`
(around 304,875 rows), holding one row per product line sold, with columns for
date (`S_DATE`), product (`EANCODE`, `S_DESC`), quantity (`QTY`), sell price
(`SELL`), cost (`COST`), category (`PRODGRP1`) and more.

> **Note:** These `.sql` files contain the queries only. Real sales figures and
> query results are confidential business data and are not published here.

## Key findings

- **Gross profit is a percentage, not a value.** The `GROSS_PROFIT` column stored the
  profit margin as a percentage, not a monetary amount — so summing it would have been
  meaningless. I confirmed this by checking sample rows against `(SELL - COST) / SELL`,
  which matched the stored percentages. I therefore calculated true profit in pounds as
  `(SELL - COST) * QTY` and used that as the correct profit measure throughout.
- **The overall profit margin is ~20%** — out of every £1 taken, about 20p is profit.
- **Revenue can mislead.** Services like PayPoint, PayZone and the National Lottery top
  the revenue list but earn almost no profit (commission only). Ranking by profit reveals
  the true earners.
- **Fresh food is the profit engine.** Bakery and Catering drive the most profit by far —
  the shop is more of a food destination than a traditional newsagent.
- **Some products sell at a loss** — a handful of lines were sold below cost, worth
  reviewing as possible pricing errors or promotions.
- **The sales table mixes retail sales with service transactions** (PayPoint, lottery),
  which carry commission-style economics rather than retail margins. Including them
  unadjusted can distort revenue and margin figures, so product-level analysis may need
  to exclude service lines.

## Queries in this folder

- `01_Extract Profit using sell-cost.sql` — total profit per year, calculated as (sell − cost) × quantity.
- `02_Profit_margin_%.sql` — overall profit margin for the business as a percentage.
- `03_total_sales_per_month.sql` — total sales per month, ranked to find the best and worst months.
- `04_total_sales_trend_per_month.sql` — monthly sales in calendar order, showing the yearly trend.
- `05_top 20 best-selling products by revenue.sql` — the highest-revenue products.
- `07_top_20_products_by_profit.sql` — the most profitable products (a different ranking to revenue).
- `08_slow_moving_products.sql` — genuine slow-moving products, filtered to exclude non-product lines.
- `09_big units but small profit.sql` — high-volume, low-profit products ("busy fools").
- `10_profit_by_category.sql` — total profit by product category (PRODGRP1).
- `14_products_sold_at_a_loss.sql` — products sold below cost, identified by negative profit.

*(More queries will be added as the analysis develops.)*
