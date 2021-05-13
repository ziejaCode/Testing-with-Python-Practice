import unittest
from unittest.mock import patch
import mock8

class TestGetMessage(unittest.TestCase):

    @patch('mock8.get_today_name')
    def test_get_message_with_friday(self, mock_message):
        mock_message.return_value = 'Friday'
        actual = mock8.get_message()
        expected = 'Hello Friday!'
        print(actual, expected)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()