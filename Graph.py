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


class Node:
    def __init__(self, name, values=None):
        if values is None:
            values = [True, False]
        self.name = name
        self.values = values

    def get_values(self):
        return self.values

    def get_indicator_clauses(self):
        pass


class Edge:
    def __init__(self, start, end):
        self.start = start
        self.end = end

