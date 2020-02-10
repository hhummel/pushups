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

class MinSpanTree(object):
    '''result is a list of vertices and weight to get there from preceeding vertex in form [(start, None), (second, value_from_start)...]'''

    def __init__(self):
        self.heap = Heap(reverse=True)
        self.graph = Graph()
        self.result = []

    def mst(self, start):
        vertex_list = self.graph.vertices[:]
        if not vertex_list:
            return None

        #Put start vertex into result. Mark it in vertex_list. Put candidate edges into heap.
        self.result = [((None, start), 0)]
        vertex_list[start] = None
        for end, value in enumerate(self.graph.edges[start]):
            if value:
                self.heap.insert(Candidate(start, end, value))

        #While there are candidates in the heap, get the best.  
        candidate = self.heap.delete()
        while candidate:

            #Filter out vertices already included in result.
            if vertex_list[candidate.end]:
                #Found the next vertex, get it's index
                start = candidate.end

                #Mark it in vertex_list
                vertex_list[start] = None

                #Add vertex (index, value_from_prev) to result
                self.result.append(((candidate.start, start), candidate.value))

                #Push new candidate edges onto heap if edge weight != 0 and not already included
                print([x is None for x in vertex_list])
                for end, value in enumerate(self.graph.edges[start]):
                    if value and vertex_list[end]:
                        self.heap.insert(Candidate(start, end, value))

            candidate = self.heap.delete()

        return self.result
