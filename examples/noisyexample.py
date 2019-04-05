from Graph import Node, Edge, Graph, NoisyGraph
from Probability import Probability
from main import main

a = Node("a", [1, 2])
b = Node("b", [1, 2])
c = Node("c", [1, 2])

e1 = Edge(a, c)
e2 = Edge(b, c)

w1 = Probability((a, 1), 0.2)
#w2 = Probability((a, 2), 0.8)
w2 = Probability((b, 1), 0.1)
#w4 = Probability((b, 2), 0.9)

w3 = Probability((c, 1), 0.2, [(a, 1)])
w6 = Probability((c, 1), 0.3, [(a, 2)])

w4 = Probability((c, 1), 0.1, [(b, 1)])
w8 = Probability((c, 1), 0.2, [(b, 2)])

graph = NoisyGraph([a, b, c], [e1, e2], [w1, w2, w3, w4], 0)

if __name__ == '__main__':
    main(graph)