import unittest


def calculate_daily_return(open, close):
    return round((close / open - 1) * 100, 2)

print(calculate_daily_return(12, 34))

class TestCalculateDailyReturn(unittest.TestCase):
    pass
