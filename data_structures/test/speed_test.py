import timeit
import os, sys

#Following lines are for assigning parent directory dynamically.
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

code_to_test = """

import random
from tree.search_tree import Tree

values = random.sample(range(1, 101), 100)
tree = Tree()

for value in values:
    tree.insert(value)

random.shuffle(values)

for value in values:
    tree.delete(value)

tree.display()
"""

elapsed_time = timeit.timeit(code_to_test, number=2)/2

print(elapsed_time)

assert 1 == 1
