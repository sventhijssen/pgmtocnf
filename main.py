from Encoding import Encoding1, Encoding2
from Graph import Node, Edge, Graph


# For the given graph, create Encoding 1 and Encoding 2
from Logic import Literal, Disjunction
from Probability import Probability
from Weight import Weight


def main():
    # i = Node("i")
    # o = Node("o")
    # r = Node("r")
    # t = Node("t")
    # s = Node("s")
    # n = Node("n")
    #
    # e1 = Edge(i, t)
    # e2 = Edge(i, s)
    # e3 = Edge(i, n)
    # e4 = Edge(o, t)
    # e5 = Edge(o, s)
    # e6 = Edge(o, n)
    # e7 = Edge(r, t)
    # e8 = Edge(r, s)
    # e9 = Edge(r, n)
    #
    # graph = Graph([i, o, r, t, s, n], [e1, e2, e3, e4, e5, e6, e7, e8, e9])

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

    enc1 = Encoding1(graph)
    #print(enc1)

    print("===")
    print("CNF - ENC1")
    print("===")
    for clause in enc1.get_cnf():
        print(clause)
    enc1.export_to_dimacs("out/enc1.cnf")
    enc1.export_enc_to_latex("out/enc1_enc.tex")
    enc1.export_weights_to_latex("out/enc1_weights.tex")

    weights = enc1.get_weights()
    for weight in weights:
        print(weight)

    enc2 = Encoding2(graph)
    print(enc2)

    cnf2 = enc2.get_cnf()
    print("===")
    print("CNF - ENC2")
    print("===")
    for clause in cnf2:
        print(clause)
    enc2.export_to_dimacs("out/enc2.cnf")
    enc2.export_enc_to_latex("out/enc2_enc.tex")
    #enc2.export_enc_to_latex("out/enc2_weights.tex")

    weights = enc2.get_weights()
    #for weight in weights:
        #print(weight)

if __name__ == '__main__':
    main()

