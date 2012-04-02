# Matthew Henderson, 2012.04.01 (Nottingham)

class Example:

  def __init__(self, P, size):
     self._P = P
     self._size = size

  def size(self):
      return self._size

  def fixed_cells(self):
      return self._P

""" 
Example 1

From "Completing Partial Latin Squares: Cropper's Question"
     by Bobga, Goldwasser, Hilton and Johnson

. . 7 3 5 . .
. . . . 6 1 5
. 6 . . . . 3
6 . . . . . .
4 . . . . . .
2 . 1 . . . .
3 4 2 . . . .
"""

eg1 = Example(
      {  3:7,  4:3,  5:5, \
        12:6, 13:1, 14:5, \
        16:6, 21:3, \
        22:6, \
        29:4, \
        36:2, 38:1, \
        43:3, 44:4, 45:2
      }, size = 7 )

"""
Example 2

6 1 2 3 . . . .
1 6 4 5 . . . .
2 4 6 1 . . . .
3 5 1 6 . . . .
. . . . 6 1 . .
. . . . 1 6 . .
. . . . . . 6 2
. . . . . . 2 6
"""


eg2 = Example(
      { 1:6,  2:1,  3:2,  4:3, \
        9:1, 10:6, 11:4, 12:5, \
       17:2, 18:4, 19:6, 20:1, \
       25:3, 26:5, 27:1, 28:6, \
       37:6, 38:1, \
       45:1, 46:6, \
       55:6, 56:2, \
       63:2, 64:6 }, size = 8 )

# Below are lists of lists of cells. Each list represents a list of subgraphs
# for which Hall's condition or the symmetric Hall condition fails. They are
# independent of the examples to aid reuse.

# fail1 is the subgraph from the paper referenced in the comment about Example
# 1. It's unlikely that this set is going to occur elsewhere so we won't attempt
# to generalise here.

fail1 = [[1,2, \
          8,9,10, \
          17, \
          23,24,25,26,27,28, \
          30,31,32,33,34,35, \
          37,39,40,41,42, \
          46,47,48,49]]

from ryser.utils import col_r
import itertools

# A first attempt at generalisation.
# Here fail2 consists of the following 4 elements from an 8 x 8 matrix labelled
# 1,..,64 across rows from top-left to bottom-right.
#   * The first 6 rows of the second last column.
#   * The first 6 rows of the last column.
#   * The first 6 rows of the last two columns.
#   * All subsets of the first 6 rows of the last two columns which contain
#     exactly 11 elements.

fail2 = [col_r(7,8)[:-2], \
         col_r(8,8)[:-2], \
         col_r(7,8)[:-2] + col_r(8,8)[:-2]] + \
        [list(x) for x in itertools.combinations(col_r(7,8)[:-2] + col_r(8,8)[:-2], 11)]

# fail3 consists of the following 7 elements:
#    * The top right block (TR) plus the top right block B1 of the
#      bottom right block (BR) as well as:
#      * all subsets we get from this set by removing a column from TR.
#    * TR minus the first column (TRmc1) plus the first row of B1.
#    * TR minus the second column (TRmc2) plus the second row of B1.

B1 = [39,40,47,48]
r1 = [5,6,7,8]
r2 = [13,14,15,16]
r3 = [21,22,23,24]
r4 = [29,30,31,32]
c2 = [6,14,22,30]
c1 = [5,13,21,29]
TR = r1 + r2 + r3 + r4
TRmc1 = [x for x in TR if x not in c1]
TRmc2 = [x for x in TR if x not in c2]

fail3 = [ B1 + r1 + r2 + r3, \
          B1 + r1 + r2 + r4, \
          B1 + r1 + r3 + r4, \
          B1 + r2 + r3 + r4, \
          B1 + r1 + r2 + r3 + r4, \
          TRmc2 + [39, 40], \
          TRmc1 + [47, 48]]

