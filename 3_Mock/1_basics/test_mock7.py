import unittest
from mock7 import get_code
from unittest import TestCase
from unittest.mock import patch

class TestGetCode(TestCase):
    @patch('random.randint')
    def test_get_code_mock_should_return_30(self, mock_random):
        mock_random.return_value = 30
        actual = get_code()
        expected = 'CX-30'
        print(actual, expected) # test
        self.assertEqual(actual, expected)


if __name__=='__main__':
    unittest.main()