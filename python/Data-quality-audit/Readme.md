# Retail Data Quality Audit

## Overview

Automated Python data-quality auditing tool developed for
a large real-world EPOS retail sales dataset.

Original production data is excluded from this repository
for confidentiality.

## Dataset

304,875+ sales records
37 attributes
Real EPOS retail environment

## Business Problem

Large operational datasets require systematic quality
assessment before cleaning, analysis, dashboarding or
machine-learning workflows.

This tool automatically audits the dataset and produces
a structured Excel quality report.

## Features

- Dataset profiling
- Missing-value analysis
- Duplicate detection
- Column profiling
- Data-type classification
- Suspected numeric-field detection
- IQR-based statistical outlier detection
- Business-rule screening
- Data-quality scoring
- Automated multi-sheet Excel reporting
- Logging and runtime monitoring

## Pipeline

Raw EPOS Data
    ↓
Data Loading
    ↓
Dataset Overview
    ↓
Missing Values
    ↓
Duplicates
    ↓
Column Profiling
    ↓
Data Type Validation
    ↓
Outlier Detection
    ↓
Business Rule Screening
    ↓
Quality Score
    ↓
Excel Audit Report

## Key Findings

[Your sanitized findings]

## Output

[images here]

## Technologies

Python
Pandas
NumPy
Pathlib
Logging
Excel

## Limitations

Statistical outliers represent observations requiring
investigation and are not automatically data errors.

Generic business-rule checks require domain-specific
interpretation before records are modified.

## Next Stage

02_retail_data_cleaning_pipeline.py
