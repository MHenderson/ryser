from vizing.hall import hall_inequality_induced_by

from ryser.graphs import latin_graph, symmetric_latin_graph
from ryser.utils import list_assignment, vertex 

def hall_inequality_on_cells_g(graph, lists, size, cells):
    """Decide if Hall's condition is satisfied for the subgraph of the latin
    graph induced by vertices in 'cells' with the usual list assignment for
    partial latin squares."""
    vertices = [vertex(cell, size) for cell in cells]
    colors = range(1, size + 1)
    return hall_inequality_induced_by(graph, lists, colors, vertices)

###########################################################################
# Convenience versions of halls_condition_on_cells_g. Incorporating graph
# construction.
###########################################################################

def hall_inequality_on_cells(partial_latin_square, size, cells):
    """Decide whether Hall's condition is satisfied for cells."""
    graph = latin_graph(size)
    lists = list_assignment(partial_latin_square, size)
    return hall_inequality_on_cells_g(graph, lists, size, cells)

def symmetric_hall_inequality_on_cells(partial_latin_square, size, cells):
    """Decide whether Hall's condition is satisfied for cells in symmetric
    case."""
    graph = symmetric_latin_graph(size)
    lists = list_assignment(partial_latin_square, size)
    return hall_inequality_on_cells_g(graph, lists, size, cells)   
