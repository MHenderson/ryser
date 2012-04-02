# Matthew Henderson, 2012.04.01 (Nottingham)

import unittest

from ryser.examples import eg1, eg2, eg3, eg4
from ryser.examples import fail1, fail2, fail3, fail4

from ryser.hall import hall_inequality_on_cells
from ryser.hall import symmetric_hall_inequality_on_cells

class TestHallConditionOnCells(unittest.TestCase):

    def __assert_false_hall_inequality_on_cells(self, P, size, lcells):
        for cells in lcells:
            self.assertFalse(hall_inequality_on_cells(P, size, cells))

    def __assert_true_hall_inequality_on_cells(self, P, size, lcells):
        for cells in lcells:
            self.assertTrue(hall_inequality_on_cells(P, size, cells))

    def __assert_true_hall_inequality_on_example(self, example, lcells):
        return self.__assert_true_hall_inequality_on_cells(example.fixed_cells(),
                                                           example.size(),
                                                           lcells)

    def __assert_false_hall_inequality_on_example(self, example, lcells):
        return self.__assert_false_hall_inequality_on_cells(example.fixed_cells(),
                                                            example.size(),
                                                            lcells)

    def test_hall_inequality_on_cells(self):
        """Test function for testing Hall's inequality on cells."""
        self.__assert_false_hall_inequality_on_example(eg1, fail1)
        self.__assert_false_hall_inequality_on_example(eg2, fail2)
        self.__assert_true_hall_inequality_on_example(eg2, fail3)
        self.__assert_true_hall_inequality_on_example(eg3, fail4)
        self.__assert_true_hall_inequality_on_example(eg4, fail4)

class TestSymmetricHallConditionOnCells(unittest.TestCase):


    def __assert_false_symmetric_hall_inequality_on_cells(self, P, size, lcells):
        for cells in lcells:
            self.assertFalse(symmetric_hall_inequality_on_cells(P, size, cells))

    def __assert_true_symmetric_hall_inequality_on_cells(self, P, size, lcells):
        for cells in lcells:
            self.assertTrue(symmetric_hall_inequality_on_cells(P, size, cells))

    def __assert_true_symmetric_hall_inequality_on_example(self, example, lcells):
        return self.__assert_true_symmetric_hall_inequality_on_cells(example.fixed_cells(),
                                                           example.size(),
                                                           lcells)

    def __assert_false_symmetric_hall_inequality_on_example(self, example, lcells):
        return self.__assert_false_symmetric_hall_inequality_on_cells(example.fixed_cells(),
                                                            example.size(),
                                                            lcells)

    def test_symmetric_hall_inequality_on_cells(self):
        """Test function for testing Hall's symmetric inequality on cells."""
        self.__assert_true_symmetric_hall_inequality_on_example(eg1, fail1)
        self.__assert_false_symmetric_hall_inequality_on_example(eg2, fail2)
        self.__assert_false_symmetric_hall_inequality_on_example(eg2, fail3)
        self.__assert_false_symmetric_hall_inequality_on_example(eg3, fail4)
        self.__assert_false_symmetric_hall_inequality_on_example(eg4, fail4)

if __name__ == '__main__':
    unittest.main()

