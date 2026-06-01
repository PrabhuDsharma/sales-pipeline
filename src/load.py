import pandas as pd
from src.utils import setup_logger
from config import PROCESSED_DATA_PATH, OUTPUT_DATA_PATH

logger = setup_logger(__name__)

def save_processed(df, filename):
    logger.info(f"Saving processed data to {PROCESSED_DATA_PATH}{filename}")
    
    try:
        filepath = PROCESSED_DATA_PATH + filename
        df.to_csv(filepath, index=False)
        logger.info(f"Saved {len(df)} rows to {filename}")
    
    except Exception as e:
        logger.error(f"Failed to save processed data: {e}")
        raise


def save_output(df, filename):
    logger.info(f"Saving output to {OUTPUT_DATA_PATH}{filename}")
    
    try:
        filepath = OUTPUT_DATA_PATH + filename
        df.to_csv(filepath, index=False)
        logger.info(f"Output saved successfully: {filename}")
    
    except Exception as e:
        logger.error(f"Failed to save output: {e}")
        raise