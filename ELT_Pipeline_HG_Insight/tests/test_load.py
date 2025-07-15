import unittest
import pandas as pd
from elt.load import Loader

class TestLoader(unittest.TestCase):
    def setUp(self):
        self.loader = Loader('sqlite:///:memory:')
        self.df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})

    def test_load_to_staging(self):
        result = self.loader.load_to_staging(self.df, 'staging')
        self.assertTrue(result)

    def test_load_to_reporting(self):
        result = self.loader.load_to_reporting(self.df, 'reporting')
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
