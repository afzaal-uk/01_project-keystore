# Retail Data Quality Audit

## Overview

This project is a Python data quality audit built using real retail EPOS sales data.

The purpose of this script is to check the quality of the data before using it for further analysis, cleaning, Power BI reporting, or machine learning.

The original raw data is not included in this repository because it comes from a real retail business.

---

## What the Script Does

The Python script automatically:

- Loads the sales data
- Checks the size and structure of the dataset
- Finds missing values
- Finds duplicate rows
- Creates a profile for each column
- Checks data types
- Flags possible numeric columns
- Detects unusual numeric values using the IQR method
- Checks negative numeric values for review
- Calculates a simple data quality score
- Creates an Excel report with the results

---

## Project Files

### Python Script

[`01_retail_data_quality_audit.py`](01_retail_data_quality_audit.py)

This is the main Python script used to run the complete data quality audit.

### Excel Report

[`retail_data_quality_report.xlsx`](retail_data_quality_report.xlsx)

Click the file above to open the generated Excel audit report.

The workbook contains separate sheets for:

- Missing Values
- Duplicate Rows
- Duplicate Summary
- Column Profile
- Data Types
- Outliers
- Business Rules
- Quality Score

---

## Dataset

The audit was tested on a real EPOS retail sales dataset containing more than 300,000 records.

The dataset contains information such as:

- Product descriptions
- Product groups
- Quantity
- Cost
- Selling price
- Gross profit
- VAT
- Retail price
- Product and transaction information

The original dataset is not uploaded to GitHub to protect business data.

---

## Missing Value Analysis

The script checks every column and calculates both the number and percentage of missing values.

![Missing Value Report](missing_values_report.png)

This helps identify columns that may need further investigation or cleaning.

---

## Outlier Detection

The script uses the IQR method to find unusually high or low values in numeric columns.

![Outlier Report](outlier_report.png)

An outlier is only flagged for investigation. It is not automatically treated as incorrect data.

---

## Data Quality Process

The script follows this process:

```text
Raw EPOS Sales Data
        |
        v
Load Data
        |
        v
Dataset Overview
        |
        v
Missing Values
        |
        v
Duplicate Check
        |
        v
Column Profile
        |
        v
Data Type Check
        |
        v
Outlier Detection
        |
        v
Business Rule Check
        |
        v
Data Quality Score
        |
        v
Excel Audit Report
```

---

## Tools Used

- Python
- Pandas
- NumPy
- Pathlib
- Logging
- Excel

---

## Why I Built This

Before analysing a large dataset, I wanted to understand its quality first.

Instead of checking the data manually, I built one Python script that can run different quality checks and create one Excel report.

This also gives me a reusable starting point for the next stage of the project.

---

## Next Step

The next part of the Python project will focus on cleaning and preparing the retail data based on the problems found during this audit.
