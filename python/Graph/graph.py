class Vertex():

    def __init__(self, id):
        self.id = id
        self.edges = []
        self.adjacent_vertices = []

    def __str__(self):
        return str("Vertex-{}".format(self.id))

    def __eq__(self, vertex):
        return self.id == vertex.id

    def __hash__(self):
        return hash(self.id)

    def add_adjacent_vertex(self, edge, vertex):
        self.edges.append(edge)
        self.adjacent_vertices.append(vertex)


class Edge():

    def __init__(self, vertex1, vertex2, weight=0, is_directed=False):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight
        self.is_directed = is_directed

    def __eq__(self, edge):
        return self.vertex1 == edge.vertex1 and self.vertex2 == edge.vertex2

    def __str__(self):
        return "Edge {} {}. Weight - {}".format(self.vertex1, self.vertex2, self.weight)


class Graph():

    def __init__(self, is_directed):
        self.all_vertices = {}
        self.all_edges = []
        self.is_directed = False

    def __str__(self):
        res = ''
        for vertex in g.all_vertices:
            res += '{} \n'.format(g.all_vertices[vertex])
            for edge in g.all_vertices[vertex].edges:
                res += '{} \n'.format(edge)
        return res

    def add_edge(self, id1, id2, weight=0):
        vertex1 = self.all_vertices.setdefault(id1, Vertex(id1))
        vertex2 = self.all_vertices.setdefault(id2, Vertex(id2))

        edge = Edge(vertex1, vertex2, weight, self.is_directed)

        vertex1.add_adjacent_vertex(edge, vertex2)
        if not self.is_directed:
            vertex2.add_adjacent_vertex(edge, vertex1)
        return
    
def topological_sort(graph):
    def sort_child(vertex, visited, stack):
        visited.add(vertex.id)
        for child in vertex.adjacent_vertices:
            if child.id in visited:
                continue
            sort_child(child, visited, stack)
        stack.append(vertex.id)

    visited = set()
    stack = []
    for id in graph.all_vertices:
        vertex = graph.all_vertices[id]
        if id in visited:
            continue
        sort_child(vertex, visited, stack)
    return stack
    
    

if __name__ == '__main__':
    g = Graph(False)
    g.add_edge(1, 2, 10)
    g.add_edge(2, 3, 5)
    g.add_edge(1, 4, 6)
    print g
