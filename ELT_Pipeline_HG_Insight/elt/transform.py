import pandas as pd
import logging
from faker import Faker
from typing import Optional

class Transformer:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.faker = Faker()

    def handle_missing(self, df: pd.DataFrame, defaults: dict) -> pd.DataFrame:
        try:
            df_filled = df.fillna(defaults)
            self.logger.info("Handled missing values with defaults.")
            return df_filled
        except Exception as e:
            self.logger.error(f"Error handling missing values: {e}")
            return df

    def anonymize_pii(self, df: pd.DataFrame, pii_columns: list) -> pd.DataFrame:
        try:
            df_copy = df.copy()
            for col in pii_columns:
                if col in df_copy.columns:
                    df_copy[col] = [self.faker.name() if 'name' in col.lower() else self.faker.email() for _ in range(len(df_copy))]
            self.logger.info(f"Anonymized PII columns: {pii_columns}")
            return df_copy
        except Exception as e:
            self.logger.error(f"Error anonymizing PII: {e}")
            return df
