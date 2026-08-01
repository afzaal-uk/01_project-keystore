# Retail Data Cleaning Pipeline

## Overview

This project is a Python-based retail data cleaning pipeline developed using a real EPOS sales dataset.

The pipeline automatically loads raw sales data, cleans and standardizes the dataset, removes duplicate records, handles missing values, creates new business features, validates the cleaned data, and exports a cleaned CSV file together with a cleaning summary.

---

# Technologies Used

- Python
- Pandas
- NumPy
- Pathlib
- Logging
- Excel

---

# Features

The pipeline performs the following tasks:

- Load raw retail sales data
- Clean column names
- Clean text values
- Convert data types
- Handle missing values
- Remove duplicate records
- Create business features
- Validate cleaned data
- Export cleaned CSV
- Export cleaning summary
- Generate execution logs

---

# Project Workflow

```
Raw Sales Data
       │
       ▼
Load Dataset
       │
       ▼
Clean Column Names
       │
       ▼
Clean Text Values
       │
       ▼
Convert Data Types
       │
       ▼
Handle Missing Values
       │
       ▼
Remove Duplicate Records
       │
       ▼
Create Business Features
       │
       ▼
Validate Dataset
       │
       ▼
Export Clean Dataset
```

---

# Project Files

```
Retail Data Cleaning Pipeline
│
├── 02_retail_data_cleaning_pipeline.py
├── README.md
├── Inside VS.png
├── cleaned files.png
└── files after cleaning.png
```

---

# Screenshots

## Python Script

The complete Python cleaning pipeline developed in Visual Studio Code.

![Python Script](Inside%20VS.png)

---

## Generated Clean Files

The pipeline automatically generates cleaned output files after processing.

![Generated Files](cleaned%20files.png)

---

## Final Output Folder

The final cleaned dataset and summary report created by the pipeline.

![Final Output](files%20after%20cleaning.png)

---

# Learning Objectives

This project demonstrates practical use of:

- Python functions
- Modular programming
- Pandas DataFrames
- Data cleaning
- Missing value handling
- Duplicate removal
- Feature engineering
- File handling
- Logging
- ETL workflow

---

# Future Improvements

Possible future enhancements include:

- Business rule validation
- Automatic outlier handling
- Better date validation
- Interactive HTML reports
- Unit testing
- Automated pipeline scheduling
