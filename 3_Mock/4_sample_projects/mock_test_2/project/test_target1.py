from unittest import TestCase
import target1

class TestExamples(TestCase):
    def test_print_contents_of_cwd_success(self):
        actual_result = target1.print_content_of_cwd()
        print('this is result ', actual_result)
        expected_directory = b'tests'
        self.assertIn(expected_directory, actual_result)


if __name__=='__main__()':
    unittest.main()

