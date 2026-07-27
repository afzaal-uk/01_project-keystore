# Retail Data Quality Audit

## Overview

This project is a Python data quality audit built using real retail EPOS sales data.

The purpose of this script is to check the quality of the data before using it for further analysis, cleaning, reporting, or machine learning.

The dataset contains more than 300,000 sales records and 37 columns.

The original raw data is not uploaded to GitHub because it comes from a real retail business.

---

## What This Script Does

The Python script automatically checks the dataset for:

- Dataset size and memory usage
- Missing values
- Missing value percentage
- Duplicate rows
- Column data types
- Unique values
- Possible incorrect data types
- Numeric outliers using the IQR method
- Negative numeric values for review
- Overall data quality score

After completing the checks, the script creates an Excel report with the results.

---

## Python Skills Used

This project uses:

- Pandas
- NumPy
- Pathlib
- Functions
- Loops
- Dictionaries and lists
- Exception handling
- Logging
- Data type validation
- IQR outlier detection
- Excel report generation

---

## Project Process

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

---

## Files

### `01_retail_data_quality_audit.py`

This is the main Python script.

It reads the sales data, runs all data quality checks, and creates the final Excel report.

### `retail_data_quality_report.xlsx`

This is the output created by the Python script.

The Excel file contains separate sheets for:

- Missing Values
- Duplicate Rows
- Duplicate Summary
- Column Profile
- Data Types
- Outliers
- Business Rules
- Quality Score

---

## Results

The audit was successfully run on more than 300,000 retail sales records.

The script found missing data in some columns, checked duplicate records, analysed column types, detected possible outliers, and created a complete Excel audit report.

The purpose of the audit is to identify possible data quality problems. It does not automatically remove or change the original data.

---

## Screenshots

### Data Quality Audit Results

![Data Quality Audit Results](Screenshot%202026-07-27%20101103.png)

### Excel Audit Report

![Excel Audit Report](Screenshot%202026-07-27%20101341.png)

---

## Important Note

The original dataset is not included in this repository because it contains real business data.

The audit identifies possible problems for further investigation. For example, an outlier or negative value is not automatically considered an error because it may represent valid retail activity.

---

## Next Step

The next part of this project is a Python data cleaning pipeline.

The cleaning pipeline will use the results from this audit to clean and prepare the data while keeping the original raw data unchanged.
