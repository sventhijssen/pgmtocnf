import unittest

from Encoding import Encoding1
from Graph import Node, Edge, Graph
from Instance import Instance
from Variables import IndicatorVariable, ParameterVariable


class TestVariables(unittest.TestCase):

    # NODES #
    def test_same_node(self):
        a1 = Node("a")
        a2 = Node("a", [1, 2, 3])
        self.assertEqual(a1, a2)

    def test_different_node(self):
        a = Node("a")
        b = Node("b")
        self.assertNotEqual(a, b)

    # INDICATOR VARIABLES #
    def test_indicator_variable_representation(self):
        a = Node("a")
        i1 = IndicatorVariable(a, a.values[0])
        i2 = IndicatorVariable(a, a.values[1])
        self.assertEqual("lambda_a1", str(i1))
        self.assertEqual("lambda_a2", str(i2))

    def test_same_indicator_variable(self):
        a = Node("a")
        i1 = IndicatorVariable(a, a.values[0])
        i2 = IndicatorVariable(a, a.values[0])
        self.assertEqual(i1, i2)

    def test_different_indicator_variable_same_name(self):
        a = Node("a")
        i1 = IndicatorVariable(a, a.values[0])
        i2 = IndicatorVariable(a, a.values[1])
        self.assertNotEqual(i1, i2)

    def test_different_indicator_variable_different_name(self):
        a = Node("a")
        b = Node("b")
        i1 = IndicatorVariable(a, a.values[0])
        i2 = IndicatorVariable(b, b.values[0])
        self.assertNotEqual(i1, i2)

    # PARAMETER VARIABLES #
    def test_parameter_variable_representation_no_incoming(self):
        a = Node("a")
        p = ParameterVariable(a, a.values[0])
        self.assertEqual("theta_a1", str(p))

    def test_parameter_variable_representation_incoming(self):
        # a  b
        # \ /
        #  c
        a = Node("a")
        b = Node("b")
        c = Node("c")
        i1 = Instance(b, b.values[0])
        i2 = Instance(c, c.values[1])
        p = ParameterVariable(a, a.values[0], [i1, i2])
        self.assertEqual("theta_a1|b1,c2", str(p))

    def test_same_parameter_variable(self):
        # a  b
        # \ /
        #  c
        a = Node("a")
        b = Node("b")
        c = Node("c")
        i1 = Instance(b, b.values[0])
        i2 = Instance(c, c.values[1])
        p1 = ParameterVariable(a, a.values[0], [i1, i2])
        p2 = ParameterVariable(a, a.values[0], [i1, i2])
        self.assertEqual(p1, p2)

    def test_different_parameter_variable_same_name(self):
        # a -> b
        a = Node("a")
        b = Node("b")
        i1 = Instance(a, a.values[0])
        i2 = Instance(a, a.values[1])
        p1 = ParameterVariable(b, b.values[0], [i1])
        p2 = ParameterVariable(b, b.values[0], [i2])
        self.assertNotEqual(p1, p2)


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
        self.assertEqual(19, len(enc1.get_all_variables()))


class TestEncoding2(unittest.TestCase):

    def test_paper_example(self):
        pass


if __name__ == '__main__':
    unittest.main()
