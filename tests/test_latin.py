import ryser
 
def test_latin():
    a = ryser.Latin({1:1, 12:3}, 9)
    assert a.fixed_cells() == {1:1, 12:3}
