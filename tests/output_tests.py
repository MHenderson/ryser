# Matthew Henderson, 18.12.2010 (Chandlers Ford)

import unittest

from ryser.output import dict_to_string, dict_to_string_std, row_string
from ryser.examples import eg1

class TestRowString(unittest.TestCase):
    """Testing of row to string."""

    def setUp(self):
        pass

    def test_row_string(self):
        self.assertEqual(row_string(eg1.fixed_cells(), 7, 0),'|.|.|7|3|5|.|.|')
        self.assertEqual(row_string(eg1.fixed_cells(), 7, 1),'|.|.|.|.|6|1|5|')
        self.assertEqual(row_string(eg1.fixed_cells(), 7, 2),'|.|6|.|.|.|.|3|')
        self.assertEqual(row_string(eg1.fixed_cells(), 7, 3),'|6|.|.|.|.|.|.|')
        self.assertEqual(row_string(eg1.fixed_cells(), 7, 4),'|4|.|.|.|.|.|.|')
        self.assertEqual(row_string(eg1.fixed_cells(), 7, 5),'|2|.|1|.|.|.|.|')
        self.assertEqual(row_string(eg1.fixed_cells(), 7, 6),'|3|4|2|.|.|.|.|')

class TestDictToString(unittest.TestCase):
    """Testing of string conversion."""

    def setUp(self):
        pass

    def test_dict_to_string(self):
        pass

class TestDictToStringStd(unittest.TestCase):
    """Testing of string conversion."""

    def setUp(self):
        pass

    def test_dict_to_string_std(self):
        pass
