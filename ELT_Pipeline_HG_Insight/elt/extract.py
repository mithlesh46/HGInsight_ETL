import pandas as pd
import logging
from typing import Optional

class Extractor:
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.logger = logging.getLogger(__name__)

    def extract(self) -> Optional[pd.DataFrame]:
        try:
            df = pd.read_csv(self.data_path)
            self.logger.info(f"Successfully extracted data from {self.data_path}")
            return df
        except Exception as e:
            self.logger.error(f"Failed to extract data: {e}")
            return None
