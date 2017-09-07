import utils


def test_index_to_node():
    assert utils.index_to_node(1, 1, 4) == 1
    assert utils.index_to_node(2, 1, 4) == 5
    assert utils.index_to_node(3, 3, 4) == 11


def test_node_to_index():
    assert utils.node_to_index(1, 4) == (1, 1)
    assert utils.node_to_index(16, 4) == (4, 4)
    assert utils.node_to_index(5, 4) == (2, 1)
    assert utils.node_to_index(9, 4) == (3, 1)
    assert utils.node_to_index(13, 4) == (4, 1)
    assert utils.node_to_index(4, 4) == (1, 4)
    assert utils.node_to_index(1, 3) == (1, 1)
    assert utils.node_to_index(2, 3) == (1, 2)
    assert utils.node_to_index(3, 3) == (1, 3)
    assert utils.node_to_index(4, 3) == (2, 1)
    assert utils.node_to_index(5, 3) == (2, 2)
    assert utils.node_to_index(6, 3) == (2, 3)
    assert utils.node_to_index(7, 3) == (3, 1)
    assert utils.node_to_index(8, 3) == (3, 2)
    assert utils.node_to_index(9, 3) == (3, 3)
