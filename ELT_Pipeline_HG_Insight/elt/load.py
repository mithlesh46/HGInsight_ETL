import logging
import pandas as pd
from sqlalchemy import create_engine
from typing import Optional

class Loader:
    def __init__(self, db_url: str):
        self.db_url = db_url
        self.engine = create_engine(db_url)
        self.logger = logging.getLogger(__name__)

    def load_to_staging(self, df: pd.DataFrame, table_name: str = 'staging') -> bool:
        try:
            df.to_sql(table_name, self.engine, if_exists='replace', index=False)
            self.logger.info(f"Loaded data to staging table: {table_name}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to load data to staging: {e}")
            return False

    def load_to_reporting(self, df: pd.DataFrame, table_name: str = 'reporting') -> bool:
        try:
            df.to_sql(table_name, self.engine, if_exists='replace', index=False)
            self.logger.info(f"Loaded data to reporting table: {table_name}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to load data to reporting: {e}")
            return False
