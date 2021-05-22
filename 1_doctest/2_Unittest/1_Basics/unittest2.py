import unittest

class TestJoinMethod(unittest.TestCase):
    """ Description """

    def test_join_with_space(self  ):
        self.assertEqual(' '.join(['Mariola', 'Janek']), 'Mariola Janek')

    def test_join_with_comma(self):
        self.assertEqual(','.join(['Mariola', 'Janek']), 'Mariola,Janek')

    def test_join_with_new_line_char(self):
        self.assertEqual('\n'.join(['Mariola', 'Janek']), 'Mariola\nJanek')

if __name__=='__main__':
    unittest.main()