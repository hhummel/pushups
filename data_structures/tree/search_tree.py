class Node:
    '''Single node in a tree'''
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def display_value(self):
        if self.value:
            return f"{self.value} "
        else:
            return "Empty"
        


class Tree:
    '''Simple, unbalanced binary search tree.  Implements range-bound search, to illustrate
       How it's done.  Intended to be used behind a separate chaining hash table.'''
    def __init__(self):
        self.root = Node()

    def display(self):
        '''Returns a string describing the tree'''
        result = []
        return "".join(self._display_node(result, self.root))

    def insert(self, value):
        self._insert_node(value, self.root)

    def locate(self, value):
        '''Returns a tuple of parent and node associated with value.  Returns (None, None)
           if node is not found.  Used in delete method.'''
        return self._locate_node(value, None, self.root)

    def delete(self, value):
        '''Implements deletion by replacing relevant node with it's next higher valued successor.'''
        parent, node = self.locate(value)
        if node:
            return self._delete_node(parent, node)
        else:
            return "Value not found"

    def traverse(self, reverse=False, lower=None, upper=None):
        '''Traverses tree to give sorted result.  Descending order if reverse=True.  
           Search optionally bounded by lower and higher fields.  Returns a list''' 
        buf = []
        self._traverse(buf, self.root, reverse, lower, upper)
        return buf

    def _traverse_left(self, buf, current, reverse=False, lower=None, upper=None):
        if current.left and (lower is None or lower < current.value):
            self._traverse(buf, current.left, reverse, lower, upper)

    def _traverse_right(self, buf, current, reverse=False, lower=None, upper=None):
        if current.right and (upper is None or upper > current.value):
            self._traverse(buf, current.right, reverse, lower, upper)

    def _evaluate_current(self, buf, current, lower=None, upper=None):
        if (lower is None or lower <= current.value) and (upper is None or current.value <= upper):
            buf.append(current.value)

    def _traverse(self, buf, current, reverse=False, lower=None, upper=None):
        if not reverse:
            self._traverse_left(buf, current, reverse, lower, upper)
            self._evaluate_current(buf, current, lower, upper)
            self._traverse_right(buf, current, reverse, lower, upper)
        else:
            self._traverse_right(buf, current, reverse, lower, upper)
            self._evaluate_current(buf, current, lower, upper)
            self._traverse_left(buf, current, reverse, lower, upper)

    def _display_node(self, result, current):
        result.append(current.display_value())

        if current.left:
            result.append("Left: ")
            self._display_node(result, current.left)

        if current.right:
            result.append("Right: ")
            self._display_node(result, current.right)
        return result

    def _insert_node(self, value, current):
        if current.value is None:
            current.value = value
        elif value < current.value:
            if current.left:
                return self._insert_node(value, current.left)
            current.left = Node(value)
        else:
            if current.right:
                return self._insert_node(value, current.right)
            current.right = Node(value)

    def _locate_node(self, value, parent, current):
        if current.value is not None and current.value == value:
            return parent, current
        elif current.left is not None and current.value > value:
            return self._locate_node(value, current, current.left)
        elif current.right is not None and current.value < value:
            return self._locate_node(value, current, current.right)
        else:
            print("Failure")
            return None, None

    def _locate_successor(self, current):
        if not current.right:
            return (None, current)
        
        _next = current.right
        while _next.left:
            current = _next
            _next = _next.left

        return (current, _next)

    def _delete_node(self, parent, node):
        if not node:
            return None

        if not (node.left or node.right):
            #No branches
            if parent is None:
                #At root, so set value to None rather than deleting node
                node.value = None
            elif node.value < parent.value:
                #If node is the left branch from parent, set to none
                parent.left = None
            else:
                #Otherwise it's the right branch
                parent.right = None
            return "Success"

        if not (node.left and node.right):
            #There's one branch node to delete, find which one
            if node.left:
                node = node.left 
            else:
                node = node.right
            #Replace the node with the next on the branch. Figure out where it goes on parent. If no parent, at root
            if parent is None:
                self.root = node
            elif node.value < parent.value:
                parent.left = node
            else:
                parent.right = node
            return "Success"

        else:
            #There are 2 branches, so use the successor trick
            successor_parent, successor = self._locate_successor(node)
            node.value = successor.value
            return self._delete_node(successor_parent, successor)
