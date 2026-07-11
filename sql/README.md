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

