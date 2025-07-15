import unittest
import pandas as pd
from elt.extract import Extractor
from elt.load import Loader
from elt.transform import Transformer

class TestPipeline(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'Name': ['Alice', 'Bob'],
            'Email': ['alice@example.com', 'bob@example.com'],
            'Age': [25, 30]
        })
        self.loader = Loader('sqlite:///:memory:')
        self.transformer = Transformer()

    def test_full_pipeline(self):
        # Load to staging
        self.assertTrue(self.loader.load_to_staging(self.df, 'staging'))
        # Transform
        defaults = {'Name': 'Unknown', 'Email': 'unknown@example.com', 'Age': 0}
        df_filled = self.transformer.handle_missing(self.df, defaults)
        df_anon = self.transformer.anonymize_pii(df_filled, ['Name', 'Email'])
        # Load to reporting
        self.assertTrue(self.loader.load_to_reporting(df_anon, 'reporting'))

if __name__ == '__main__':
    unittest.main()
