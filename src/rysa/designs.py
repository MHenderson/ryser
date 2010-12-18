# Matthew Henderson, 18.12.2010 (Chandlers Ford)

class latin():

    def __init__(self, fixed, size):
        self.__size__ = size
        self.__fixed__ = fixed

    def __call__(self, row, column):
        return self.__fixed__.get((row, column))

    def size(self):
        return self.__size__

class gerechte():
    pass

class sudoku():
    pass

