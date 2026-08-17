# 01_project-keystore

## Retail Sales Analysis — Keystore Project

**End-to-end retail sales analysis using SQL, Python and Power BI**

A hands-on retail analytics project built using real-world EPOS sales data. The project combines SQL-based business analysis, Python data-processing pipelines and statistical analysis, and Power BI dashboards to turn raw transactional data into actionable business insights.

The project was developed around real retail business questions rather than a purely academic dataset.

---

# Project Overview

This project takes real retail EPOS data — including invoices, takings, product records and sales history — and turns it into structured analysis and business intelligence.

The main objective was to answer questions a retail manager or business owner would actually care about:

- Where is the profit really coming from?
- Which products generate the most revenue and profit?
- Which products are underperforming?
- How are sales changing over time?
- Are there unusual sales patterns that require investigation?
- Which products should be treated as high-value products?
- Can historical sales data be prepared for forecasting?
- Can the analytical workflow be automated using Python?
- Can the results be presented clearly through Power BI?

![10 years RAW data overview](images/Rawdata.png)

---

# The Data

The data was extracted from a **Firebird database** used by a retail EPOS system.

The source database contains multiple business tables, including:

- `SALES_HISTORY`
- `INVDET`
- `INVHEAD`
- `TAKINGS`
- `PRODUCT`
- `PAYMENT`

The core sales analysis focuses on the 2025 trading year.

The `SALES_HISTORY` dataset contains approximately **304,875 rows**.

> **Data privacy:**  
> The original raw sales data is confidential business data and is therefore **not included in this repository**. Screenshots are provided where appropriate to demonstrate the structure and scale of the source data.

---

# Tools & Technologies

## SQL

**Firebird / DBeaver**

Used for:

- Business-question analysis
- Aggregation
- Joins
- Subqueries
- Window functions
- Ranking
- Running totals
- Historical comparisons
- Product and category analysis
- Data validation

The SQL folder contains **28 business-focused queries**.

---

## Python

**Python 3**

Main libraries:

- `pandas`
- `numpy`
- `pathlib`
- `logging`
- `time`

Python was used for tasks that go beyond simple SQL querying, including:

- Automated data processing
- Data-quality validation
- Reusable transformation pipelines
- Statistical anomaly detection
- Time-series feature engineering
- Rolling averages
- Lag features
- Product segmentation
- Automated reporting
- Exporting analytical results

---

## Power BI

Used for:

- Interactive dashboards
- KPI reporting
- Sales analysis
- Profit analysis
- Product performance
- Business-level visualisation

Dashboard screenshots are included in the `PowerBI/` folder.

---

# Project Architecture

The project follows a simplified analytical workflow:

```text
Firebird EPOS Database
        │
        ▼
   SQL Analysis
        │
        ├──────────────► Business Findings
        │
        ▼
    Cleaned Data
        │
        ▼
      Python
        │
        ├── Data Quality
        ├── Data Cleaning
        ├── Anomaly Detection
        ├── Forecast Preparation
        └── Product Segmentation
        │
        ▼
   Analytical Outputs
        │
        ▼
     Power BI
        │
        ▼
 Business Intelligence
