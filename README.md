# 01_project-keystore

Sales analysis using **SQL, Python and Power BI**

# Retail Sales Analysis — Keystore Project

A hands-on retail sales analytics project built using **SQL, Python and Power BI**.

The project uses real retail EPOS data to investigate sales, profit, product performance,
data quality, anomalies, forecasting patterns and product segmentation.

See the full [28-question analysis plan](business-questions.md) for the business
questions driving the SQL analysis, and the [`sql/`](sql/) folder for the queries
and detailed findings.

---

## Overview

This project takes real retail EPOS data — invoices, takings, product records
and sales history — and turns it into practical business insights.

The analysis was designed around questions a shop owner or manager would actually care about:

![10 years RAW data overview](images/Rawdata.png)

- Where is the profit really coming from?
- Which products generate the most value?
- Which products have weak performance?
- How are sales trending over time?
- Are there unusual sales patterns that require investigation?
- Which products should be prioritised?
- Can historical sales be prepared for forecasting?

---

## The Data

The data was extracted from a **Firebird database**, covering tables such as
`SALES_HISTORY`, `INVDET`, `INVHEAD`, `TAKINGS`, `PRODUCT` and `PAYMENT`.

The core Python analysis focuses on the cleaned 2025 sales history dataset,
containing approximately **304,875 transaction-level rows**.

> **Note:** The raw sales data is confidential business data and is **not included**
> in this repository. Screenshots are provided for context, while the code,
> queries and dashboards demonstrate the analytical work performed on the data.

---

## Tools Used

- **SQL** — DBeaver / Firebird for querying and validating the source database
- **Python** — pandas, NumPy, pathlib, logging and time
- **Power BI** — interactive business dashboards and visualisation
- **GitHub** — project organisation, documentation and version control

---

# What I Did

## 1. SQL Business Analysis

I created and validated **28 SQL queries** based on real business questions.

The analysis covers:

- Sales and revenue analysis
- Product performance
- Profit analysis
- Category performance
- Monthly and daily trends
- Ranking and top-performing products
- Window functions
- Subqueries
- Business-focused aggregations

The SQL analysis was also used to validate important characteristics of the source data before reporting results.

See the [`sql/`](sql/) folder for the complete analysis.

---

## 2. Data Validation

One of the most important findings was that the `GROSS_PROFIT` field was misleading.

The field actually stores a **margin percentage**, rather than monetary gross profit.
Therefore, summing the field would produce an incorrect business result.

I validated this against sample records and calculated true monetary profit using:

```text
(SELL - COST) × QTY
