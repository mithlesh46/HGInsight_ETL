import unittest
import pandas as pd
from elt.transform import Transformer

class TestTransformer(unittest.TestCase):
    def setUp(self):
        self.transformer = Transformer()
        self.df = pd.DataFrame({
            'Name': ['Alice', None],
            'Email': ['alice@example.com', None],
            'Age': [25, None]
        })

    def test_handle_missing(self):
        defaults = {'Name': 'Unknown', 'Email': 'unknown@example.com', 'Age': 0}
        df_filled = self.transformer.handle_missing(self.df, defaults)
        self.assertFalse(df_filled.isnull().values.any())

    def test_anonymize_pii(self):
        pii_columns = ['Name', 'Email']
        df_anon = self.transformer.anonymize_pii(self.df, pii_columns)
        self.assertNotEqual(df_anon['Name'][0], 'Alice')
        self.assertNotEqual(df_anon['Email'][0], 'alice@example.com')

if __name__ == '__main__':
    unittest.main()
