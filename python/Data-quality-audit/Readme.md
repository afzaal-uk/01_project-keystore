# Retail Data Quality Audit

## Overview

This project is a Python data quality audit built using real-world retail EPOS sales data.

The purpose of this script is to check the quality of the data before using it for further analysis, cleaning, Power BI reporting, or machine learning.

The original raw dataset is not included in this repository because it contains real business data.

## Dataset

The audit was performed on a retail sales dataset containing:

- 304,000+ sales records
- 37 columns
- Product, sales, cost, profit, VAT, quantity and category information

## What the Python Script Does

The script automatically checks:

- Dataset size and memory usage
- Missing values
- Missing value percentages
- Duplicate rows
- Column data types
- Unique values
- Possible incorrect data types
- Numeric outliers using the IQR method
- Negative numeric values for review
- Overall data quality

The results are automatically exported to an Excel report.

## Python Script

The full Python program is available here:

[View Python Script](./01_retail_data_quality_audit.py)

## Excel Audit Report

The script generates an Excel workbook containing separate sheets for the different data quality checks.

[Open Retail Data Quality Report](./retail_data_quality_report.xlsx)

The report contains:

- Missing Values
- Duplicate Rows
- Duplicate Summary
- Column Profile
- Data Types
- Outliers
- Business Rules
- Quality Score

## Results

### Missing Values

The audit checks every column and calculates both the number and percentage of missing values.

![Missing Values Report](./Screenshot%202026-07-27%20101103.png)

### Data Quality Report

The audit results are exported automatically to Excel so the findings can be reviewed without using the Python terminal.

![Data Quality Report](./Screenshot%202026-07-27%20101341.png)

## Tools Used

- Python
- Pandas
- NumPy
- Pathlib
- Logging
- Excel

## Project Workflow

Raw EPOS Data  
↓  
Load Data  
↓  
Dataset Overview  
↓  
Missing Value Check  
↓  
Duplicate Check  
↓  
Column Profile  
↓  
Data Type Validation  
↓  
Outlier Detection  
↓  
Business Rule Check  
↓  
Data Quality Score  
↓  
Excel Report

## Note

Outliers and negative values are flagged for review. They are not automatically treated as errors because some unusual values may represent valid retail activity.

The original business dataset is kept private and is not uploaded to GitHub.
