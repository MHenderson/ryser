# Copyright Matthew Henderson 2013.
# Created 18th December 2010.
# Last updated: Tue Mar 26 09:53:38 GMT 2013

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

    def extend(self, disjoint_fixed):
        self._P.update(disjoint_fixed)

