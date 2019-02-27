from Encoding import Encoding1, Encoding2
from Graph import Node, Edge, Graph


# For the given graph, create Encoding 1 and Encoding 2
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

    e1 = Edge(a, c)
    e2 = Edge(b, c)

    graph = Graph([a, b, c], [e1, e2])

    enc1 = Encoding1(graph)
    print(enc1.get_clauses())
    #enc2 = Encoding2(graph)


if __name__ == '__main__':
    main()

