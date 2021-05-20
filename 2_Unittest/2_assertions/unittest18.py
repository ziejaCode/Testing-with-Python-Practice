import unittest


class StringListOnly(list):

    def append(self, string):
        if not isinstance(string, str):
            raise TypeError('Only object of type str can be added to the list.')
        super().append(string)



class TestStringListOnly1(unittest.TestCase):

    def test_append_string(self):
        slo = StringListOnly()
        slo.append('test')        
        self.assertIn('test', slo)

    def test_append_not_string_should_raise_error(self):
        slo = StringListOnly()
        not_string_1 = [1,2]
        not_string_2 = True
        slo.append(not_string_1)
        slo.append(not_string_2)        
        self.assertIn(TypeError, slo.append, not_string_1)
        self.assertIn(TypeError, slo.append, not_string_2)


class TestStringListOnly(unittest.TestCase):
 
    def test_append_string(self):
        slo = StringListOnly()
        string = 'big_data'
        slo.append(string)
        self.assertIn(string, slo)
 
    def test_append_not_string_should_raise_error(self):
        slo = StringListOnly()
        not_string_1 = ['big_data']
        not_string_2 = 'True'
        self.assertRaises(TypeError, slo.append, not_string_1)
        self.assertRaises(TypeError, slo.append, not_string_2)


if __name__ == '__main__':
    unittest.main()