from heaps.object_heap import Heap
from graphs.non_directed_graph import Graph

class Candidate(object):
    '''Candidate for inclusion in MST. Value is weight in graph'''

    def __init__(self, start, end, value):
        self.start = start
        self.end = end
        self.value = value

    def __str__(self):
        return f"Start : {self.start} End: {self.end} Weight: {self.value}"

class PathEntry(object):
    def __init__(self, parent, value):
        self.parent = parent
        self.value = value

    def __str__(self):
        return f"Parent : {self.parent} Cost: {self.value}"

class Dijkstra(object):
    '''Find shortest path from origin to other vertices'''

    def __init__(self):
        self.heap = Heap(reverse=True)
        self.graph = Graph()
        self.paths = []

    def get_paths(self, origin):
        '''Find shortest path to each vertex from origin'''

        vertex_list = [True] * len(self.graph.vertices)
        if not vertex_list:
            return None
        paths = [None] * len(vertex_list)
        vertex_list[origin] = False
        paths[origin] = PathEntry(origin, 0)

        while any(vertex_list):
            self.heap = Heap(reverse=True)
            start_list = [index for index, value in enumerate(vertex_list) if value is False]
            end_list = [index for index, value in enumerate(vertex_list) if value is True]
            for start in start_list:
                for end in end_list:
                    if self.graph.edges[start][end]:
                        #Find incremental cost to next vertex from established vertices. Add to base cost
                        value = paths[start].value + self.graph.edges[start][end]
                        self.heap.insert(Candidate(start, end, value))

            #Find the best, update paths table and vertex_list
            best = self.heap.delete()
            if best:
                vertex_list[best.end] = False
                if not paths[end] or paths[end].value > best.value:
                    paths[best.end] = PathEntry(best.start, best.value)
            else:
                vertex_list = [False for x in vertex_list]

        self.paths = paths

    def show_paths(self):
        return [(x.parent, x. value) for x in self.paths if x]
