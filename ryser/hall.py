from vizing.hall import hall_inequality_induced_by
from vizing.hall import hall_number

from ryser.graphs import latin_graph, symmetric_latin_graph
from ryser.utils import list_assignment, vertex 

def hall_inequality_on_cells_g(graph, lists, size, cells):
    """Decide if Hall's condition is satisfied for the subgraph of the latin
    graph induced by vertices in 'cells' with the usual list assignment for
    partial latin squares."""
    vertices = [vertex(cell, size) for cell in cells]
    colors = range(1, size + 1)
    return hall_inequality_induced_by(graph, lists, colors, vertices)

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

def hall_numbers(partial_latin_square, size, cells):
    """Returns a list of Hall numbers for the subgraph induced by cells in
    cells.
    TODO: Implement hall_numbers in vizing and then rewrite this function."""
    cell_vertices = [vertex(x, size) for x in cells]
    H = symmetric_latin_graph(size).subgraph(cell_vertices)
    L = list_assignment(partial_latin_square, size)
    colours = range(1, size + 1)
    hall_numbers = [hall_number(H, L, c) for c in colours]
    return hall_numbers

