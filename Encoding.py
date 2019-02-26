from Logic import Clause, Literal, Conjunction, Equivalence
from Variables import IndicatorVariable, ParameterVariable


class Encoding1:

    def __init__(self, graph):
        self.graph = graph
        self.indicator_variables = []

        # # For each value x of each network variable X, define an indicator variable lambda_x
        # for node in graph.nodes:
        #     for value in node.values:
        #         self.indicator_variables.append(IndicatorVariable(node, value))
        #
        # # For each parameter Pr(x|[u]) in the Bayesian network, define a corresponding parameter theta_x|[u] in the CNF.
        # self.parameter_variables = []
        #
        # # For each node
        # for node in graph.nodes:
        #     # Check whether the node is an end node in any edge
        #     if node in graph.get_end_nodes():
        #         # If the node has incoming edges, check for which edges
        #         for edge in graph.edges:
        #             # Check whether the node is an end node in any edge
        #             if node == edge.end:
        #                 # The node is an end node and thus has incoming edges
        #                 start_node = edge.start
        #
        #                 # Make a parameter variable for the with the start node and the end node,
        #                 # for each possible value combination of both variables
        #                 for node_value in node.values:
        #                     for start_node_value in edge.start.values:
        #                         self.parameter_variables.append(
        #                             ParameterVariable(node, node_value, start_node, start_node_value))
        #     else:
        #         # The node is not an end node and thus has no incoming edges
        #         for node_value in node.values:
        #             self.parameter_variables.append(
        #                 ParameterVariable(node, node_value, node, node_value))


    def get_clauses(self):
        return self.get_indicator_clauses() + "\n\n" + self.get_parameter_clauses()

    def get_indicator_clauses(self):
        clauses = []
        for node in self.graph.nodes:
            clause = Clause()
            for i in range(len(node.get_values())):
                clause.__add__(Literal(IndicatorVariable(node, i+1)))
            clauses.append(clause)

        for node in self.graph.nodes:
            for i in range(len(node.get_values())):
                for j in range(i+1, len(node.get_values())):
                    clause = Clause()
                    clause.__add__(Literal(IndicatorVariable(node, i+1), False))
                    clause.__add__(Literal(IndicatorVariable(node, j+1), False))
                    clauses.append(clause)

        return "\n".join(map(str, clauses))

    def get_parameter_clauses(self):

        clauses = []
        equivalences = []
        for node in self.graph.nodes:
            if node not in self.graph.get_end_nodes():
                for i in range(len(node.get_values())):
                    equivalences.append(Equivalence(Literal(IndicatorVariable(node, i+1)), Literal(ParameterVariable(node, i+1))))

        for equivalence in equivalences:
            for implication in equivalence.get_implications():
                clauses.append(implication.get_clause())

        return "\n".join(map(str, clauses))

class Encoding2:

    def __init__(self, graph):
        pass