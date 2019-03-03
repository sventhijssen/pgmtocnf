import unittest

from Encoding import Encoding1
from Graph import Node, Edge, Graph


class TestEncoding1(unittest.TestCase):

    def test_paper_example(self):
        a = Node("a", [1, 2])
        b = Node("b", [1, 2])
        c = Node("c", [1, 2, 3])

        e1 = Edge(a, b)
        e2 = Edge(a, c)

        graph = Graph([a, b, c], [e1, e2])
        enc1 = Encoding1(graph)
        self.assertEqual(42, len(enc1.get_cnf()))

    def test_isupper(self):
        pass

    def test_split(self):
        pass


class TestEncoding2(unittest.TestCase):

    def test_paper_example(self):
        pass


if __name__ == '__main__':
    unittest.main()
