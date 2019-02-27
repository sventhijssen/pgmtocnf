import itertools

from Instance import Instance
from Logic import Clause, Literal, Conjunction, Equivalence, Disjunction
from Variables import IndicatorVariable, ParameterVariable


class Encoding1:

    def __init__(self, graph):
        self.graph = graph

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

    def get_cnf(self):
        full_cnf = []
        indicator_clauses = self.get_indicator_clauses()
        for i in indicator_clauses:
            full_cnf.append(Disjunction(i.variables))

        parameter_clauses = self.get_parameter_clauses()
        for p in parameter_clauses:  # a parameter clause is an equivalence
            cnf = p.get_cnf()
            for lst in cnf:
                for cjn in lst:
                    full_cnf.append(cjn)

        return full_cnf

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
                    values.append([Literal(IndicatorVariable(i, v)) for v in i.get_values()])
                    conditions.append([Instance(i, v) for v in i.get_values()])
                cs = list(itertools.product(*conditions))  # cartesian

                lst = []
                for tup in cs:
                    l = list(tup)
                    nl = []
                    for v in l:
                        nl.append(Literal(IndicatorVariable(v.get_node(), v.get_value())))
                    lst += [nl + [Literal(IndicatorVariable(node, v)), Literal(ParameterVariable(node, v, l))] for v in node.get_values()]
                #clauses.extend(lst)
                for it in lst:
                    clauses.append((Equivalence(Conjunction(it[:len(it)-1]), it[len(it)-1])))

        return clauses


class Encoding2:

    def __init__(self, graph):
        self.graph = graph

