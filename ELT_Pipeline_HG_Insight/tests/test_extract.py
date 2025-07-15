import unittest
import pandas as pd
from elt.extract import Extractor

class TestExtractor(unittest.TestCase):
    def test_extract_valid(self):
        extractor = Extractor('Data/customer_churn_data.csv')
        df = extractor.extract()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertFalse(df.empty)

if __name__ == '__main__':
    unittest.main()
