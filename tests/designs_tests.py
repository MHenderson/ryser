# Matthew Henderson, 18.12.2010 (Chandlers Ford)

import unittest

from ryser.designs import latin

from tests import test_data
        
P = { (0,0): 'a', (0,1): 'b', (0,2): 'c', \
      (1,0): 'b', (1,1): 'c', (1,2): 'a', \
      (2,0): 'c', (2,1): 'a', (2,2): 'b' }

L = latin(P, (3, 3))

class TestLatin(unittest.TestCase):
    """Testing of latin square components."""

    def setUp(self):
        pass

    def test_latin(self):
        self.assertEqual(L.nrows(), 3)
        self.assertEqual(L.ncols(), 3)
        self.assertEqual(L(0,2), 'c')
