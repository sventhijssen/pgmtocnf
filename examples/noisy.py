from Graph import Node, Edge, NoisyGraph
from Probability import Probability
from main import main

i = Node("I", [1, 2])
o = Node("O", [1, 2])
r = Node("R", [1, 2])

t = Node("T", [1, 2])
s = Node("S", [1, 2])
n = Node("N", [1, 2])

leak_probability = 0.10

e1 = Edge(i, t)
e2 = Edge(o, t)
e3 = Edge(r, t)

e4 = Edge(i, s)
e5 = Edge(o, s)
e6 = Edge(r, s)

e7 = Edge(i, n)
e8 = Edge(o, n)
e9 = Edge(r, n)

w1 = Probability((i, 2), 0.05)
w2 = Probability((o, 2), 0.01)
w3 = Probability((r, 2), 0.0001)

w22 = Probability((i, 1), 0.95)
w23 = Probability((o, 1), 0.99)
w24 = Probability((r, 1), 0.9999)

# F F T
w4 = Probability((t, 2), 1-0.2619, [(r, 2)])
w5 = Probability((s, 2), 1-0.0089, [(r, 2)])
w6 = Probability((n, 2), 1-0.4466, [(r, 2)])
w7 = Probability((t, 2), 1-0.873, [(r, 1)])
w8 = Probability((s, 2), 1-0.8866, [(r, 1)])
w9 = Probability((n, 2), 1-0.8933, [(r, 1)])



# F T F
w10 = Probability((t, 2), 1-0.8729, [(o, 2)])
w11 = Probability((s, 2), 1-0.0090, [(o, 2)])
w12 = Probability((n, 2), 1-0.8932, [(o, 2)])
w13 = Probability((t, 2), 1-0.8729, [(o, 1)])
w14 = Probability((s, 2), 1-0.8954, [(o, 1)])
w15 = Probability((n, 2), 1-0.8932, [(o, 1)])

# T F F
w16 = Probability((t, 2), 1-0.36, [(i, 2)])
w17 = Probability((s, 2), 1-0.8019, [(i, 2)])
w18 = Probability((n, 2), 1-0.7650, [(i, 2)])
w19 = Probability((t, 2), 1-0.8999, [(i, 1)])
w20 = Probability((s, 2), 1-0.8910, [(i, 1)])
w21 = Probability((n, 2), 1-0.9, [(i, 1)])

graph = NoisyGraph(
    [i, o, r, t, s, n],
    [e1, e2, e3, e4, e5, e6, e7, e8, e9],
    [w1, w2, w3,w4, w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,w18,w19,w20,w21,w22,w23,w24],
    leak_probability)

if __name__ == '__main__':
    main(graph)

