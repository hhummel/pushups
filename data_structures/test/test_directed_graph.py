def test_vertex():
    from directed_graph import Graph

    g = Graph()
    g.add_vertex(0)
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)

    assert len(g.vertices) == 4
    assert len(g.edges) == 4
    assert len(g.edges[0]) == 4

def test_edges():
    from directed_graph import Graph

    g = Graph()
    g.add_vertex(0)
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)


    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)

    assert g.edges == [[0, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

def test_dfs():
    from directed_graph import Graph
    g = Graph()
    g.add_vertex(0)
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)

    g.add_edge(1, 0)
    g.add_edge(2, 0)
    g.add_edge(3, 0)

    assert g.dfs() == ['0']

    g = Graph()
    g.add_vertex(0)
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_vertex(4)
    g.add_vertex(5)
    g.add_vertex(6)

    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(5, 5)
    g.add_edge(6, 6)

    assert g.dfs() == ['0', '1', '3', '4', '2']

def test_bfs():
    from directed_graph import Graph
    g = Graph()
    g.add_vertex(0)
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)

    g.add_edge(1, 0)
    g.add_edge(2, 0)
    g.add_edge(3, 0)

    assert g.bfs() == ['0']

    g = Graph()
    g.add_vertex(0)
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_vertex(4)
    g.add_vertex(5)
    g.add_vertex(6)

    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(5, 2)
    g.add_edge(6, 2)

    assert g.bfs() == ['0', '1', '2', '3', '4']


def test_delete():
    from directed_graph import Graph
    g = Graph()
    g.add_vertex(0)
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)

    g.add_edge(1, 0)
    g.add_edge(2, 0)
    g.add_edge(3, 0)

    g.delete_vertex(2)
    assert [x.value for x in g.vertices] == [0, 1, 3]
    assert g.edges == [[0, 0, 0], [1, 0, 0], [1, 0, 0]]

    g = Graph()
    g.add_vertex(0)
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_vertex(4)
    g.add_vertex(5)
    g.add_vertex(6)

    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(5, 2)
    g.add_edge(6, 2)

    result = g.topologic_sort()
    assert result == [6, 5, 0, 1, 4, 3, 2]
