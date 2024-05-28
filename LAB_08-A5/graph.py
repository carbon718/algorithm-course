def cost(v,u):
    return ((v.x - u.x)**2 + (v.y - u.y)**2)**0.5
class Vertex:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.parent = None
        self.cost = float('inf')

class Edge:
    def __init__(self, v, u):
        self.v = v
        self.u = u
        self.cost = cost(v,u)
class Graph ():
    def __init__ (self):
        self.vertices = []
        self.edges = []
    def add_vertex (self, id, x, y):
        self.vertices.append(Vertex(id, x, y))
    def add_edge (self, v, u):
        e = Edge(v, u)
        self.edges.append(e)
