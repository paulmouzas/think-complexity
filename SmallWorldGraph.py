from RandomGraph import RandomGraph
from Graph import Graph, Vertex, Edge
from graphworld import *
import random

class SmallWorldGraph(RandomGraph):
    def __init__(self, vs, k, p):
        RandomGraph.__init__(self, vs)
        self.add_regular_edges(k=k)

    def rewire(self, p=0.01):
        es = list(self.edges())
        random.shuffle(es)
        vs = self.vertices()
        
        for e in es:
            v, w = e
            self.remove_edge(e)
            
            while True:
                w = random.choice(vs)
                if v is not w and not self.has_edge(v, w):
                    break
            self.add_edge(Edge(v,w))
def main():
    
    vs = [Vertex(c) for c in 'abcdefghijklmnopqrstuvwxyz']
    g = SmallWorldGraph(vs,2, p=0.01)
    g.rewire()
    layout = CircleLayout(g)
    
    # draw the graph
    gw = GraphWorld()
    gw.show_graph(g, layout)
    gw.mainloop()
    
    
if __name__ == '__main__':
    main()