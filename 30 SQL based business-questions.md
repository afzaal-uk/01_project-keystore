## Easy — "how are we doing?" (Q1–10)

1. "What was our total profit for the year?"
2. "What's our overall profit margin — out of every pound we take, how much do we keep?"
3. "Which months were our best and worst for sales?"
4. "Show me the sales trend across the year, month by month."
5. "What are our top 20 best-selling products by revenue?"
6. "Which products actually make us the most profit — not just the most cash?"
7. "Which products are barely selling — our slow movers we could drop?"
8. "Which products sell in high volume but earn us little — the 'busy fools'?"
9. "Which categories or departments drive the most profit?"
10. "Are we selling anything at a loss — below what it cost us?"

## Medium — "let's dig deeper" (Q11–20)

11. "Bakery is our biggest category — give me the top 10 products within Bakery."
12. "Which products have the best profit margin %, ignoring one-off flukes?"
13. "Which products spike in particular months or seasons?"
14. "What's the average sale value in each department?"
15. "Which days of the week are our busiest? I need to plan staff rotas."
16. "How much are we losing to reductions and markdowns?"
17. "Show me our cheap items — under £2 — that still make good profit."
18. "For each category, show me revenue AND profit side by side."
19. "How many different products do we actually carry in each department?"
20. "Which months beat our yearly average for sales?"

## Hard — "the strategic questions" (Q21–30)

21. "What's the single best-selling product in EACH category?"
22. "What share of our total profit comes from our top 10 products? Is it really 80/20?"
23. "Show me month-on-month growth — are we going up or down each month?"
24. "Which suppliers or manufacturers give us the best margins?"
25. "If we dropped the bottom 10% of our products, how much would we actually lose?"
26. "Show me products ranked within each category — the full 1st, 2nd, 3rd pecking order."
27. "Show me our cumulative sales through the year — building toward the annual figure."
28. "Which products are in the top 10 EVERY month — the ones I can always count on?"
29. "Compare each month against the same month last year — are we up or down year-on-year?"
30. "Flag any statistically unusual sales days — anomalies worth investigating."

---

## Notes on outcomes

- **Q1–23, 25–28** were answered directly with SQL.
- **Q24 (supplier margins)** and **Q29 (year-on-year)** became *documented data
  limitations* — the reference data (manufacturer table; multiple years) wasn't
  available in a single database. Identifying and reporting these honestly is itself
  part of the analyst's job.
- **Q30 (anomaly detection)** bridges naturally from SQL into Python, where proper
  statistical methods can flag unusual days across the full history.

*Built as part of the Keystore retail analysis portfolio project.*
