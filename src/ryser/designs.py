# Matthew Henderson, 18.12.2010 (Chandlers Ford)

from output import dict_to_string

class latin():
    """This is a component for building latin square objects."""
    def __init__(self, fixed, size):
        self.__nrows__ = size[0]
        self.__ncols__ = size[1]
        self.__fixed__ = fixed

    def __repr__(self):
        return dict_to_string(self.__fixed__, self.__nrows__, self.__ncols__, padding = 1, rowend = "\n")

    def __call__(self, row, column):
        return self.__fixed__.get((row, column))

    def nrows(self):
        return self.__nrows__

    def ncols(self):
        return self.__ncols__

class gerechte():
    pass

class sudoku():
    pass
