import pandas as pd
import numpy as np
from pathlib import Path
import logging
import time

script_dir = Path(__file__).resolve().parent
project_root = script_dir.parent.parent

raw_folder = project_root / "data" / "raw"
processed_folder = project_root / "data" / "processed"

file_name = "SALES_HISTORY_202606281155.csv"

input_path = raw_folder / file_name
output_path = processed_folder / "sales_history_cleaned.csv"

processed_folder.mkdir(
    parents=True,
    exist_ok=True
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
start_time = time.time()

def load_data(file_path):
    logging.info(f"Loading raw data: {file_path.name}")

    try:
        df = pd.read_csv(file_path)
        logging.info(f"Loaded {len(df):,} rows.")
        return df

    except FileNotFoundError:
        logging.error("Raw data file not found.")
        raise

    except Exception as e:
        logging.error(f"Error loading data: {e}")
        raise

def clean_column_names(df):
    logging.info("Cleaning column names...")

    df.columns = (
        df.columns
        .str.strip()
        .str.replace(" ","_")
        .str.upper()
    )
    return df

def clean_text_columns(df):
    logging.info("Cleaning text columns...")

    text_columns = df.select_dtypes(include="object").columns

    for column in text_columns:
        df[column] = df[column].str.strip()
        df[column] = df[column].replace("", np.nan)

    return df

def convert_data_types(df):
    logging.info("Converting data types...")

    numeric_columns = [
        "QTY",
        "COST",
        "SELL",
        "GROSS_PROFIT",
        "VAT",
        "BONUS",
        "RRP",
        "VAT_RATE",
        "INV_COUNT",
        "M_SAVING_VAT",
        "M_SAVING",
        "PROMO_QTY",
        "REDUCED_QTY"
    ]

    for column in numeric_columns:

        if column in df.columns:
            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            )
    date_columns = [
        "S_DATE",
        "CREATEDON",
        "DELETEDON"
    ]

    for column in date_columns:
        if column in df.columns:
            df[column] = pd.to_datetime(
                df[column],
                errors = "coerce"
            )

    return df

def handle_missing_values(df):
    logging.info("Handling missing values...")

    missing_before = df.isnull().sum().sum()

    optional_text_columns = [
        "PRODGRP2",
        "PRODGRP3",
        "PRODGRP4",
        "PRODGRP5",
        "P_FAMILY1"
    ]

    for column in optional_text_columns:
        if column in df.columns:
            df[column] = df[column].fillna("UNKNOWN")
    missing_after = df.isnull().sum().sum()

    logging.info(f"Missing values before: {missing_before:,}")
    logging.info(f"Missing values after: {missing_after:,}")

    return df

def remove_duplicates(df):
    logging.info("Removing duplicate rows...")

    rows_before = len(df)
    df = df.drop_duplicates()
    rows_after = len(df)

    duplicates_removed = rows_before - rows_after
    logging.info(f"Duplicates removed: {duplicates_removed:,}")

    return df

def validate_cleaned_data(df):
    logging.info("Running final validation...")

    validation = {}
    validation["Rows"] = len(df)
    validation["Missing values"] = (
        df.isnull().sum().sum()
    )

    validation["Duplicate Rows"] = (
        df.duplicated().sum()
    )
    return validation

def save_clean_data(df):
    logging.info("Saving cleaned dataset...")

    df.to_csv(
        output_path,
        index=False

    )

    logging.info(
        f"Cleaned file saved to {output_path}"
    )

def cleaning_summary(raw_df, clean_df):
        logging.info("Creating cleaning summary...")
        summary = pd.DataFrame({
           "Metric": [

            "Rows Before",
            "Rows After",
            "Missing Before",
            "Missing After",
            "Duplicates Before",
            "Duplicates After"

        ],
        "Value": [
            len(raw_df),
            len(clean_df),
            raw_df.isnull().sum().sum(),
            clean_df.isnull().sum().sum(),
            raw_df.duplicated().sum(),
            clean_df.duplicated().sum()
        ]

    })
        return summary

def create_features(df):
    logging.info("Creating business features...")
    if(
        "SELL" in df.columns
        and 
        "QTY" in df.columns
    ):
        df["SALE_VALUE"] = (
            df["SELL"] * df["QTY"]
        )
    if (
        "SELL" in df.columns
        and
        "COST" in df.columns
    ):
        df["PROFIT_VALUE"] = (
            df["SELL"] - df["COST"]
        )
    return df

def export_summary(summary):
    report_path = (
        processed_folder / 
        "cleaning_summary.xlsx"
    )
    summary.to_excel(
        report_path,
        index=False
    )
    logging.info(
        f"Summary saved: {report_path}"
    )

def main():
    logging.info("Starting cleaning pipeline...")

    raw_df = load_data(input_path)
    clean_df = raw_df.copy()
    clean_df = clean_column_names(clean_df)
    clean_df = clean_text_columns(clean_df)
    clean_df = convert_data_types(clean_df)
    clean_df = handle_missing_values(clean_df)
    clean_df = remove_duplicates(clean_df)
    clean_df = create_features(clean_df)

    validation = validate_cleaned_data(clean_df)
    
    summary = cleaning_summary(
        raw_df,
        clean_df
    )
    save_clean_data(clean_df)
    export_summary(summary)
    logging.info("Cleaning pipeline completed successfully.")
    runtime = time.time() - start_time
    logging.info(
        f"Cleaning pipeline completed in {runtime:.2f} seconds."
    )

if __name__ == "__main__":
    main()



    