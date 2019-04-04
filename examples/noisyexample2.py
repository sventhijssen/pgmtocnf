from Graph import Node, Edge, NoisyGraph
from Probability import Probability
from main import main

a = Node("a", [1, 2])
b = Node("b", [1, 2])
c = Node("c", [1, 2])

e1 = Edge(a, b)
e2 = Edge(a, c)

w1 = Probability((a, 1), 0.1)
w2 = Probability((a, 2), 0.9)

w3 = Probability((b, 1), 0.1, [(a, 1)])
w4 = Probability((b, 1), 0.2, [(a, 2)])

w5 = Probability((c, 1), 0.1, [(a, 1)])
w6 = Probability((c, 1), 0.01, [(a, 2)])


graph = NoisyGraph([a, b, c], [e1, e2], [w1, w2, w3, w4, w5, w6])

if __name__ == '__main__':
    main(graph)