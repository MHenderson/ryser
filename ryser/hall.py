from vizing.hall import hall_inequality_induced_by
from vizing.hall import hall_numbers as _hall_numbers_
from vizing.hall import hall_subgraph

from ryser.graphs import latin_graph, symmetric_latin_graph
from ryser.utils import list_assignment, vertex 

import matplotlib.pyplot as plt
from networkx import draw_circular as draw
from networkx import maximal_independent_set, write_graphml, write_dot

def hall_inequality_on_cells_g(graph, lists, size, cells):
    """Decide if Hall's condition is satisfied for the subgraph of the latin
    graph induced by vertices in 'cells' and list assignment given by 'lists'."""
    vertices = [vertex(cell, size) for cell in cells]
    colours = range(1, size + 1)
    return hall_inequality_induced_by(graph, lists, colours, vertices)

def hall_inequality_on_cells(partial_latin_square, cells):
    """Decide whether Hall's condition is satisfied for cells."""
    size = partial_latin_square.size()
    fixed = partial_latin_square.fixed_cells()
    graph = latin_graph(size)
    lists = list_assignment(fixed, size)
    return hall_inequality_on_cells_g(graph, lists, size, cells)

def symmetric_hall_inequality_on_cells(partial_latin_square, cells):
    """Decide whether Hall's condition is satisfied for cells in symmetric
    case."""
    size = partial_latin_square.size()
    fixed = partial_latin_square.fixed_cells()
    graph = symmetric_latin_graph(size)
    lists = list_assignment(fixed, size)
    return hall_inequality_on_cells_g(graph, lists, size, cells)   

def hall_numbers(partial_latin_square, cells):
    """Returns a list of Hall numbers for the subgraph induced by cells in
    cells."""
    size = partial_latin_square.size()
    fixed = partial_latin_square.fixed_cells()
    cell_vertices = [vertex(x, size) for x in cells]
    H = latin_graph(size).subgraph(cell_vertices)
    L = list_assignment(fixed, size)
    colours = range(1, size + 1)
    return _hall_numbers_(H, L, colours)

def symmetric_hall_numbers(partial_latin_square, cells):
    """Returns a list of Hall numbers for the subgraph induced by cells in
    cells."""
    size = partial_latin_square.size()
    fixed = partial_latin_square.fixed_cells()
    cell_vertices = [vertex(x, size) for x in cells]
    H = symmetric_latin_graph(size).subgraph(cell_vertices)
    L = list_assignment(fixed, size)
    colours = range(1, size + 1)
    return _hall_numbers_(H, L, colours)

def hall_subgraphs(partial_latin_square, cells, with_labels = False, format = 'png'):
    """Draw symmetric Hall subgraphs."""
    size = partial_latin_square.size()
    fixed = partial_latin_square.fixed_cells()
    cell_vertices = [vertex(x, size) for x in cells]
    H = symmetric_latin_graph(size).subgraph(cell_vertices)
    L = list_assignment(fixed, size)
    for i in range(1, size + 1):
      Hi = hall_subgraph(H, L, i)
      try:
        I = maximal_independent_set(Hi)
        node_color = [v in I for v in Hi.nodes()]
      except:
        node_color = Hi.nodes()
      if Hi.number_of_nodes() > 0:
        if format == 'png':
          draw(Hi, node_color = node_color, with_labels = with_labels)
          plt.savefig("graph" + str(i) + ".png")
          plt.clf()
        elif format == 'graphml':
          write_graphml(Hi, "graph" + str(i) + ".graphml")
        elif format == 'dot':
          write_dot(Hi, "graph" + str(i) + ".dot")
        else:
          raise "No such format"

