# Created 18th December 2010. Last updated Thu Aug  9 16:14:34 BST 2012

from ryser.output import dict_to_string_simple

class Latin:

    def __init__(self, P, size):
        self._P = P
        self._size = size

    def __str__(self):
        return dict_to_string_simple(self._P, self._size)

    def size(self):
        return self._size

    def fixed_cells(self):
        return self._P

