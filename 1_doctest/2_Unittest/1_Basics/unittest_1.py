import unittest

class TestSplitMethod(unittest.TestCase):

    def test_split_by_default(self):
        self.assertEquals('Python Testing'.split(), ['Python', 'Testing'])
        
    def test_split_by_comma(self):
        expected = ['open', 'high', 'low', 'close']
        actual = 'open,high,low,close'.split(',')
        self.assertEquals(expected, actual)

    def test_split_by_hash(self):
        expected = ['open', 'high', 'low', 'close']
        actual = 'open#high#low#close'.split('#')
        self.assertEquals(expected, actual)
        

if __name__ == '__main__':
    unittest.main()