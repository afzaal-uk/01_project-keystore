# 01_project-keystore

Sales analysis using Python, SQL and Power BI

# Retail Sales Analysis — Keystore Project

A retail sales analysis built with **SQL and Power BI**, with a Python phase planned next.
Created by a recent Data Science graduate as a hands-on, end-to-end analytics project.

See the full [28-question analysis plan](business-questions.md) for the business
questions driving this project, and the [`sql/`](sql/) folder for the queries and
detailed findings.

---

## Overview

This project takes real retail EPOS data — invoices, takings, product records
and sales history — and turns it into clear business insights. The goal was to answer
questions a shop owner actually cares about:

- Where is the profit really coming from?
- Which products make the most money, and which lose money?
- How are sales trending, and how concentrated is the business?

## The Data

The data was extracted from a **Firebird database**, covering tables such as
SALES_HISTORY, INVDET, INVHEAD, TAKINGS, PRODUCT and PAYMENT.
The core analysis focuses on the 2025 trading year (SALES_HISTORY holds ~304,875 rows).

> **Note:** The raw sales data is confidential business data and is **not** included in
> this repository. The code, queries and dashboard shown here use it for
> analysis only.

## Tools Used

- **SQL** (DBeaver / Firebird) — querying the source database
- **Power BI** — interactive dashboard
- **Python** (pandas, matplotlib) — planned next phase: forecasting, anomaly detection,
  market basket analysis and clustering across multiple years of data

## What I Did

1. **Queried with SQL** — answered 28 real business questions against the Firebird
   database, from basic aggregation up to window functions and subqueries (see the
   [`sql/`](sql/) folder).
2. **Validated key findings**, including correcting a misleading data field before
   reporting any numbers.
3. **Built an interactive Power BI dashboard** connected directly to the database,
