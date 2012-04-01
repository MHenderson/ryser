# Matthew Henderson, 2012.04.01 (Nottingham)

import unittest

from ryser.examples import Example1, Example2

from ryser.hall import hall_inequality_on_cells
from ryser.hall import symmetric_hall_inequality_on_cells

class TestHallConditionOnCells(unittest.TestCase):

    def __test_hall_inequality_on_cells(self, P, size, failing, passing):
        """This is a convenience for testing Hall's inequality on a partial
        latin square 'P' of size 'size'. The parameter 'failing' is a list
        of lists of cells, each of which represents a subgraph on which
        Hall's condition fails. The parameter 'passing' is a list of lists
        off cells for which Hall's condition passes."""
        for cells in failing:
            self.assertFalse(hall_inequality_on_cells(P, size, cells))
        for cells in passing:
            self.assertTrue(hall_inequality_on_cells(P, size, cells))

    def test_hall_inequality_on_cells(self):
        """Test function for testing Hall's inequality on cells."""
        eg1 = Example1()
        self.__test_hall_inequality_on_cells(eg1.P, eg1.size, eg1.bad_cells,
                                             [])
        eg2 = Example2()
        self.__test_hall_inequality_on_cells(eg2.P, eg2.size, eg2.bad_cells,
                                             eg2.symmetric_bad_cells)

class TestSymmetricHallConditionOnCells(unittest.TestCase):

    def __test_symmetric_hall_inequality_on_cells(self, P, size, failing,
                                                  passing):
        """This is a convenience for testing Hall's symmetric inequality on a
        partial latin square 'P' of size 'size'. The parameter 'failing' is a
        list of lists of cells, each of which represents a subgraph on which
        Hall's condition fails. The parameter 'passing' is a list of lists
        off cells for which Hall's condition passes."""

        for cells in failing:
            self.assertFalse(symmetric_hall_inequality_on_cells(P, size, cells))
        for cells in passing:
            self.assertTrue(symmetric_hall_inequality_on_cells(P, size, cells))

    def test_symmetric_hall_inequality_on_cells(self):
        """Test function for testing Hall's symmetric inequality on cells."""
        eg2 = Example2()
        self.__test_symmetric_hall_inequality_on_cells(eg2.P, eg2.size,
                                                       eg2.bad_cells, [])

if __name__ == '__main__':
    unittest.main()

