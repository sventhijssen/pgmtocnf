import itertools

from Instance import Instance
from Logic import Clause, Literal, Conjunction, Equivalence, Disjunction
from Variables import IndicatorVariable, ParameterVariable


class Encoding1:

    def __init__(self, graph):
        self.graph = graph

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

    def __str__(self):
        out = "-----------------\n"
        out += "Indicator clauses\n"
        out += "-----------------\n"
        out += "\n".join(map(str, self.get_indicator_clauses()))
        out += "\n\n"
        out += "-----------------\n"
        out += "Parameter clauses\n"
        out += "-----------------\n"
        out += "\n".join(map(str, self.get_parameter_clauses()))
        return out


    def get_clauses(self):
        return self.get_indicator_clauses() + self.get_parameter_clauses()

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

        return clauses

    def get_parameter_clauses(self):
        clauses = []
        equivalences = []
        for node in self.graph.nodes:
            if node not in self.graph.get_end_nodes():
                for i in range(len(node.get_values())):
                    equivalences.append(Equivalence(Literal(IndicatorVariable(node, i+1)), Literal(ParameterVariable(node, i+1))))

                clauses.extend(equivalences)

            else:
                values = []
                conditions = []
                for i in self.graph.get_incoming_nodes(node):
                    values.append([IndicatorVariable(i, v) for v in i.get_values()])
                    conditions.append([Instance(i, v) for v in i.get_values()])
                cs = list(itertools.product(*conditions))

                lst = []
                for tup in cs:
                    l = list(tup)
                    nl = []
                    for v in l:
                        nl.append(IndicatorVariable(v.get_node(), v.get_value()))
                    lst += [nl + [IndicatorVariable(node, v), ParameterVariable(node, v, l)] for v in node.get_values()]
                #clauses.extend(lst)
                for it in lst:
                    clauses.append((Equivalence(Conjunction(it[:len(it)-1]), it[len(it)-1])))

        return clauses


                # cartesian = list(itertools.product(*values))
                # lst = []
                # for tup in cs:
                #     l = list(tup)
                #     lst.append([ParameterVariable(node, v, l) for v in node.get_values()])
                #
                # for l in lst:
                #     print(l)

                # for start_node in self.graph.get_incoming_nodes(node):
                #     for value in start_node.get_values():
                #         clauses.append(Clause([Literal(), Literal()]))
                # for edge in self.graph.edges:
                #     if edge.end == node:
                #         start_node = edge.start
                #         for i in range(len(node.get_values())):
                #             for j in range(len(start_node.get_values())):
                #                 equivalences.append(Equivalence(Conjunction([Literal(IndicatorVariable(node, i+1)), Literal(IndicatorVariable(start_node, j+1))]), Literal(ParameterVariable(node, i+1, start_node, j+1))))

        # # TODO: Fix, left part or right part of implication can contain conjunctions such that multiple clauses can be derived
        # for equivalence in equivalences:
        #     for implication in equivalence.get_implications():
        #         clauses.append(implication.get_clause())

        #return "\n".join(map(str, clauses))

class Encoding2:

    def __init__(self, graph):
        pass