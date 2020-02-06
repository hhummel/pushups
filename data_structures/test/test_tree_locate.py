import random
import os, sys

#Following lines are for assigning parent directory dynamically.
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

def test_locate():
    from tree.search_tree import Tree

    tree = Tree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(100)
    tree.insert(2)
    tree.insert(7)
    tree.insert(50)
    tree.insert(200)
    assert tree.display() == '10 Left: 5 Left: 2 Right: 7 Right: 100 Left: 50 Right: 200 '

    result = tree.locate(5)
    #Result returns the parent object and the matching object, if found
    assert result[0].value == 10
    assert result[1].value == 5

    tree.delete(5)
    assert tree.display() == '10 Left: 7 Left: 2 Right: 100 Left: 50 Right: 200 '
    parent, child = tree.locate(5)
    assert parent is None
    assert child is None

