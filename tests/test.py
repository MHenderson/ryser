"""
Unit testing of the automatic batch processing application
"""
import unittest
import ryser
 
class LatinTests(unittest.TestCase):
    def test_app(self):
        """Simple Tests"""
        a = ryser.Latin({1:1, 12:3}, 9)
        self.assertEqual(a.fixed_cells(), {1:1, 12:3})
 
def suite():
    _suite = unittest.TestSuite()
    _suite.addTest(LatinTests('test_app'))
    return _suite
