from functools import reduce
from operator import mul

from Instance import Instance
from Variables import ParameterVariable


class Graph:
    def __init__(self, nodes, edges, probabilities):
        self.nodes = nodes
        self.edges = edges
        self.probabilities = probabilities

    @staticmethod
    def get_graph_type():
        return "full"

    def get_start_nodes(self):
        start_nodes = []
        for edge in self.edges:
            start_nodes.append(edge.start)
        return set(start_nodes)

    def get_end_nodes(self):
        end_nodes = []
        for edge in self.edges:
            end_nodes.append(edge.end)
        return set(end_nodes)

    def get_incoming_nodes(self, node):
        incoming = []
        for edge in self.edges:
            if edge.end == node:
                incoming.append(edge.start)
        return incoming

    def get_probability(self, parameter):
        for prob in self.probabilities:
            if prob.parameter_variable == parameter:
                return prob.probability
        return 1


class NoisyGraph:
    def __init__(self, nodes, edges, probabilities, leaky_probability):
        self.nodes = nodes
        self.edges = edges
        self.probabilities = probabilities
        self.leaky_probability = leaky_probability

    @staticmethod
    def get_graph_type():
        return "noisy"

    def get_start_nodes(self):
        start_nodes = []
        for edge in self.edges:
            start_nodes.append(edge.start)
        return set(start_nodes)

    def get_end_nodes(self):
        end_nodes = []
        for edge in self.edges:
            end_nodes.append(edge.end)
        return set(end_nodes)

    def get_incoming_nodes(self, node):
        incoming = []
        for edge in self.edges:
            if edge.end == node:
                incoming.append(edge.start)
        return incoming

    def get_probability(self, parameter):
        if len(parameter.condition) == 0:
            return self.get_noisy_probability(parameter)

        probabilities = [1]
        for condition in parameter.condition:
            if condition.value == 2:  # True
                probabilities.append(self.get_noisy_probability(
                    ParameterVariable(parameter.conditional_node, parameter.conditional_value,
                                      [condition])))
        product = reduce(
            lambda p1, p2: (1 - p1)*(1 - p2),
            probabilities)
        product/(1-self.leaky_probability)**(len(self.probabilities)-1)
        if parameter.conditional_value == 2:  # True
            return 1 - (1 - self.leaky_probability) * product
        return (1 - self.leaky_probability) * product

    def get_noisy_probability(self, parameter):
        for prob in self.probabilities:
            if prob.parameter_variable == parameter:
                return prob.probability
        return 1

    # def get_probability(self, parameter):
    #     #for prob in self.probabilities:
    #     #    if prob.parameter_variable == parameter:
    #     #        return prob.probability
    #
    #     cond_node = parameter.conditional_node
    #     cond_value = parameter.conditional_value
    #     cond = parameter.condition
    #     if len(cond) == 0:
    #         if cond_value == 1:
    #             return self.get_prob(ParameterVariable(cond_node,1))
    #         else: return 1 - self.get_prob(ParameterVariable(cond_node,1))
    #     if len(cond) == 1:
    #         x,*_ = cond
    #         if cond_value == 1:
    #             return self.get_prob(ParameterVariable(cond_node,1,[x]))
    #         else:
    #             return (1 - self.get_prob(ParameterVariable(cond_node, 1, [x])))
    #     else:
    #         pr = 0
    #         for c in cond:
    #             if Instance.get_value(c) == 2:
    #                 if pr == 0:
    #                     pr = self.get_probability(
    #                         ParameterVariable(cond_node, 1, [c]))
    #                 else:
    #                     pr = pr * self.get_probability(ParameterVariable(cond_node,1,[c]))
    #             else:
    #                 if pr == 0:
    #                     pr = (1 - self.get_probability(
    #                         ParameterVariable(cond_node, 1, [c])))
    #                 else:
    #                     pr = pr * (1 - self.get_probability(
    #                     ParameterVariable(cond_node, 1, [c])))
    #         if cond_value == 1:
    #             return pr
    #         else: return 1-pr
    #
    # def get_prob(self,parameter):
    #     for prob in self.probabilities:
    #         if prob.parameter_variable == parameter:
    #             return prob.probability
    #     return 100


class Node:
    def __init__(self, name, values=None):
        if values is None:
            values = [1, 2]
        self.name = name
        self.values = values

    def __str__(self):
        return "Node " + self.name

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.name == other.name
        return False

    def __hash__(self):
        return hash(self.name)

    def get_values(self):
        return self.values


class Edge:
    def __init__(self, start, end):
        self.start = start
        self.end = end

