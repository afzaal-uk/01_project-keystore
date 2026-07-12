# SQL Queries — Keystore Project

This folder contains the SQL queries used to analyse the Keystore retail sales
data. The queries were written and run in **DBeaver** against a **Firebird**
database, and each one answers a real business question a retail manager would ask.

## Database

The source is a Firebird EPOS database. The main table is `SALES_HISTORY`
(around 304,875 rows for the 2025 trading year), with one row per product line
sold — columns for date (`S_DATE`), product (`EANCODE`, `S_DESC`), quantity
(`QTY`), sell price (`SELL`), cost (`COST`), category (`PRODGRP1`), manufacturer
(`M_MANUF`) and more.

> **Note:** These `.sql` files contain the queries only. Real sales figures and
> query results are confidential business data and are not published here.

## Key findings

**Profit & margin**
- **`GROSS_PROFIT` is a percentage, not a value.** The column stores a margin %, not
  money — so summing it is meaningless. Confirmed against `(SELL - COST) / SELL`, then
  true profit calculated as `(SELL - COST) * QTY` throughout.
- **Overall margin ≈ 20%** — out of every £1 taken, about 20p is profit.
- **Revenue is misleading on its own.** PayPoint had ~£2m revenue but only ~£10k profit
  (≈0.5% margin); Bakery earned similar revenue but ~£828k profit (≈39% margin) — Bakery
  makes roughly 80× more profit on comparable revenue.
- **Profit is extremely concentrated.** The top 10 products generate ~60% of all profit.
- **Some products sell at a loss** (below cost) — worth reviewing as pricing errors or
  promotions.

**Products & range**
- **Fresh food is the profit engine** — Bakery and Catering drive the most profit by far.
- **Cheap items under £2 are quiet workhorses** — energy drinks, Rizla papers, bread and
  penny sweets earn steady profit through volume.
- **Five products are the reliable core** — Auld's rolls, Daily Record, lottery, carrier
  bags and Mortons confectionery appear in the top 10 *every month*.
- **The range is heavily bloated.** Dropping the 500 weakest products would lose only
  ~£1,159 revenue and ~£240 profit for the entire year (under 0.01% of the business).
- **Confectionery carries the widest range** (1,302 products) but modest profit; Bakery
  carries just 141 products yet leads on profit — range and profit are not the same thing.

**Time & operations**
- **Sales are steady year-round** with a mild May peak and October dip.
- **Month-on-month, sales are volatile** (swinging roughly −12% to +20%) rather than
  trending — stable overall but bumpy; best handled with a rolling average.
- **Annual turnover ≈ £14.9m** (confirmed via a cumulative running total).
- **Friday and Saturday are busiest**; Sunday quietest by far — useful for staff rotas.
- **Promotions concentrate in impulse/multibuy categories** (soft drinks, off-licence,
  confectionery, crisps).

**Data-quality findings**
- **The sales table mixes retail with service transactions** (PayPoint, PayZone, lottery),
  which carry commission economics, not retail margins — they must be treated separately.
- **`REDUCED_QTY` is empty** across all rows — reductions aren't tracked at line level.
- **The `MANUFACTURER` lookup table is empty** — supplier/manufacturer margin analysis
  wasn't possible (a documented limitation, not a method failure).
- **An uncategorised `XXX` product group** was noted as a data-quality item.

## Techniques demonstrated

Aggregation and grouping, multi-condition filtering (`WHERE` / `HAVING`),
`COUNT(DISTINCT)`, date functions (`EXTRACT`), **subqueries**, and four
**window functions**: `ROW_NUMBER()`, `RANK()`, `LAG()` and `SUM() OVER (...)`.

## Queries in this folder

- `01_Extract Profit using sell-cost.sql` — total profit per year, as (sell − cost) × quantity.
- `02_Profit_margin_%.sql` — overall profit margin for the business.
- `03_total_sales_per_month.sql` — total sales per month, ranked for best/worst.
- `04_total_sales_trend_per_month.sql` — monthly sales in calendar order (the trend).
- `05_top 20 best-selling products by revenue.sql` — highest-revenue products.
- `07_top_20_products_by_profit.sql` — most profitable products (differs from revenue).
- `08_slow_moving_products.sql` — genuine slow movers, filtered to exclude non-product lines.
- `09_big units but small profit.sql` — high-volume, low-profit products ("busy fools").
- `10_profit_by_category.sql` — total profit by category.
- `11_top_products_in_bakery.sql` — top products within the Bakery category.
- `12_highest_margin_products.sql` — highest-margin products, excluding low-volume flukes.
- `13_top_products_in_month.sql` — top products for a specific month (seasonality).
- `14_avg_sale_by_category.sql` — average sale value per department, with counts for context.
- `14_products_sold_at_a_loss.sql` — products sold below cost.
- `15_busiest_days_of_week.sql` — total sales by day of week.
- `16_promotions_by_category.sql` — promotional units by category.
- `17_cheap_profitable_items.sql` — cheap items (under £2) that still earn well.
- `18_revenue_vs_profit_by_category.sql` — revenue and profit side by side per category.
- `19_products_per_category.sql` — number of distinct products per category.
- `20_months_above_average.sql` — months beating the yearly average (subquery).
- `21_top_product_per_category.sql` — the #1 product in each category (`ROW_NUMBER`).
- `22_top10_profit_share.sql` — share of total profit from the top 10 products.
- `23_month_on_month_growth.sql` — month-on-month % growth (`LAG`).
- `25_bottom_products_impact.sql` — revenue/profit at risk from dropping the weakest products.
- `26_top3_products_per_category.sql` — top 3 products per category (`RANK`).
- `27_running_total_sales.sql` — cumulative sales through the year (`SUM OVER`).
- `28_consistent_top_products.sql` — products in the top 10 every month.

## Documented limitations

- **Q24 (supplier margins):** the `MANUFACTURER` table was empty; the JOIN technique was
  validated against the schema but couldn't be run for lack of reference data.
- **Q29 (year-on-year):** the 2025 file holds only one year; year-on-year comparison
  requires combining multiple yearly databases — a natural next step in Python.
