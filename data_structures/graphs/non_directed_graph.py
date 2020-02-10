class Vertex(object):
    def __init__(self, value):
        self.value = value
        self.visited = False

class Graph(object):
    def __init__(self):
        from collections import deque
        self.vertices = []
        self.edges = []
        self.stack = []
        self.queue = deque()

    def add_vertex(self, value):
        self.vertices.append(Vertex(value))
        self.edges = [x + [0] for x in self.edges]
        self.edges.append([0] * len(self.vertices))

    def add_edge(self, start, end, weight=1):
        l = len(self.edges)
        if 0 < start >= l or 0 < end >= l:
            print("Add edge error")
        else:
            self.edges[start][end] = self.edges[end][start] = weight

    def find_next_adjacent(self, index):
        for vert_index, value in enumerate(self.edges[index]):
            if (value and not self.vertices[vert_index].visited):
                return vert_index

        return None

    def display_vertex(self, index):
        return f"{self.vertices[index].value}"

    def dfs(self):
        result = []
        if not self.vertices:
            return result

        index = 0
        self.vertices[index].visited = True
        result.append(self.display_vertex(index))
        self.stack.append(index)

        while (self.stack):
            index = self.find_next_adjacent(self.stack[-1])
            if index:
                self.vertices[index].visited = True
                result.append(self.display_vertex(index))
                self.stack.append(index)
            else:
                index = self.stack.pop()

        return result


    def bfs(self):
        result = []
        if not self.vertices:
            return result

        index = 0
        self.vertices[index].visited = True
        result.append(self.display_vertex(index))
        self.queue.appendleft(index)

        while(self.queue):
            index = self.find_next_adjacent(self.queue[-1])
            if index:
                self.vertices[index].visited = True
                result.append(self.display_vertex(index))
                self.queue.appendleft(index)
            else:
                index = self.queue.pop()

        return result
