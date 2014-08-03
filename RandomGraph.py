from Graph import *
from graphworld import *
import random
import string

class RandomGraph(Graph):
    
    def add_random_edges(self, p=0.05):
        """Starting with an edgeless graph, add edges to
        form a random graph where (p) is the probability 
        that there is an edge between any pair of vertices.
        """
        vs = self.vertices()
        for i, v in enumerate(vs):
            for j, w in enumerate(vs):
                if j <= i: continue
                if random.random() > p: continue
                self.add_edge(Edge(v, w))

def test_graph(n, p):
    vertex_labels = string.ascii_lowercase[:n]
    vs = [Vertex(c) for c in vertex_labels]
    
    g = RandomGraph(vs)
    g.add_random_edges(p=p)
    return g.is_connected()
    
def test_p(n, p, num):
    """ Generates the number of graphs (num) with n vertices
    and p probability and returns how many of which are connected
    """
    count = 0 
    for i in range(num):
        if test_graph(n, p):
            count += 1
    return count
                
if __name__ == '__main__':
    # create a graph and a layout
    vs = [Vertex(c) for c in 'abcdefgh']
    g = RandomGraph(vs)
    #g.add_random_edges()
    g.add_all_edges()
    print g.is_connected()
    