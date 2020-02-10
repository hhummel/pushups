def test_vertex():
    from graphs.non_directed_graph import Graph

    g = Graph()
    g.add_vertex(0)
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)

    assert len(g.vertices) == 4
    assert len(g.edges) == 4
    assert len(g.edges[0]) == 4

def test_edges():
    from graphs.non_directed_graph import Graph

    g = Graph()
    g.add_vertex(0)
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)


    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)

    assert g.edges == [[0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]

def test_dfs():
    from graphs.non_directed_graph import Graph
    g = Graph()
    g.add_vertex(0)
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)

    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)

    assert g.dfs() == ['0', '1', '2', '3']

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
    g.add_edge(2, 5)
    g.add_edge(2, 6)

    assert g.dfs() == ['0', '1', '3', '4', '2', '5', '6']


def test_bfs():
    from graphs.non_directed_graph import Graph
    g = Graph()
    g.add_vertex(0)
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)

    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)

    assert g.bfs() == ['0', '1', '2', '3']

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
    g.add_edge(2, 5)
    g.add_edge(2, 6)

    assert g.bfs() == ['0', '1', '2', '3', '4', '5', '6']



