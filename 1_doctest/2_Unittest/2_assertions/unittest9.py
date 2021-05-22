import unittest


class TestLstripMethod(unittest.TestCase):
    """ disc """

    def test_lstrip(self):
        txt = '   mela'
        self.assertEqual(txt.lstrip(), 'mela')

    def test_rstrip(self):
        txt = 'mela     '
        self.assertEqual(txt.rstrip(), 'mela')

    def test_strip(self):
        txt = '    mela     '
        self.assertEqual(txt.strip(), 'mela')


if __name__=='__main__':
    unittest.main()