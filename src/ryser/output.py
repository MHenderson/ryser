def dict_to_string(fixed, nrows, ncols, padding = 0, row_sep = '', col_sep = ''):
    """
    Returns a puzzle string of dimension 'boxsize' from a dictionary of 
    'fixed' cells.
    
    padding : number of spaces between adjacent symbols
    row_end : a string added to the last symbol of every row 
    col_sep : a string added to the last symbol of every column
    
    """
    s = row_sep
    for row in range(nrows):
        s += col_sep
        for col in range(ncols):
            symbol = fixed.get((row, col))
            if symbol:
                s += ' '*padding + symbol
            else:
                s += ' '*padding + '.'   
            s += col_sep
        s += row_sep
    s += ' '*padding
    return s

def dict_to_string_std(fixed, nrows, ncols, padding = 0):
    """Returns a puzzle string of dimension 'boxsize' from a dictionary of 
    'fixed' cells with some suitably chosen row/column seperators."""
    row_sep = '\n' + (2*ncols + 1)*'-' + '\n'
    col_sep = '|'
    return dict_to_string(fixed, nrows, ncols, padding, row_sep, col_sep)
