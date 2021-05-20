import unittest
from unittest.mock import patch
from mock12 import Programmer


class TestProgrammer(unittest.TestCase):


    def setUp(self):
        print('setting up')
        self.programmer = Programmer()
        self.programmer.add_tech('python') \
            .add_tech('sql') \
            .add_tech('java') \
            .add_tech('c++') \
            .add_tech('aws')
        
        
        
 
    
    def testAdd_tech(self):
        
        print(len(self.programmer.tech_names))

   



    @patch.object(Programmer, 'get_random_tech')
    def test_get_random_tech_mocked_python(self, mock_tech):
        mock_tech.return_value = 'python'
        actual = self.programmer.get_random_tech()
        expected = 'python'
        self.assertEqual(actual, expected)

    @patch.object(Programmer, 'get_random_tech')
    def test_get_random_tech_mocked_cpp(self, mock_tech):
        mock_tech.return_value = 'c++'
        actual = self.programmer.get_random_tech()
        expected = 'c++'
        self.assertEqual(actual, expected)

    @patch.object(Programmer, 'get_random_tech')
    def test_display_random_tech_mocked_python(self, mock_tech):        
        mock_tech.return_value = 'python'
        actual = self.programmer.display_random_tech()
        expected = 'Technology name: python'
        self.assertEqual(actual, expected)


if __name__=='__main__':
    unittest.main()