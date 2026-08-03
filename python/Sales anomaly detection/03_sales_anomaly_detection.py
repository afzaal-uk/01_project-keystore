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
    parents=True,
    exist_ok = True
)


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

start_time = time.time()

def load_data(file_path):
    logging.info(f"Loading cleaned data: {file_path.name}")

    try:
        df = pd.read_csv(file_path)
        logging.info(
        f"Loaded{len(df):,} rows."
        )

        return df
    except FileNotFoundError:
        logging.error(f"File not found.")
        raise

def product_sales_summary(df):
    logging.info("Creating product sales summary...")
    summary_df = (
    df.groupby(["EANCODE", "S_DESC"])
    .agg(

        TOTAL_QTY=("QTY", "sum"),

        AVG_QTY=("QTY", "mean"),

        STD_QTY=("QTY", "std"),

        TRANSACTIONS=("QTY", "count"),

        AVG_SELL=("SELL", "mean")

    )
    .reset_index()
)
    return summary_df

def detect_high_sales(summary_df, threshold):
    logging.info("Detecting products with high sales...")
    high_sales = summary_df[
        summary_df["TOTAL_QTY"] > threshold
    ]
    logging.info(f"Products found: {len(high_sales):,}")
    return high_sales

def calculate_z_score(summary_df):
    logging.info("Calculating Z_score....")

    mean_qty = summary_df["TOTAL_QTY"].mean()

    std_qty = summary_df["TOTAL_QTY"].std()

    summary_df["Z_SCORE"] = (
        summary_df["TOTAL_QTY"] - mean_qty
    ) / std_qty

    return summary_df

def detect_anomalies(summary_df):
    logging.info("Detecting sales anomalies...")
    anomalies = summary_df[
        abs(summary_df["Z_SCORE"]) > 3
    ]
    logging.info(f"Anomalies found: {len(anomalies):,}")
    return anomalies

def export_anomalies(anomalies_df):
    logging.info("Exporting anomaly report...")
    report_path = (
        output_folder /
        "Sales_anomalies.xlsx"
    )
    anomalies_df.to_excel(
        report_path,
        index=False
    )
    logging.info(
        f"Report saved: {report_path}"
    )

def anomaly_summary(summary_df, anomalies_df):
    logging.info("Creating anomaly summary...")
    summary = pd.DataFrame({
        "Metric": [

            "Products Analysed",
            "Anomalies Found",
            "Average Quantity",
            "Average Selling Price"

        ],
        "Value": [
            len(summary_df),
            len(anomalies_df),
            round(summary_df["TOTAL_QTY"].mean(), 2),
            round(summary_df["AVG_SELL"].mean(), 2)
        ]
    })
    return summary

def export_summary(summary):
    report_path = (
        output_folder /
        "anomaly_summary.xlsx"
    )
    summary.to_excel(
        report_path,
        index=False
    )
    logging.info(
        f"Summary report saved: {report_path}"
    )


def main():
    logging.info("Starting anomaly detection..."
    )
    sales_df = load_data(input_path)
    summary_df = product_sales_summary(sales_df)
    summary_df = calculate_z_score(summary_df)
    anomalies_df = detect_anomalies(summary_df)

    summary = anomaly_summary(
        summary_df,
        anomalies_df
    )
    export_anomalies(anomalies_df)
    export_summary(summary)
    runtime = time.time() - start_time
    logging.info(
        f"Pipeline completed in {runtime:.2f} seconds."
    )

if __name__ == "__main__":


     main()