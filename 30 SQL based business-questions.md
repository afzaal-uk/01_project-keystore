# Keystore Project — 30 Business Questions (Manager-Style)

A structured set of 30 questions a retail manager would realistically ask an
analyst, grouped by difficulty. Each was (or will be) answered with SQL against
the Keystore Firebird database in DBeaver.

- **Easy (1–10):** single-idea queries — totals, groups, rankings.
- **Medium (11–20):** combining filters, conditions and multiple measures.
- **Hard (21–30):** window functions, subqueries, joins and advanced logic.

> The `.sql` files contain the queries only. Real sales figures and results are
> confidential business data and are not published.

---

## Easy (1–10) 

1. **"What was our total profit for the year?"**
   → Profit calculated as `(SELL - COST) * QTY`, after discovering `GROSS_PROFIT` was a margin %, not a value.
2. **"What's our overall profit margin — out of every pound we take, how much do we keep?"**
   → Business-wide margin ≈ 20%.
3. **"Which months were our best and worst for sales?"**
   → Monthly totals ranked; sales fairly steady, mild May peak, October dip.
4. **"Show me the sales trend across the year, month by month."**
   → Monthly totals in calendar order (Jan → Dec) to reveal the shape.
5. **"What are our top 20 products by revenue?"**
   → Highest-revenue lines — revealed that services (PayPoint, lottery) dominate raw revenue.
6. **"Which products actually make us the most profit?"**
   → Top products by profit — a very different list to revenue (fresh food and confectionery lead).
7. **"Which products are barely selling — our slow movers?"**
   → Single-unit sellers, filtered with `HAVING` to exclude non-product/service lines.
8. **"Which products sell in high volume but earn us little — the 'busy fools'?"**
   → High units, low profit — shelf space that doesn't pay its way.
9. **"Which categories/departments drive the most profit?"**
   → Profit by `PRODGRP1` — Bakery and Catering are the profit engine.
10. **"Are we selling anything at a loss — below cost?"**
    → Products with negative profit (e.g. certain batteries) — possible pricing errors or promotions.

---

## Medium (11–20) — in progress

11. **"Bakery is our biggest category — give me the top 10 products within Bakery."**
    → Filter to one category (`WHERE PRODGRP1 = 'BAKERY'`), then rank products by profit.
12. **"Which products have the best profit margin %, ignoring one-off flukes?"**
    → Per-product margin %, filtered with `HAVING` so only products with real volume count.
13. **"Which products spike in particular months or seasons?"**
    → Product sales filtered/grouped by month to spot seasonal winners.
14. **"What's the average sale value in each department?"**
    → `AVG` combined with `GROUP BY` category.
15. **"Which days of the week are our busiest?"**
    → Extract day-of-week from `S_DATE` and total sales per day — for staffing decisions.
16. **"How much are we losing to reductions and markdowns?"**
    → Using the `REDUCED_QTY` / `PROMO_QTY` columns to quantify wastage.
17. **"Show me our cheap items (under £2) that still earn good profit."**
    → Combine a `WHERE` price filter with profit grouping.
18. **"For each category, show me revenue AND profit side by side."**
    → Two measures per group — spot categories that look busy but earn little.
19. **"How many different products do we carry in each department?"**
    → `COUNT(DISTINCT ...)` with `GROUP BY` — measuring range and breadth.
20. **"Which months beat the yearly average for sales?"**
    → Compare each month against the overall average — a step toward advanced analysis.

---

## Hard (21–30) — advanced techniques

21. **"What's the single best-selling product in EACH category?"**
    → `ROW_NUMBER()` with `PARTITION BY` category, then keep rank 1 (window function + subquery).
22. **"What share of our total profit comes from our top 10 products?" (the 80/20 rule)**
    → Top-10 profit vs total profit — subquery or running total.
23. **"Show me month-on-month growth % — are we growing or declining?"**
    → `LAG()` window function to compare each month to the previous one.
24. **"Which suppliers or manufacturers give us the best margins?"**
    → `JOIN` `SALES_HISTORY` to the supplier/manufacturer table.
25. **"If we dropped the bottom 10% of products, how much would we lose?"**
    → Rank/percentile products, then measure the tail's contribution.
26. **"Rank products within each category and show their position."**
    → `RANK()` / `DENSE_RANK()` over category partitions.
27. **"What's our running (cumulative) sales total through the year?"**
    → Running total using a window `SUM() OVER (ORDER BY ...)`.
28. **"Which products are consistently in the top 10 every month?"**
    → Monthly ranking combined and filtered for consistency.
29. **"Compare each month's sales against the same month last year."**
    → Year-on-year comparison (`LAG` by 12, or across yearly data).
30. **"Flag any statistically unusual sales days — anomalies."**
    → Identify outlier days; naturally bridges from SQL into Python for proper statistics.

---

