import pandas as pd
from src.utils import setup_logger
from config import RAW_DATA_PATH

logger = setup_logger(__name__)

def read_csv(filename):
    filepath = RAW_DATA_PATH + filename
    logger.info(f"Starting extract from {filepath}")
    
    try:
        df = pd.read_csv(filepath)
        logger.info(f"Successfully extracted {len(df)} rows from {filename}")
        return df
    
    except FileNotFoundError:
        logger.error(f"File not found: {filepath}")
        raise
    
    except Exception as e:
        logger.critical(f"Unexpected error while reading {filename}: {e}")
        raise