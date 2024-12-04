import ryser as ry

def test_pls_list_colouring_problem():
  F = {1:1, 2:2, 6:1}
  G = ry.pls_list_colouring_problem(F, 3)
  assert list(G.nodes()) == [0, 1, 2]
  assert list(G.edges(data = True)) == [(0, 1, {'permissible': [2]}), (0, 2, {'permissible': [3]}), (0, 0, {'permissible': [1]}), (1, 0, {'permissible': [2, 3]}), (1, 2, {'permissible': [1]}), (1, 1, {'permissible': [3]}), (2, 0, {'permissible': [2, 3]}), (2, 1, {'permissible': [1, 3]}), (2, 2, {'permissible': [2, 3]})]
