class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges

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


class Node:
    def __init__(self, name, values=None):
        if values is None:
            values = [True, False]
        self.name = name
        self.values = values

    def __str__(self):
        return "Node " + self.name

    def get_values(self):
        return self.values

    def get_indicator_clauses(self):
        pass


class Edge:
    def __init__(self, start, end):
        self.start = start
        self.end = end

