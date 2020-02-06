import random
import os, sys

#Following lines are for assigning parent directory dynamically.
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

def test_insert():
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

def test_insert_delete():
    from tree.search_tree import Tree

    tree = Tree()
    values = random.sample(range(1, 10001), 10000)

    for value in values:
        tree.insert(value)

    random.shuffle(values)

    for value in values:
        tree.delete(value)

    assert tree.display() == "Empty"

def test_successor():
    from tree.search_tree import Tree

    tree = Tree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(100)
    tree.insert(2)
    tree.insert(7)
    tree.insert(50)
    tree.insert(200)
    tree.delete(5)
    assert tree.display() == '10 Left: 7 Left: 2 Right: 100 Left: 50 Right: 200 '
    tree.delete(50)
    assert tree.display() == '10 Left: 7 Left: 2 Right: 100 Right: 200 '
    tree.delete(10)
    assert tree.display() == '100 Left: 7 Left: 2 Right: 200 '
    tree.delete(200)
    assert tree.display() == '100 Left: 7 Left: 2 '
    tree.delete(7)
    assert tree.display() == '100 Left: 2 '

