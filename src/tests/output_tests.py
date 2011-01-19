# Matthew Henderson, 18.12.2010 (Chandlers Ford)

import unittest

from ryser.output import dict_to_string, dict_to_string_std

from tests.test_data import P

class TestDictToString(unittest.TestCase):
    """Testing of string conversion."""

    def setUp(self):
        pass

    def test_dict_to_string(self):
        self.assertEqual(dict_to_string(P, 3, 3, padding = 0), 'abcbcacab')
        self.assertEqual(dict_to_string(P, 3, 3, padding = 1), ' a b c b c a c a b ')
        self.assertEqual(dict_to_string(P, 3, 3, padding = 2), '  a  b  c  b  c  a  c  a  b  ')
        
class TestDictToStringStd(unittest.TestCase):
    """Testing of string conversion."""

    def setUp(self):
        pass

    def test_dict_to_string_std(self):
#        self.assertEqual(dict_to_string_std(P, 3, 3, padding = 0), 'abcbcacab')
        pass



