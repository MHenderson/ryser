import unittest

from ryser.hall import hall_inequality_on_cells
from ryser.hall import symmetric_hall_inequality_on_cells

##########################################
# Testing of Hall's condition on cells
##########################################

# Example from
# "Completing Partial Latin Squares: Cropper's Question"
#              by Bobga, Goldwasser, Hilton and Johnson

# . . 7 3 5 . . 
# . . . . 6 1 5
# . 6 . . . . 3
# 6 . . . . . .
# 4 . . . . . . 
# 2 . 1 . . . .
# 3 4 2 . . . .

size__ = 7

P__ = {  3:7,  4:3,  5:5, \
      12:6, 13:1, 14:5, \
      16:6, 21:3, \
      22:6, \
      29:4, \
      36:2, 38:1, \
      43:3, 44:4, 45:2 }

bad_cells__ = [1,2, \
             8,9,10, \
             17, \
             23,24,25,26,27,28, \
             30,31,32,33,34,35, \
             37,39,40,41,42, \
             46,47,48,49]

# Example of symmetric latin square.
#
# 6 1 2 3 . . . .
# 1 6 4 5 . . . .
# 2 4 6 1 . . . . 
# 3 5 1 6 . . . . 
# . . . . 6 1 . . 
# . . . . 1 6 . .
# . . . . . . 6 2
# . . . . . . 2 6

size = 8

P = { 1:6,  2:1,  3:2,  4:3, \
      9:1, 10:6, 11:4, 12:5, \
     17:2, 18:4, 19:6, 20:1, \
     25:3, 26:5, 27:1, 28:6, \
     37:6, 38:1, \
     45:1, 46:6, \
     55:6, 56:2, \
     63:2, 64:6 }

# The cells in 'all_bad_cells' fail both the symmetric and normal Hall's condition

all_bad_cells = [[39, 47, 7, 15, 23, 31], \
                 [40, 48, 8, 16, 24, 32], \
                 [39, 40, 47, 7, 8, 15, 16, 23, 24, 31, 32],  \
                 [39, 40, 48, 7, 8, 15, 16, 23, 24, 31, 32],  \
                 [39, 47, 48, 7, 8, 15, 16, 23, 24, 31, 32],  \
                 [40, 47, 48, 7, 8, 15, 16, 23, 24, 31, 32],  \
                 [39, 40, 47, 48, 7, 8, 15, 16, 23, 24, 31],  \
                 [39, 40, 47, 48, 7, 8, 15, 16, 23, 24, 32],  \
                 [39, 40, 47, 48, 7, 8, 15, 16, 23, 31, 32],  \
                 [39, 40, 47, 48, 7, 8, 15, 16, 24, 31, 32],  \
                 [39, 40, 47, 48, 7, 8, 15, 23, 24, 31, 32],  \
                 [39, 40, 47, 48, 7, 8, 16, 23, 24, 31, 32],  \
                 [39, 40, 47, 48, 7, 15, 16, 23, 24, 31, 32], \
                 [39, 40, 47, 48, 8, 15, 16, 23, 24, 31, 32], \
                 [39, 40, 47, 48, 7, 8, 15, 16, 23, 24, 31, 32]]

# The cells in 'more_bad_cells' only fail the symmetric Hall condition.

more_bad_cells = [[39, 40, 47, 48, 5, 6, 7, 8, 13, 14, 15, 16, 21, 22, 23, 24], \
                  [29, 31, 32, 39, 40, 5, 7, 8, 13, 15, 16, 21, 23, 24], \
                  [30, 31, 32, 47, 48, 6, 7, 8, 14, 15, 16, 22, 23, 24], \
                  [29, 30, 31, 32, 39, 40, 47, 48, 5, 6, 7, 8, 13, 14, 15, 16], \
                  [29, 30, 31, 32, 39, 40, 47, 48, 5, 6, 7, 8, 21, 22, 23, 24], \
                  [29, 30, 31, 32, 39, 40, 47, 48, 13, 14, 15, 16, 21, 22, 23, 24], \
                  [29, 30, 31, 32, 39, 40, 47, 48, 5, 6, 7, 8, 13, 14, 15, 16, 21, 22, 23, 24]]

class TestHallConditionOnCells(unittest.TestCase):
    def test_hall_inequality_on_cells(self):
        self.assertFalse(hall_inequality_on_cells(P__, size__, bad_cells__))    
        for bad_cells in all_bad_cells:
            self.assertFalse(hall_inequality_on_cells(P, size, bad_cells))
        for bad_cells in more_bad_cells:
            self.assertTrue(hall_inequality_on_cells(P, size, bad_cells))

class TestSymmetricHallConditionOnCells(unittest.TestCase):
    def test_symmetric_hall_inequality_on_cells(self):
        for bad_cells in all_bad_cells:
            self.assertFalse(symmetric_hall_inequality_on_cells(P, size, bad_cells))
        for bad_cells in more_bad_cells:
            self.assertFalse(symmetric_hall_inequality_on_cells(P, size, bad_cells))

if __name__ == '__main__':
    unittest.main()

