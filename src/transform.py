import pandas as pd
from src.utils import setup_logger
from config import PROCESSED_DATA_PATH

logger = setup_logger(__name__)

def clean_data(df):
    logger.info("Starting data cleaning...")
    
    initial_rows = len(df)
    
    df = df.dropna()
    
    df.columns = df.columns.str.strip().str.lower()
    
    df["date"] = pd.to_datetime(df["date"])
    
    df["total_sales"] = df["quantity"] * df["price"]
    
    final_rows = len(df)
    dropped = initial_rows - final_rows
    
    if dropped > 0:
        logger.warning(f"{dropped} rows with null values were dropped")
    
    logger.info(f"Cleaning complete. {final_rows} rows ready.")
    return df


def summarize_by_region(df):
    logger.info("Summarizing sales by region...")
    
    summary = df.groupby("region")["total_sales"].sum().reset_index()
    summary.columns = ["region", "total_revenue"]
    summary = summary.sort_values("total_revenue", ascending=False)
    
    logger.info(f"Summary complete. {len(summary)} regions found.")
    return summary