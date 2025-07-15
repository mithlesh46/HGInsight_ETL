import os
from dotenv import load_dotenv

class Config:
    def __init__(self, env_path: str = '.env'):
        load_dotenv(env_path)
        self.data_path = os.getenv('DATA_PATH', 'Data/customer_churn_data.csv')
        self.db_url = os.getenv('DB_URL', 'sqlite:///elt_pipeline.db')
        self.staging_table = os.getenv('STAGING_TABLE', 'staging')
        self.reporting_table = os.getenv('REPORTING_TABLE', 'reporting')
        self.pii_columns = os.getenv('PII_COLUMNS', 'Name,Email').split(',')
        self.missing_defaults = eval(os.getenv('MISSING_DEFAULTS', '{}'))
