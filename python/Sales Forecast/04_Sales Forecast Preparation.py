import pandas as pd
import numpy as np
from pathlib import Path
import logging
import time

script_dir = Path(__file__).resolve().parent
project_root = script_dir.parent.parent

processed_folder = project_root / "data" / "processed"
output_folder = project_root / "output"

file_name = "sales_history_cleaned.csv"

input_path = processed_folder / file_name

output_folder.mkdir(
    parents=True, exist_ok=True
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

start_time = time.time()

def Load_data(input_path):
    logging.info(f"Loading data from {input_path}")
    try:
        df = pd.read_csv(input_path)
        logging.info(f"Data loaded successfully with shape {df.shape} rows")
        return df
    except FileNotFoundError:
        logging.error("File not found")
        raise
    except Exception as e:
        logging.error(f"Unexpected error:{e}")
        raise

def create_date_features(df):
    logging.info("Creating date features")
    df["CREATEDON"] = pd.to_datetime(
        df["CREATEDON"], errors="coerce"
    )
    df["YEAR"] = (
        df["CREATEDON"]
        .dt.year
    )
    df["MONTH"] = (
        df["CREATEDON"]
        .dt.month
    )
    df["MONTH_NAME"] = (
        df["CREATEDON"]
        .dt.month_name()
    )
    df["QUARTER"] = (
        df["CREATEDON"]
        .dt.quarter
    )
    df["DAY"] = (
        df["CREATEDON"]
        .dt.day
    )
    df["DAY_NAME"] = (
        df["CREATEDON"]
        .dt.day_name()
    )
    df["WEEK"] = (
        df["CREATEDON"]
        .dt.isocalendar().week
    )
    df["IS_WEEKEND"] = (
        df["DAY_NAME"]
        .isin([
            "Saturday",
            "Sunday"
        ]
        )

        )

    return df

def daily_sales_summary(df):
    logging.info(f"Creating daily sales summary")
    df["SALE_DATE"] = (
        df["CREATEDON"]
        .dt.date
    )
    daily_df = (
        df.groupby("SALE_DATE")
        .agg(
            TOTAL_SALES=("SELL","sum"),
            TOTAL_QTY=("QTY","sum"),
            TRANSACTIONS=("SELL","count")
        )
        .reset_index()
    )
    return daily_df

def rolling_average(df):
    logging.info(f"Calculating rolling averages...")
    df = df.sort_values("SALE_DATE")
    df["ROLLING_7_DAY"] = (
        df["TOTAL_SALES"]
        .rolling(window=7)
        .mean()
    )
    df["ROLLING_30_DAY"] = (
        df["TOTAL_SALES"]
        .rolling(window=30)
        .mean()
    )
    return df

def create_lag_features(df):
    logging.info(f"Creating lag features...")
    df = df.sort_values("SALE_DATE")

    df["LAG_1_DAY"] = (
        df["TOTAL_SALES"]
        .shift(1)
    )

    df["LAG_7_DAY"] = (
        df["TOTAL_SALES"]
        .shift(7)
    )

    df["LAG_30_DAY"] = (
        df["TOTAL_SALES"]
        .shift(30)
    )
    return df

def validate_forecast_data(df):
    logging.info("Running final validation...")
    validation = {}

    validation["Rows"] = len(df)
    validation["Columns"] = len(df.columns)
    validation["Missing Values"] = (
        df.isnull().sum().sum()
    )
    validation["Duplicate Rows"] = (
        df.duplicated().sum()
    )
    validation["Date start"] = (
        df["SALE_DATE"].min()
    )
    validation["Date end"] = (
        df["SALE_DATE"].max()
    )
    return validation

def save_forecast_data(df):
    logging.info("Saving forecast-ready dataset...")

    output_path = (
        output_folder / 
        "sales_forecast_ready.csv"
    )
    df.to_csv(
        output_path,
        index=False
    )
    logging.info(f"Forecast dataset saved: {output_path}")

def export_validation(validation):
    report_path = (
        output_folder / 
        "forecast_validation.xlsx"
    )

    validation_df = pd.DataFrame({
        "Metric": validation.keys(),
        "Value": validation.values()
    })

    validation_df.to_excel(
        report_path,
        index=False
    )
    logging.info(
        f"Validation report save: {report_path}"
    )

def main():
    logging.info(
        "Starting sales forecast preparation..."
    )
    sales_df = Load_data(input_path)
    sales_df = create_date_features(
        sales_df
    )
    daily_df = daily_sales_summary(
        sales_df
    )
    daily_df = rolling_average(
        daily_df
    )
    daily_df = create_lag_features(
        daily_df
    )
    validation = validate_forecast_data(
        daily_df
    )
    save_forecast_data(
        daily_df
    )
    export_validation(
        validation
    )
    runtime = time.time() - start_time

    logging.info(
        f"Forecast preparation completed in "
        f"{runtime:.2f} seconds."
    )

if __name__ == "__main__":
    main()