import unittest


def calculate_daily_return(open, close):
    return round((close / open - 1) * 100, 2)

print(calculate_daily_return(12, 34))

class TestCalculateDailyReturn(unittest.TestCase):

    def test_positive_return(self):
        self.assertEqual(calculate_daily_return(350.00, 360.00), 3.15)

    def test_negative_return(self):
        self.assertEqual(calculate_daily_return(349.00, 340.00), -2.58)

    def test_zero_return(self):
        self.assertEqual(calculate_daily_return(349.00, 349.00), 0.00)

    

if __name__=='__main__':
    unittest.main()
