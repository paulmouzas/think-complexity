""" Code example from Complexity and Computation, a book about
exploring complexity science with Python.  Available free from

http://greenteapress.com/complexity

Copyright 2011 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
"""
from collections import deque

def is_odd(n):
    return n%2 == 1

class Vertex(object):
    """A Vertex is a node in a graph."""

    def __init__(self, label=''):
        self.label = label

    def __repr__(self):
        """Returns a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Vertex(%s)' % repr(self.label)

    __str__ = __repr__
    """The str and repr forms of this object are the same."""


class Edge(tuple):
    """An Edge is a list of two vertices."""

    def __new__(cls, *vs):
        """The Edge constructor takes two vertices."""
        if len(vs) != 2:
            raise ValueError, 'Edges must connect exactly two vertices.'
        return tuple.__new__(cls, vs)

    def __repr__(self):
        """Return a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))

    __str__ = __repr__
    """The str and repr forms of this object are the same."""


class Graph(dict):
    """A Graph is a dictionary of dictionaries.  The outer
    dictionary maps from a vertex to an inner dictionary.
    The inner dictionary maps from other vertices to edges.
    
    For vertices a and b, graph[a][b] maps
    to the edge that connects a->b, if it exists."""

    def __init__(self, vs=[], es=[]):
        """Creates a new graph.  
        vs: list of vertices;
        es: list of edges.
        """
        for v in vs:
            self.add_vertex(v)
            
        for e in es:
            self.add_edge(e)

    def add_vertex(self, v):
        """Add a vertex to the graph."""
        self[v] = {}

    def add_edge(self, e):
        """Adds and edge to the graph by adding an entry in both directions.

        If there is already an edge connecting these Vertices, the
        new edge replaces it.
        """
        v, w = e
        self[v][w] = e
        self[w][v] = e

    def remove_edge(self, e):
        v, w = e
        del self[v][w]
        del self[w][v]
        
    def vertices(self):
        return self.keys()

    def edges(self):
        es = set()
        for e in self.itervalues():
            es.update(e.itervalues())
        return list(es)

    def get_edge(self, v, w):
        try:
            return self[v][w]
        except KeyError:
            return None
    has_edge = get_edge
    def out_vertices(self, v):
        return self[v].keys()

    def out_edges(self, v):
        return self[v].values()
        
    def add_all_edges(self):
        vs = self.vertices()
        for i, v in enumerate(vs):
            for j, w in enumerate(vs):
                if j == i: break
                self.add_edge(Edge(v, w))
    
    def add_regular_edges(self, k=2):
        vs = self.vertices()
        if k >= len(vs):
            raise ValueError, ("cannot build a regular graph with " +
                               "degree >= number of vertices.")
        if is_odd(k):
            if is_odd(len(vs)):
                raise ValueError, ("cannot build a regular graph with " +
                                   "an odd degree and an odd number of " +
                                   "vertices.")
            self.add_regular_edges_even(k-1)
            self.add_regular_edges_odd()
        
        self.add_regular_edges_even(k)
        
    def add_regular_edges_even(self, k=2):
        vs = self.vertices()
        double = vs * 2
        for i, v in enumerate(vs):
            for j in (1, k/2+1):
                w = double[i+j]
                self.add_edge(Edge(v, w))
                
    def add_regualr_edges_odd(self):
        vs = self.vertices()
        double = vs * 2
        n = len(vs)
        
        for i in range(n/2):
            v = vs[i]
            w = vs[i+n/2]
            self.add_edge(v,w)
                
    def bfs(self, s, visit=None):
        """Breadth first search, starting with (s).
        If (visit) is provided, it is invoked on each vertex.
        Returns the set of visited vertices.
        """
        visited = set()

        # initialize the queue with the start vertex
        queue = deque([s])
        
        # loop until the queue is empty
        while queue:

            # get the next vertex
            v = queue.popleft()

            # skip it if it's already visited
            if v in visited: continue

            # mark it visited, then invoke the visit function
            visited.add(v)
            if visit: visit(v)

            # add its out vertices to the queue
            queue.extend(self.out_vertices(v))

        # return the visited vertices
        return visited

    def is_connected(self):
        """Returns True if there is a path from any vertex to
        any other vertex in this graph; False otherwise.
        """
        vs = self.vertices()
        visited = self.bfs(vs[0])
        return len(visited) == len(vs)
                
def main(script, *args):
    v = Vertex('v')
    print v
    w = Vertex('w')
    print w
    g = Graph([v,w])
    print g
    g.add_all_edges()
    print g
    print g.bfs(v)
if __name__ == '__main__':
    import sys
    main(*sys.argv)