# SQL Queries — Keystore Project

This folder contains the SQL queries used to analyse the Keystore retail sales
data. The queries were written and run in **DBeaver** against a **Firebird**
database, and they answer real business questions about sales, products and profit.

## Database

The source is a Firebird EPOS database. The main table used here is
`SALES_HISTORY` (around 304,875 rows for the year analysed), holding one row per
product sold, with columns for date, product, quantity, sell price, cost and more.

> **Note:** These `.sql` files contain the queries only. Real sales figures and
> query results are confidential business data and are not published here.

## A note on gross profit (data validation)

The dataset included a `GROSS_PROFIT` column, but on inspection I found it stored
the profit **margin as a percentage**, not a monetary value — so simply summing it
would have been meaningless. I confirmed this by checking sample rows against the
formula `(SELL - COST) / SELL`, which matched the stored percentages.

I therefore calculated true profit in pounds as `(SELL - COST) * QTY`, validated it
against sample rows, and used that as the correct profit measure throughout the
analysis.

## Queries in this folder

- `15_profit_per_year.sql` — total profit per year, calculated as (sell − cost) × quantity.

*(More queries will be added as the analysis develops.)*

## Keyfinding

-  I found the sales table blends retail product sales with service transactions such as PayPoint bill payments, which carry commission-style economics rather than retail margins. This matters because including them unadjusted can distort revenue and margin figures — so I flagged that product-level analysis may need to exclude service lines.
