def test_get_paths():
    from  graphs.dijkstra import Dijkstra

    dijkstra = Dijkstra()

    dijkstra.graph.add_vertex(0)
    dijkstra.graph.add_vertex(1)
    dijkstra.graph.add_vertex(2)
    dijkstra.graph.add_vertex(3)
    dijkstra.graph.add_vertex(4)
    dijkstra.graph.add_vertex(5)
    dijkstra.graph.add_vertex(6)

    dijkstra.graph.add_edge(0, 1, 10)
    dijkstra.graph.add_edge(0, 2, 20)
    dijkstra.graph.add_edge(0, 3, 30)
    dijkstra.graph.add_edge(1, 2, 10)
    dijkstra.graph.add_edge(1, 3, 40)
    dijkstra.graph.add_edge(1, 4, 50)
    dijkstra.graph.add_edge(2, 4, 50)
    dijkstra.graph.add_edge(2, 5, 20)
    dijkstra.graph.add_edge(2, 6, 60)
    dijkstra.graph.add_edge(3, 4, 60)
    dijkstra.graph.add_edge(3, 5, 10)
    dijkstra.graph.add_edge(4, 5, 5)
    dijkstra.get_paths(0)
    result_0 = dijkstra.show_paths()

    assert result_0 == [(0, 0), (0, 10), (0, 20), (0, 30), (5, 45), (2, 40), (2, 80)]

def test_get_isolated_paths():
    from  graphs.dijkstra import Dijkstra

    dijkstra = Dijkstra()

    dijkstra.graph.add_vertex(0)
    dijkstra.graph.add_vertex(1)
    dijkstra.graph.add_vertex(2)
    dijkstra.graph.add_vertex(3)
    dijkstra.graph.add_vertex(4)
    dijkstra.graph.add_vertex(5)
    dijkstra.graph.add_vertex(6)
    dijkstra.graph.add_vertex(7)
    dijkstra.graph.add_vertex(8)

    dijkstra.graph.add_edge(0, 1, 10)
    dijkstra.graph.add_edge(0, 2, 20)
    dijkstra.graph.add_edge(0, 3, 30)
    dijkstra.graph.add_edge(1, 2, 10)
    dijkstra.graph.add_edge(1, 3, 40)
    dijkstra.graph.add_edge(1, 4, 50)
    dijkstra.graph.add_edge(2, 4, 50)
    dijkstra.graph.add_edge(2, 5, 20)
    dijkstra.graph.add_edge(2, 6, 60)
    dijkstra.graph.add_edge(3, 4, 60)
    dijkstra.graph.add_edge(3, 5, 10)
    dijkstra.graph.add_edge(4, 5, 5)
    dijkstra.graph.add_edge(7, 8, 5)
    dijkstra.get_paths(0)
    result_0 = dijkstra.show_paths()
    assert result_0 == [(0, 0), (0, 10), (0, 20), (0, 30), (5, 45), (2, 40), (2, 80)]

    dijkstra.get_paths(7)
    result_1 = dijkstra.show_paths()
    assert result_1 == [(7, 0), (7, 5)]
