# 01_project-keystore

Sales analysis using Python, SQL, Excel and Power BI

# Retail Sales Analysis — Keystore Project

A retail sales analysis built with **Python, SQL, Excel and Power BI**.
Created by a recent Data Science graduate as a hands-on, end-to-end analytics project.

See the full [30-question analysis plan](business-questions.md) for the business
questions driving this project.

---

## Overview

This project takes real retail EPOS data — invoices, takings, product records
and sales history — and turns it into clear business insights. The goal was to answer
questions a shop owner actually cares about:

- How are sales trending month to month?
- Which products make the most money, and which lose money?
- Where is the profit really coming from?

## The Data

The data was extracted from a **Firebird database** and exported as CSV files,
covering tables such as SALES_HISTORY, INVDET, INVHEAD, TAKINGS, PRODUCT and PAYMENT.
The core analysis focuses on the 2025 trading year (SALES_HISTORY holds ~304,875 rows).

> **Note:** The raw sales data is confidential business data and is **not** included in
> this repository. The code, queries, charts and dashboard shown here use it for
> analysis only.

## Tools Used

- **Python** (pandas, matplotlib) — loading, cleaning, analysis and charts
- **SQL** (DBeaver / Firebird, and MySQL Workbench) — querying the source database
- **Excel** — multi-sheet summary reports
- **Power BI** — interactive dashboard

## What I Did

1. **Loaded and combined** multiple CSV files into single datasets using `glob` and `pandas`.
2. **Cleaned the data** — handled missing values, removed duplicates, and fixed date
   and number formats so the data was reliable to analyse.
3. **Queried with SQL** — answered real business questions directly against the Firebird
   database (see the `sql/` folder).
4. **Analysed and summarised** — monthly and yearly trends, product rankings and profit
   breakdowns, exported to a multi-sheet Excel report.
5. **Visualised the results** — charts in Python and an interactive Power BI dashboard.

## Key Findings

- **Gross profit was misleading.** While working in SQL I discovered the `GROSS_PROFIT`
  column actually stores a **margin percentage**, not a monetary value — so summing it
  would be wrong. I calculated true profit as `(SELL - COST) * QTY` instead.
- **Overall margin ≈ 20%** — out of every £1 taken, about 20p is profit.
- **Revenue can mislead:** services like PayPoint and the National Lottery top the
  revenue list but earn almost no profit (commission only). True earners appear only
  when ranking by profit.
- **Fresh food is the profit engine:** Bakery and Catering drive the most profit by far.
- **Sales are fairly steady year-round**, with a mild May peak and October dip.
- **Some products sell at a loss** (below cost) — worth reviewing as pricing errors or
  promotions.

## Dashboard & Charts

![Power BI Dashboard](images/dashboard.png)

*Interactive Power BI dashboard summarising sales and profit.*

## Project Structure

- `python/` — analysis scripts
- `sql/` — SQL queries answering business questions
- `images/` — saved charts and dashboard screenshots
- `excel/` — summary reports
- `powerbi/` — Power BI file
- `business-questions.md` — the 30-question analysis plan

---

*Built as part of my ongoing learning as a Data Science graduate seeking a Data Analyst role.*
