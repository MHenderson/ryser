# Below, 'size' is the dimension of a latin square.
# Rows and columns are labelled: 0, 1, ... , size - 1
# Cells are labelled: 1, 2, ... , size^2

def row(cell, size): 
    """The row label of the row in a latin square of dimension 'size'
    containing the cell with label 'cell'."""
    return int((cell - 1)/size) 

def col(cell, size): 
    """The column label of the column in a latin square of dimension 'size'
    containing the cell with label 'cell'."""
    return (cell - 1) % size

def row_r(cell, size): 
    """A range of all labels of cells in the same row as 'cell'."""
    return range(row(cell, size)*size + 1, (row(cell, size) + 1)*size + 1)

def col_r(cell, size): 
    """A range of all labels of cells in the same column as 'cell'."""
    return range(col(cell, size) + 1, size**2 + 1, size)

def vertex(cell, size):
    """The row and column labels of 'cell', as a pair."""
    return (row(cell, size), col(cell, size))

def list_assignment(partial_latin_square, size):
    """The (canonical) list assignment for a partial latin square. The list of
    a filled cell is the list containing just the element in that cell. The
    list of an empty cell contains only those symbols not already used in the
    same row and column as that cell."""
    P = partial_latin_square
    L = {}
    # initialise lists
    for i in range(1, size**2 + 1):
        if i in P.keys():
            L[row(i,size),col(i,size)] = [P[i]]
        else:
            L[row(i,size),col(i,size)] = range(1, size + 1)
    # update lists (remove used symbols from lists of same row/col)
    for i in range(1, size**2 + 1):
        if i in P.keys():
            # then remove P[i] from any list of a cell not in P from the same row/col
            for j in row_r(i, size) + col_r(i, size):
                if j not in P.keys():
                    if P[i] in L[row(j, size), col(j, size)]:
                        L[row(j, size), col(j, size)].remove(P[i])
    return L