import unittest

class TestUpper(unittest.TestCase):
    """ desc """
    def test_upper(self):
        self.assertEqual('summer'.upper(), 'SUMMER')
    
    def test_isUpper(self):
        self.assertTrue('SUMMER'.isupper())
    
    def test_isNotUpper(self):
        self.assertFalse('summer'.isupper())



if __name__=='__main__':
    unittest.main()
