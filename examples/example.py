from Graph import Node, Edge, Graph
from Probability import Probability

a = Node("a", [1, 2])
b = Node("b", [1, 2])
c = Node("c", [1, 2, 3])

e1 = Edge(a, b)
e2 = Edge(a, c)

w1 = Probability((a, 1), 0.1)
w2 = Probability((a, 2), 0.9)

w3 = Probability((b, 1), 0.1, [(a, 1)])
w4 = Probability((b, 2), 0.9, [(a, 1)])
w5 = Probability((b, 1), 0.2, [(a, 2)])
w6 = Probability((b, 2), 0.8, [(a, 2)])

w7 = Probability((c, 1), 0.1, [(a, 1)])
w8 = Probability((c, 2), 0.2, [(a, 1)])
w9 = Probability((c, 3), 0.7, [(a, 1)])

w10 = Probability((c, 1), 0.01, [(a, 2)])
w11 = Probability((c, 2), 0.09, [(a, 2)])
w12 = Probability((c, 3), 0.9, [(a, 2)])

graph = Graph([a, b, c], [e1, e2], [w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12])