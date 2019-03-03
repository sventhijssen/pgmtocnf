from Encoding import Encoding1, Encoding2
from Graph import Node, Edge, Graph


# For the given graph, create Encoding 1 and Encoding 2
from Logic import Literal, Disjunction


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

    graph = Graph([a, b, c], [e1, e2])

    enc1 = Encoding1(graph)
    print(enc1)

    print("===")
    print("CNF - ENC1")
    print("===")
    cnf = enc1.get_cnf()
    for clause in cnf:
        print(clause)

    # enc2 = Encoding2(graph)
    # print(enc2)
    #
    # print("===")
    # print("CNF - ENC2")
    # print("===")
    # cnf2 = enc2.get_cnf()
    # for clause in cnf2:
    #     print(clause)

if __name__ == '__main__':
    main()

