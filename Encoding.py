import itertools
import re

from Instance import Instance
from Logic import Clause, Literal, Conjunction, Equivalence, Disjunction, Implication
from Variables import IndicatorVariable, ParameterVariable
from Weight import Weight


class Encoding1:

    def __init__(self, graph):
        self.graph = graph

    def __str__(self):
        out = "-----ENC1------\n"
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
            # print(p)
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
                clause.__add__(Literal(IndicatorVariable(node, i + 1)))
            clauses.append(clause)

        for node in self.graph.nodes:
            for i in range(len(node.get_values())):
                for j in range(i + 1, len(node.get_values())):
                    clause = Clause()
                    clause.__add__(Literal(IndicatorVariable(node, i + 1), False))
                    clause.__add__(Literal(IndicatorVariable(node, j + 1), False))
                    clauses.append(clause)

        return clauses

    def get_parameter_clauses(self):
        clauses = []
        equivalences = []
        for node in self.graph.nodes:
            # if no edge incoming in the node
            if node not in self.graph.get_end_nodes():
                for i in range(len(node.get_values())):
                    equivalences.append(
                        Equivalence(Literal(IndicatorVariable(node, i + 1)), Literal(ParameterVariable(node, i + 1))))

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
                    lst += [nl + [Literal(IndicatorVariable(node, v)), Literal(ParameterVariable(node, v, l))] for v in
                            node.get_values()]
                # clauses.extend(lst)
                for it in lst:
                    clauses.append((Equivalence(Conjunction(it[:len(it) - 1]), it[len(it) - 1])))

        return clauses

    def get_all_variables(self):
        return set(itertools.chain(*[disjunction.literals for disjunction in self.get_cnf()]))

    def get_dimacs_map(self):
        variables = self.get_all_variables()
        numbers = [i + 1 for i in range(len(variables))]
        return dict(zip(variables, numbers))

    def export_to_dimacs(self, filename):
        dimacs_enc = self.get_dimacs_map()

        file = open(filename, "w")
        file.write("c ENC1\n")
        file.write("p cnf " + str(len(self.get_all_variables())) + " " + str(len(self.get_cnf())) + "\n")

        for disjunction in self.get_cnf():
            for lit in disjunction.literals:
                if lit.positive:
                    file.write(str(dimacs_enc[lit]))
                else:
                    file.write(str(-dimacs_enc[lit]))
                file.write(" ")
            file.write(str(0))
            file.write("\n")
        file.close()

    def get_weights(self):
        weights = []
        for literal in self.get_all_variables():
            if type(literal.name) == ParameterVariable:
                weights.append(Weight(literal, True, self.graph.get_probability(literal.name)))
                weights.append(Weight(literal, False, 1))
            else:
                weights.append(Weight(literal, True, 1))
                weights.append(Weight(literal, False, 1))
        return weights

    def export_enc_to_latex(self, filename):
        file = open(filename, "w")
        for clause in self.get_cnf():
            file.write('$')
            for i in range(len(clause.literals)):
                m = re.match(r"([a-z]+)_([a-z0-9]+(?:\|[a-z0-9]+)*)", str(clause.literals[i].name))
                if not clause.literals[i].positive:
                    file.write('\\neg')
                file.write('\\{0}_{{{1}}}'.format(m.group(1), m.group(2)))
                if i < len(clause.literals)-1:
                    file.write(' \\vee ')
            file.write('$')
            file.write('\\\\\n')
        file.close()

    def export_weights_to_latex(self, filename):
        file = open(filename, "w")
        for weight in self.get_weights():
            file.write('$')
            m = re.match(r"([a-z]+)_([a-z0-9]+(?:\|[a-z0-9]+)*)", str(weight.variable))
            if weight.positive:
                file.write('W(\\{0}_{{{1}}})={2}'.format(m.group(1), m.group(2), weight.probability))
            else:
                file.write('W(\\neg\\{0}_{{{1}}})={2}'.format(m.group(1), m.group(2), weight.probability))
            file.write('$')
            file.write('\\\\\n')
        file.close()


class Encoding2:

    def __init__(self, graph):
        self.graph = graph

    def __str__(self):
        out = "---ENC2---\n"
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
        for p in parameter_clauses:  # a parameter clause is an implication
            #print(p)
            cnf = p.get_cnf()
            #print(cnf)
            for lst in cnf:
                full_cnf.append(lst)

        return full_cnf

    def get_clauses(self):
        return self.get_indicator_clauses() + self.get_parameter_clauses()

    # indicator clauses of ENC2 are the same as ENC1
    def get_indicator_clauses(self):
        clauses = []
        for node in self.graph.nodes:
            clause = Clause()
            for i in range(len(node.get_values())):
                clause.__add__(Literal(IndicatorVariable(node, i + 1)))
            clauses.append(clause)

        for node in self.graph.nodes:
            for i in range(len(node.get_values())):
                for j in range(i + 1, len(node.get_values())):
                    clause = Clause()
                    clause.__add__(Literal(IndicatorVariable(node, i + 1), False))
                    clause.__add__(Literal(IndicatorVariable(node, j + 1), False))
                    clauses.append(clause)

        return clauses

    def get_parameter_clauses(self):
        clauses = []
        implications = []
        for node in self.graph.nodes:
            # if no edge incoming in the node
            if node not in self.graph.get_end_nodes():
                parameters = []
                for i in range(len(node.get_values())):

                    parameterscopy = parameters.copy()
                    if i < len(node.get_values()) - 1:
                        parameterscopy.append(Literal(ParameterVariable(node, i + 1), True))

                    implications.append(
                        Implication(Conjunction(parameterscopy), Literal(IndicatorVariable(node, i + 1))))

                    if i < len(node.get_values()) - 1:
                        parameters.append(parameterscopy[-1].negate())

                clauses.extend(implications)

            # edges coming into the node
            else:
                values = []
                conditions = []
                for i in self.graph.get_incoming_nodes(node):
                    values.append([Literal(IndicatorVariable(i, v)) for v in i.get_values()])
                    conditions.append([Instance(i, v) for v in i.get_values()])
                cs = list(itertools.product(*conditions))  # cartesian

                for tup in cs:
                    parameters = []
                    i = 0
                    for v in node.get_values():
                        i = i + 1
                        l = list(tup)
                        nl = []
                        for p in l:
                            nl.append(Literal(IndicatorVariable(p.get_node(), p.get_value())))
                        parameterscopy = parameters.copy()
                        if i < len(node.get_values()):
                            parameterscopy.append(Literal(ParameterVariable(node, v, l)))
                        if i < len(node.get_values()):
                            parameters.append(Literal(ParameterVariable(node, v, l), False))
                        clauses.append(
                            (Implication(Conjunction(nl + parameterscopy), Literal(IndicatorVariable(node, v)))))

        return clauses

    def get_all_variables(self):
        return set(itertools.chain(*[disjunction.literals for disjunction in self.get_cnf()]))

    def get_dimacs_map(self):
        variables = self.get_all_variables()
        numbers = [i + 1 for i in range(len(variables))]
        return dict(zip(variables, numbers))

    def export_to_dimacs(self, filename):
        dimacs_enc = self.get_dimacs_map()

        file = open(filename, "w")
        file.write("c ENC2\n")
        file.write("p cnf " + str(len(self.get_all_variables())) + " " + str(len(self.get_cnf())) + "\n")

        for disjunction in self.get_cnf():
            for lit in disjunction.literals:
                if lit.positive:
                    file.write(str(dimacs_enc[lit]))
                else:
                    file.write(str(-dimacs_enc[lit]))
                file.write(" ")
            file.write(str(0))
            file.write("\n")
        file.close()

    def get_weights(self):
        weights = []
        variables = list(self.get_all_variables())
        vars_map = {}
        for literal in variables:
            if type(literal.name) == ParameterVariable:
                pv = literal.name
                if not (pv.condition, pv.conditional_node.name) in vars_map.keys():
                    vars_map[(pv.condition, pv.conditional_node.name)] = [pv]
                else:
                    vars_map[(pv.condition, pv.conditional_node.name)].append(pv)

        # Create an ordered domain
        for k, v in vars_map.items():
            vars_map[k] = sorted(v, key=lambda x: x.conditional_value)

        for k in vars_map.keys():
            if len(vars_map[k]) > 1:
                s = 0
                for i in range(len(vars_map[k])):
                    literal = vars_map[k][i]
                    weights.append(Weight(literal, True, self.graph.get_probability(literal)/(1-s)))
                    weights.append(Weight(literal, False, 1-(self.graph.get_probability(literal) / (1 - s))))
                    s += self.graph.get_probability(literal)
            #else:
               # weights.append(Weight(literal, True, ))

        for w in weights:
            print(w)


        # for literal in vars:
        #     print(literal)
            # if type(literal.name) == ParameterVariable:
            #     weights.append(Weight(literal, True, self.graph.get_probability(literal.name)))
            #     weights.append(Weight(literal, False, 1))
        #     else:
        #         weights.append(Weight(literal, True, 1))
        #         weights.append(Weight(literal, False, 1))
        # return weights

    def export_enc_to_latex(self, filename):
        file = open(filename, "w")
        for clause in self.get_cnf():
            file.write('$')
            for i in range(len(clause.literals)):
                m = re.match(r"([a-z]+)_([a-z0-9]+(?:\|[a-z0-9]+)*)", str(clause.literals[i].name).replace('theta', 'rho'))
                if not clause.literals[i].positive:
                    file.write('\\neg')
                file.write('\\{0}_{{{1}}}'.format(m.group(1), m.group(2)))
                if i < len(clause.literals)-1:
                    file.write(' \\vee ')
            file.write('$')
            file.write('\\\\\n')
        file.close()

    def export_weights_to_latex(self, filename):
        file = open(filename, "w")
        for weight in self.get_weights():
            file.write('$')
            v = str(weight.variable)
            v.replace('theta', 'rho')
            m = re.match(r"([a-z]+)_([a-z0-9]+(?:\|[a-z0-9]+)*)", v)
            if weight.positive:
                file.write('W(\\{0}_{{{1}}})={2}'.format(m.group(1), m.group(2), weight.probability))
            else:
                file.write('W(\\neg\\{0}_{{{1}}})={2}'.format(m.group(1), m.group(2), weight.probability))
            file.write('$')
            file.write('\\\\\n')
        file.close()
