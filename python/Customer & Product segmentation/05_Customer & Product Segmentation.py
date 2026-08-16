import pandas as pd
import numpy as np
from pathlib import Path
import logging
import time

script_dir = Path(__file__).resolve().parent
project_root =script_dir.parent.parent

processed_folder = project_root / "data" / "processed" 
output_folder = project_root / "output"

file_name ="sales_history_cleaned.csv"

input_path = processed_folder / file_name

output_folder.mkdir(
    parents=True,
    exist_ok=True
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
    )
start_time = time.time()

def load_data(file_path):
    logging.info(
        f"Loading data from {file_path.name}"
    )
    try:
        df = pd.read_csv(file_path)
        logging.info(
            f"Loaded {len(df)} rows."
        )
        return df
    except FileNotFoundError:
        logging.error("File not found.")
        raise
    except Exception as e:
        logging.error(
            f"Unexpected error: {e}"
        )
        raise

def product_performance_summary(df):
    logging.info(
    f"Creating product performance summary...."
)
    summary_df = (
        df.groupby(
            ["EANCODE", "S_DESC"]
     )

        .agg(
            TOTAL_QTY=("QTY","sum"),
            TOTAL_SALES=("SELL", "sum"),
            AVG_SELL=("SELL","mean"),
            TOTAL_PROFIT=("GROSS_PROFIT", "sum"),
            TRANSACTIONS=("SELL", "count")
        )
        .reset_index()

    )
    return summary_df

def calculate_profit_margin(df):
    logging.info(
        "Calculating profit margins..."
    )
    df["PROFIT_MARGIN"] = (
        df["TOTAL_PROFIT"]
        / df["TOTAL_SALES"]
    ) * 100
    return df

def create_sales_segments(df):
    logging.info(
        "Creating sales segments..."
    )

    df["SALES_SEGMENT"] = pd.qcut(
        df["TOTAL_SALES"],
        q=3,
        labels=[
            "Low",
            "Medium",
            "High"
        ],
        duplicates="drop"
    )
    return df

def create_product_segment(df):
    logging.info(
        "Creating product segments..."
    )
    conditions = [
        (
            (df["SALES_SEGMENT"]=="High") &
            (df["PROFIT_MARGIN"] >= 20)
        ),
        (
            (df["SALES_SEGMENT"] == "Medium") &
            (df["PROFIT_MARGIN"] >= 10)
        )
    ]

    choices = [
        "High Value",
        "Medium Value"
    ]
    df["PRODUCT_SEGMENT"] = np.select(
        conditions,
        choices,
        default="Low Value"
    )
    return df
def validate_segments(df):
    logging.info(
        "Validating product segments..."
    )
    validation = pd.DataFrame({
        "Segment": (
            df["PRODUCT_SEGMENT"]
            .value_counts()
            .index
        ),
        "Products" : (
            df["PRODUCT_SEGMENT"]
            .value_counts()
            .values
        ),

    })
    return validation

def save_segmented_data(df):
    logging.info(
        "Saving segmented product data..."
    )
    output_path = (
        output_folder /
        "product_segmentation.csv"
    )
    df.to_csv(
        output_path,
        index=False
    )
    logging.info(
        f"Segmented data saved: {output_path}"
    )
def export_validation(validation):
    report_path = (
        output_folder /
        "product_segmentation_summary.xlsx"
    )
    validation.to_excel(
        report_path,
        index=False
    )
    logging.info(
        f"Segmentaion summary saved: {report_path}"
    )

def main():
    logging.info("Starting product segmentaion...")
    sales_df = load_data(input_path)

    summary_df = product_performance_summary(
        sales_df
    )
    summary_df = calculate_profit_margin(
        summary_df
    )
    summary_df = create_sales_segments(
        summary_df
    )
    summary_df = create_product_segment(
        summary_df
    )
    
    validation = validate_segments(
        summary_df
    )
    summary_df = save_segmented_data(
        summary_df
    )
    export_validation(
        validation
    )

    runtime = time.time() - start_time
    logging.info(
        f"Product segmentation completed in "
        f"{runtime:.2f} seconds."
    )

if __name__=="__main__":
    main()