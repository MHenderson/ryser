# Matthew Henderson, 18.12.2010 (Chandlers Ford)

import unittest

import rysa.designs

class TestLatin(unittest.TestCase):

    def setUp(self):
        self.P = { (0,0): 'a', (0,1): 'b', (0,2): 'c', \
                   (1,0): 'b', (1,1): 'c', (1,2): 'a', \
                   (2,0): 'c', (2,1): 'a', (2,2): 'b' }
        self.L = rysa.designs.latin(self.P, (3, 3))

    def test_latin(self):
        self.assertEqual(self.L.size(), (3, 3))
        self.assertEqual(self.L(0,2), 'c')

