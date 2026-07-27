import pandas as pd
import numpy as np
from pathlib import Path
import logging
import time


# --------------------------------------------------
# Project configuration
# Build paths from the script location so the project
# can run without hard-coded C:\Users\... paths.
# --------------------------------------------------

script_dir = Path(__file__).resolve().parent
project_root = script_dir.parent.parent

data_folder = project_root / "data" / "raw"
output_folder = project_root / "output"

file_name = "SALES_HISTORY_202606281155.csv"
file_path = data_folder / file_name

output_folder.mkdir(exist_ok=True)


# Logging shows the progress of the audit while it runs.

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

start_time = time.time()


# --------------------------------------------------
# Load the raw sales data
# --------------------------------------------------

def load_data(file_path):
    logging.info(f"Reading file: {file_path.name}")

    try:
        df = pd.read_csv(file_path)
        logging.info("File loaded successfully.")
        return df

    except FileNotFoundError:
        logging.error("File not found.")
        raise

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise


# --------------------------------------------------
# Basic dataset overview
# Gives a quick idea of dataset size and structure.
# --------------------------------------------------

def dataset_overview(df):
    logging.info("Creating dataset overview...")

    total_rows = df.shape[0]
    total_columns = df.shape[1]
    total_cells = total_rows * total_columns

    memory_usage = df.memory_usage(deep=True).sum() / 1024**2

    numeric_columns = df.select_dtypes(include=np.number).shape[1]
    text_columns = df.select_dtypes(include="object").shape[1]

    logging.info(f"Rows: {total_rows}")
    logging.info(f"Columns: {total_columns}")
    logging.info(f"Total cells: {total_cells}")
    logging.info(f"Memory Usage: {memory_usage:.2f} MB")
    logging.info(f"Numeric Columns: {numeric_columns}")
    logging.info(f"Text Columns: {text_columns}")


# --------------------------------------------------
# Missing-value audit
# Checks both the number and percentage of missing
# values in every column.
# --------------------------------------------------

def missing_values_report(df):
    logging.info("Checking missing values...")

    missing_count = df.isnull().sum()

    missing_percentage = (
        missing_count / len(df)
    ) * 100

    missing_df = pd.DataFrame({
        "Missing Values": missing_count,
        "Missing %": missing_percentage
    })

    missing_df = (
        missing_df
        .sort_values(by="Missing Values", ascending=False)
        .reset_index()
        .rename(columns={"index": "Column"})
    )

    return missing_df


# --------------------------------------------------
# Duplicate audit
# Keeps the duplicate records and also creates a
# small summary for the final report.
# --------------------------------------------------

def duplicate_report(df):
    logging.info("Checking duplicate rows...")

    duplicate_rows = df.duplicated()

    total_duplicates = duplicate_rows.sum()
    duplicate_df = df[duplicate_rows]

    duplicate_summary = pd.DataFrame({
        "Metric": [
            "Total Rows",
            "Duplicate Rows"
        ],
        "Value": [
            len(df),
            total_duplicates
        ]
    })

    logging.info(f"Duplicate rows found: {total_duplicates}")

    return duplicate_df, duplicate_summary


# --------------------------------------------------
# Column profiling
# Creates one summary record for every field in the
# dataset without changing the original data.
# --------------------------------------------------

def column_profile(df):
    logging.info("Creating column profile...")

    profile_data = []

    for column in df.columns:

        non_null_values = df[column].dropna()

        sample_value = (
            non_null_values.iloc[0]
            if not non_null_values.empty
            else "No data"
        )

        profile_data.append({
            "Column": column,
            "Data Type": str(df[column].dtype),
            "Missing Values": df[column].isnull().sum(),
            "Unique Values": df[column].nunique(),
            "Sample Value": sample_value
        })

    profile_df = pd.DataFrame(profile_data)

    return profile_df


# --------------------------------------------------
# Data-type validation
# Classifies each field and flags text columns where
# most populated values can be converted to numbers.
# --------------------------------------------------

def data_type_validation(df):
    logging.info("Checking data types...")

    datatype_data = []

    for column in df.columns:

        if pd.api.types.is_numeric_dtype(df[column]):
            category = "Numeric"

        elif pd.api.types.is_datetime64_any_dtype(df[column]):
            category = "Date"

        elif pd.api.types.is_bool_dtype(df[column]):
            category = "Boolean"

        else:
            category = "Text"

        status = "OK"
        numeric_conversion_pct = None

        if category == "Text":

            non_null_values = df[column].dropna()

            if not non_null_values.empty:

                converted_values = pd.to_numeric(
                    non_null_values,
                    errors="coerce"
                )

                numeric_conversion_pct = (
                    converted_values.notna().mean() * 100
                )

                if numeric_conversion_pct >= 90:
                    status = "Suspected Numeric"

        datatype_data.append({
            "Column": column,
            "Data Type": str(df[column].dtype),
            "Category": category,
            "Numeric Conversion %": numeric_conversion_pct,
            "Status": status
        })

    datatype_df = pd.DataFrame(datatype_data)

    return datatype_df


# --------------------------------------------------
# Statistical outlier detection
# Uses the IQR method to flag unusually high or low
# observations in numeric columns.
# --------------------------------------------------

def outlier_detection(df):
    logging.info("Detecting numeric outliers...")

    outlier_data = []

    numeric_columns = df.select_dtypes(
        include=np.number
    ).columns

    for column in numeric_columns:

        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)

        iqr = q3 - q1

        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        outliers = df[
            (df[column] < lower_bound) |
            (df[column] > upper_bound)
        ]

        outlier_count = len(outliers)

        outlier_percentage = (
            outlier_count / len(df)
        ) * 100

        outlier_data.append({
            "Column": column,
            "Q1": q1,
            "Q3": q3,
            "IQR": iqr,
            "Lower Bound": lower_bound,
            "Upper Bound": upper_bound,
            "Outlier Count": outlier_count,
            "Outlier %": outlier_percentage
        })

    outlier_df = pd.DataFrame(outlier_data)

    return outlier_df


# --------------------------------------------------
# Business-rule screening
# Negative numeric values are flagged for review.
# A negative value is not automatically treated as
# an error because it may be valid business activity.
# --------------------------------------------------

def business_rule_validation(df):
    logging.info("Checking business rules...")

    validation_data = []

    numeric_columns = df.select_dtypes(
        include=np.number
    ).columns

    for column in numeric_columns:

        negative_count = (df[column] < 0).sum()

        validation_data.append({
            "Column": column,
            "Rule": "Negative Values",
            "Violations": negative_count,
            "Violation %": (
                negative_count / len(df)
            ) * 100
        })

    validation_df = pd.DataFrame(validation_data)

    return validation_df


# --------------------------------------------------
# Simple quality score
# Uses missing data and duplicate rows as the first
# two measurable quality indicators.
# --------------------------------------------------

def data_quality_score(df):
    logging.info("Calculating data quality score...")

    total_cells = df.shape[0] * df.shape[1]

    missing_cells = df.isnull().sum().sum()
    duplicate_rows = df.duplicated().sum()

    missing_rate = missing_cells / total_cells
    duplicate_rate = duplicate_rows / len(df)

    score = 100 - (
        missing_rate * 50 +
        duplicate_rate * 50
    )

    score = max(0, min(100, score))

    return round(score, 2)


# --------------------------------------------------
# Export all audit results into one Excel workbook.
# Each audit area is stored on a separate worksheet.
# --------------------------------------------------

def export_report(
    missing_df,
    duplicate_df,
    duplicate_summary,
    profile_df,
    datatype_df,
    outlier_df,
    validation_df,
    score
):

    logging.info("Exporting audit report...")

    report_path = (
        output_folder /
        "retail_data_quality_report.xlsx"
    )

    with pd.ExcelWriter(report_path) as writer:

        missing_df.to_excel(
            writer,
            sheet_name="Missing Values",
            index=False
        )

        duplicate_df.to_excel(
            writer,
            sheet_name="Duplicate Rows",
            index=False
        )

        duplicate_summary.to_excel(
            writer,
            sheet_name="Duplicate Summary",
            index=False
        )

        profile_df.to_excel(
            writer,
            sheet_name="Column Profile",
            index=False
        )

        datatype_df.to_excel(
            writer,
            sheet_name="Data Types",
            index=False
        )

        outlier_df.to_excel(
            writer,
            sheet_name="Outliers",
            index=False
        )

        validation_df.to_excel(
            writer,
            sheet_name="Business Rules",
            index=False
        )

        pd.DataFrame({
            "Metric": ["Data Quality Score"],
            "Value": [score]
        }).to_excel(
            writer,
            sheet_name="Quality Score",
            index=False
        )

    logging.info(f"Report saved to: {report_path}")


# --------------------------------------------------
# Main pipeline
# Runs each audit stage and passes the results to the
# final Excel report.
# --------------------------------------------------

def main():
    logging.info("Starting retail data quality audit...")

    sales_df = load_data(file_path)

    dataset_overview(sales_df)

    missing_df = missing_values_report(sales_df)

    duplicate_df, duplicate_summary = duplicate_report(
        sales_df
    )

    profile_df = column_profile(sales_df)

    datatype_df = data_type_validation(sales_df)

    outlier_df = outlier_detection(sales_df)

    validation_df = business_rule_validation(sales_df)

    score = data_quality_score(sales_df)

    export_report(
        missing_df,
        duplicate_df,
        duplicate_summary,
        profile_df,
        datatype_df,
        outlier_df,
        validation_df,
        score
    )

    runtime = time.time() - start_time

    logging.info(f"Data Quality Score: {score}/100")
    logging.info(
        f"Audit completed in {runtime:.2f} seconds."
    )


if __name__ == "__main__":
    main()