from Graph import Node, Edge, Graph
from Probability import Probability
from main import main

i = Node("I", [1, 2])
o = Node("O", [1, 2])
r = Node("R", [1, 2])

t = Node("T", [1, 2])
s = Node("S", [1, 2])
n = Node("N", [1, 2])

e1 = Edge(i, t)
e2 = Edge(o, t)
e3 = Edge(r, t)

e4 = Edge(i, s)
e5 = Edge(o, s)
e6 = Edge(r, s)

e7 = Edge(i, n)
e8 = Edge(o, n)
e9 = Edge(r, n)

w1 = Probability((i, 1), 0.95)
w2 = Probability((i, 2), 0.05)

w3 = Probability((o, 1), 0.99)
w4 = Probability((o, 2), 0.01)

w5 = Probability((r, 1), 0.9999)
w6 = Probability((r, 2), 0.0001)

# F F F
w7 = Probability((t, 1), 0.90, [(i, 1), (o, 1), (r, 1)])
w8 = Probability((t, 2), 0.10, [(i, 1), (o, 1), (r, 1)])
w9 = Probability((s, 1), 0.90, [(i, 1), (o, 1), (r, 1)])
w10 = Probability((s, 2), 0.10, [(i, 1), (o, 1), (r, 1)])
w11 = Probability((n, 1), 0.90, [(i, 1), (o, 1), (r, 1)])
w12 = Probability((n, 2), 0.10, [(i, 1), (o, 1), (r, 1)])

# F F T
w13 = Probability((t, 1), 0.27, [(i, 1), (o, 1), (r, 2)])
w14 = Probability((t, 2), 0.73, [(i, 1), (o, 1), (r, 2)])
w15 = Probability((s, 1), 0.0090, [(i, 1), (o, 1), (r, 2)])
w16 = Probability((s, 2), 0.9910, [(i, 1), (o, 1), (r, 2)])
w17 = Probability((n, 1), 0.45, [(i, 1), (o, 1), (r, 2)])
w18 = Probability((n, 2), 0.55, [(i, 1), (o, 1), (r, 2)])

# F T F
w19 = Probability((t, 1), 0.90, [(i, 1), (o, 2), (r, 1)])
w20 = Probability((t, 2), 0.10, [(i, 1), (o, 2), (r, 1)])
w21 = Probability((s, 1), 0.0090, [(i, 1), (o, 2), (r, 1)])
w22 = Probability((s, 2), 0.9910, [(i, 1), (o, 2), (r, 1)])
w23 = Probability((n, 1), 0.90, [(i, 1), (o, 2), (r, 1)])
w24 = Probability((n, 2), 0.10, [(i, 1), (o, 2), (r, 1)])

# T F F
w25 = Probability((t, 1), 0.36, [(i, 2), (o, 1), (r, 1)])
w26 = Probability((t, 2), 0.64, [(i, 2), (o, 1), (r, 1)])
w27 = Probability((s, 1), 0.81, [(i, 2), (o, 1), (r, 1)])
w28 = Probability((s, 2), 0.19, [(i, 2), (o, 1), (r, 1)])
w29 = Probability((n, 1), 0.7650, [(i, 2), (o, 1), (r, 1)])
w30 = Probability((n, 2), 0.2350, [(i, 2), (o, 1), (r, 1)])

# F T T
w31 = Probability((t, 1), 0.27, [(i, 1), (o, 2), (r, 2)])
w32 = Probability((t, 2), 0.73, [(i, 1), (o, 2), (r, 2)])
w33 = Probability((s, 1), 0.0001, [(i, 1), (o, 2), (r, 2)])
w34 = Probability((s, 2), 0.9999, [(i, 1), (o, 2), (r, 2)])
w35 = Probability((n, 1), 0.45, [(i, 1), (o, 2), (r, 2)])
w36 = Probability((n, 2), 0.55, [(i, 1), (o, 2), (r, 2)])

# T F T
w37 = Probability((t, 1), 0.1080, [(i, 2), (o, 1), (r, 2)])
w38 = Probability((t, 2), 0.8920, [(i, 2), (o, 1), (r, 2)])
w39 = Probability((s, 1), 0.0081, [(i, 2), (o, 1), (r, 2)])
w40 = Probability((s, 2), 0.9919, [(i, 2), (o, 1), (r, 2)])
w41 = Probability((n, 1), 0.3825, [(i, 2), (o, 1), (r, 2)])
w42 = Probability((n, 2), 0.6175, [(i, 2), (o, 1), (r, 2)])

# T T F
w43 = Probability((t, 1), 0.36, [(i, 2), (o, 2), (r, 1)])
w44 = Probability((t, 2), 0.64, [(i, 2), (o, 2), (r, 1)])
w45 = Probability((s, 1), 0.0081, [(i, 2), (o, 2), (r, 1)])
w46 = Probability((s, 2), 0.9919, [(i, 2), (o, 2), (r, 1)])
w47 = Probability((n, 1), 0.7650, [(i, 2), (o, 2), (r, 1)])
w48 = Probability((n, 2), 0.2350, [(i, 2), (o, 2), (r, 1)])

# T T T
w49 = Probability((t, 1), 0.1080, [(i, 2), (o, 2), (r, 2)])
w50 = Probability((t, 2), 0.8920, [(i, 2), (o, 2), (r, 2)])
w51 = Probability((s, 1), 0.0001, [(i, 2), (o, 2), (r, 2)])
w52 = Probability((s, 2), 0.9999, [(i, 2), (o, 2), (r, 2)])
w53 = Probability((n, 1), 0.3825, [(i, 2), (o, 2), (r, 2)])
w54 = Probability((n, 2), 0.6175, [(i, 2), (o, 2), (r, 2)])

graph = Graph(
    [i, o, r, t, s, n],
    [e1, e2, e3, e4, e5, e6, e7, e8, e9],
    [w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12,
     w13, w14, w15, w16, w17, w18, w19, w20, w21, w22, w23, w24,
     w25, w26, w27, w28, w29, w30, w31, w32, w33, w34, w35, w36,
     w37, w38, w39, w40, w41, w42, w43, w44, w45, w46, w47, w48,
     w49, w50, w51, w52, w53, w54])

if __name__ == '__main__':
    main(graph)

