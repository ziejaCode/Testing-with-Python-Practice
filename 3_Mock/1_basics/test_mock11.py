import unittest
from mock10 import get_code_with_day
from unittest.mock import patch

class TestGetCodeWithDay(unittest.TestCase):

    @patch('mock10.get_today_name')
    @patch('random.randint')   
    def testGet_code_with_day(self, mock_code, mock_day):
        mock_code.return_value = 30
        mock_day.return_value = 'MON'      

        expected = 'CX-30-MON'
        actual = get_code_with_day()

        self.assertEqual(actual, expected)

    @patch('mock10.get_today_name')
    @patch('random.randint')   
    def testGet_code_with_Friday(self, mock_code, mock_day):
        mock_code.return_value = 20
        mock_day.return_value = 'FRI'      

        expected = 'CX-20-FRI'
        actual = get_code_with_day()

        self.assertEqual(actual, expected)




if __name__=='__main__':
    unittest.main()