def test_mst():
    from  graphs.weighted_mst import MinSpanTree

    mstree = MinSpanTree()

    mstree.graph.add_vertex(0)
    mstree.graph.add_vertex(1)
    mstree.graph.add_vertex(2)
    mstree.graph.add_vertex(3)
    mstree.graph.add_vertex(4)
    mstree.graph.add_vertex(5)

    mstree.graph.add_edge(0, 1, 10)
    mstree.graph.add_edge(0, 2, 20)
    mstree.graph.add_edge(0, 3, 30)
    mstree.graph.add_edge(1, 2, 10)
    mstree.graph.add_edge(1, 3, 40)
    mstree.graph.add_edge(1, 4, 50)
    mstree.graph.add_edge(2, 4, 50)
    mstree.graph.add_edge(2, 5, 20)
    mstree.graph.add_edge(2, 6, 60)
    mstree.graph.add_edge(3, 4, 60)
    mstree.graph.add_edge(3, 5, 10)
    mstree.graph.add_edge(4, 5, 50)
    result_0 = mstree.mst(0)
    assert result_0 == [((None, 0), 0), ((0, 1), 10), ((1, 2), 10), ((2, 5), 20), ((5, 3), 10), ((5, 4), 50)]

    result_5 = mstree.mst(5)
    assert result_5 == [((None, 5), 0), ((5, 3), 10), ((5, 2), 20), ((2, 1), 10), ((1, 0), 10), ((2, 4), 50)]

    assert sum([x[1] for x in result_0]) == sum([x[1] for x in result_5])

