from ryser.utils import cell

def row_string(fixed, size, row, col_sep='|', padding=0):
    """
    Converts a dict of fixed cells to a string.

    fixed - a cell-symbol dictionary
    size - the dimension of the PLS
    row - the row to convert to a string
    col_sep - a string used as a separator between columns
    padding - number of spaces either side of a symbol
    """
    s = col_sep
    for col in range(size):
        symbol = fixed.get(cell(row, col, size))
        if symbol:
            s += ' '*padding + str(symbol)
        else:
            s += ' '*padding + '.'   
        s += col_sep
    return s

def dict_to_string(fixed, rows, cols, padding = 0, row_sep = '', col_sep = '', top = '', bottom = ''):
    """
    Returns a puzzle string of dimension 'boxsize' from a dictionary of 
    'fixed' cells.
    
    padding : number of spaces between adjacent symbols
    row_end : a string added to the last symbol of every row 
    col_sep : a string added to the last symbol of every column
    
    """
    s = top
    for row in rows[:-1]:
        s += f(fixed, col_sep, cols, row, row_sep, padding)
        s += row_sep
    s += f(fixed, col_sep, cols, rows[-1], row_sep, padding)
    s += ' '*padding
    s += bottom
    return s

def dict_to_string_std(fixed, rows, cols, padding = 0):
    """Returns a puzzle string of dimension 'boxsize' from a dictionary of 
    'fixed' cells with some suitably chosen row/column seperators."""
    ncols = len(cols)
    row_sep = '\n' + (2*ncols + 1)*'-' + '\n'
    col_sep = '|'
    return dict_to_string(fixed, rows, cols, padding, row_sep, col_sep, row_sep, row_sep)

def dict_to_string_xxx(fixed, nrows, ncols, padding = 0):
    rows = range(nrows)
    cols = range(ncols)
    return dict_to_string_std(fixed, rows, cols, padding)
