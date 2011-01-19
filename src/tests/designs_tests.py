# Matthew Henderson, 18.12.2010 (Chandlers Ford)

import unittest

from ryser.designs import latin

from tests import test_data

class TestLatin(unittest.TestCase):
    """Testing of latin square components."""

    def setUp(self):
        self.P = test_data.P
        self.L = latin(self.P, (3, 3))

    def test_latin(self):
        self.assertEqual(self.L.nrows(), 3)
        self.assertEqual(self.L.ncols(), 3)
        self.assertEqual(self.L(0,2), 'c')

