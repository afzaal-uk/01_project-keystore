# 01_project-keystore
Sales analysis using Python, SQL, Excel and PowerBI
# Retail Sales Analysis — Keystore Project

A 10-year retail sales analysis built with **Python, SQL, Excel and Power BI**.
Created by a recent Data Science graduate as a hands-on, end-to-end analytics project.

---

## Overview

This project takes a decade of real retail data — invoices, takings, product records
and sales history — and turns it into clear business insights. The goal was to answer
questions a shop owner actually cares about:

- How are sales trending month to month and year to year?
- Which products make the most money, and which lose money?
- Where is the profit really coming from?

## The Data

The data was extracted from a **Firebird database** and exported as **162 CSV files**,
covering tables such as SALES_HISTORY, INVDET, INVHEAD, TAKINGS, PRODUCT and PAYMENT just for the year 2025.

> **Note:** The raw sales data is confidential business data and is **not** included in
> this repository. The code, charts and dashboard shown here use it for analysis only.

## Tools Used

- **Python** (pandas, matplotlib) — loading, cleaning, analysis and charts
- **SQL** — querying the source Firebird database & mySQL workbench
- **Excel** — multi-sheet summary reports
- **Power BI** — interactive dashboard

## What I Did

1. **Loaded and combined** 162 CSV files into single datasets using `glob` and `pandas`.
2. **Cleaned the data** — handled missing values, removed duplicates, and fixed date
   and number formats so the data was reliable to analyse.
3. **Analysed sales** — produced monthly and yearly summaries, product rankings and
   profit breakdowns, exported to a multi-sheet Excel report.
4. **Visualised the results** — built charts in Python and an interactive Power BI dashboard.

## Key Findings

- **Sales trends:** Identified clear monthly sales patterns, making it easy to see which periods are rising and which are falling.
- **Top products:** Found the best-selling products and services — for example cigarettes, off-licence sales and PayPoint services.
- **Underperformers:** Identified slow-moving products that have been sitting in the shop for a long time and may not be worth restocking.
- **Profit:** Can now see which months and products drive the most profit, and what factors affect it.
- **Gross_profit** while doing sql i have folunt out that the gross_profit is actually the percentage.

## Dashboard & Charts

![Power BI Dashboard](images/dashboard.png)

*Interactive Power BI dashboard summarising sales and profit.*

## Project Structure

- `python/` — analysis scripts
- `images/` — saved charts and dashboard screenshots
- `excel/` — summary reports
- `powerbi/` — Power BI file

---

*Built as part of my ongoing learning as a Data Science graduate seeking a Data Analyst role.*
