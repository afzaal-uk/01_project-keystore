
# Sales Forecast Preparation

A Python-based sales forecasting preparation pipeline built from cleaned retail EPOS data.

The purpose of this script is to transform transaction-level sales data into a structured, time-series-ready dataset for future forecasting and trend analysis.

## What This Script Does

- Loads cleaned retail sales data
- Converts transaction timestamps into usable date features
- Creates daily sales summaries
- Calculates 7-day and 30-day rolling averages
- Creates lag features for previous sales periods
- Validates the forecast-ready dataset
- Exports the prepared dataset and validation report

## Key Features

### Date Features

Creates useful time-based features including:

- Year
- Month
- Month name
- Quarter
- Day
- Day name
- Week number
- Weekend indicator

### Daily Sales Summary

Aggregates transaction-level data into daily metrics:

- Total Sales
- Total Quantity
- Number of Transactions

### Rolling Averages

Calculates:

- 7-day rolling average
- 30-day rolling average

These help identify short-term and longer-term sales trends.

### Lag Features

Creates:

- 1-day lag
- 7-day lag
- 30-day lag

These features can be used by forecasting and machine-learning models to understand previous sales behaviour.

### Validation

The pipeline checks:

- Number of rows
- Number of columns
- Missing values
- Duplicate rows
- Start date
- End date

## Output

The script produces:

- `sales_forecast_ready.csv`
- `forecast_validation.xlsx`

These files provide a clean and structured dataset ready for further forecasting analysis.

## Visual Results

### Forecast Preparation Overview

![Sales Forecast Overview](forecast1.png)

### Sales Trends and Forecast Features

![Sales Forecast Features](forecast2.png)

## Technologies Used

- Python
- Pandas
- NumPy
- Pathlib
- Logging
- Excel
- CSV

## Purpose

This project demonstrates how raw retail transaction data can be transformed into a structured time-series dataset suitable for sales forecasting and business analysis.
