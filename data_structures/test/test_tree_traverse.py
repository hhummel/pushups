import random
import os, sys

#Following lines are for assigning parent directory dynamically.
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

def test_traverse():
    from tree.search_tree import Tree

    values = random.sample(range(1, 101), 100)
    tree = Tree()

    for value in values:
        tree.insert(value)

    traverse_list = tree.traverse()
    reverse_list = tree.traverse(reverse = True)
    range_list = tree.traverse(lower=10, upper=20)
    reverse_range = tree.traverse(reverse=True, lower=10, upper=20)

    assert traverse_list == list(range(1, 101))
    traverse_list.reverse()
    assert reverse_list == traverse_list

    assert range_list == list(range(10, 21))
    range_list.reverse()
    assert reverse_range == range_list 

    random.shuffle(values)

    for value in values:
        tree.delete(value)

    assert tree.display() == "Empty"

