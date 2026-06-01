import logging
from src.extract import read_csv
from src.transform import clean_data, summarize_by_region
from src.load import save_processed, save_output
from src.utils import setup_logger

logger = setup_logger(__name__)

def run_pipeline():
    logger.info("========== Pipeline started ==========")
    
    try:
        # Extract
        df = read_csv("sales.csv")
        
        # Transform
        df_clean = clean_data(df)
        summary = summarize_by_region(df_clean)
        
        # Load
        save_processed(df_clean, "sales_cleaned.csv")
        save_output(summary, "sales_by_region.csv")
        
        logger.info("========== Pipeline completed ==========")
    
    except Exception as e:
        logger.critical(f"Pipeline failed: {e}")
        raise

if __name__ == "__main__":
    run_pipeline()