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

    def get_all_literals(self):
        literals_list = [disjunction.literals for disjunction in self.get_cnf()]
        literals = list(itertools.chain(*literals_list))
        return literals

    def get_all_variables(self):
        literals = self.get_all_literals()
        return set([literal.atom for literal in literals])

    def get_dimacs_map(self):
        variables = self.get_all_variables()
        numbers = [i + 1 for i in range(len(variables))]
        return dict(zip(variables, numbers))

    def export_to_dimacs(self, filename):
        dimacs_enc = self.get_dimacs_map()

        file = open(filename, "w")
        file.write("c ENC1\n")
        file.write("c weights ")
        positive_weights = []
        negative_weights = []
        for key in dimacs_enc.keys():  # we assume the dimacs encoding is sorted from 1..N
            for w in self.get_weights():
                if w.literal.atom == key:
                    if w.literal.positive:
                        positive_weights.append(w.probability)
                    else:
                        negative_weights.append(w.probability)

        for i in range(len(positive_weights)):
            file.write(str(positive_weights[i]))
            file.write(" ")
            file.write(str(negative_weights[i]))
            if i < len(positive_weights)-1:
                file.write(" ")
            else:
                file.write("\n")

        file.write("p cnf " + str(len(self.get_all_variables())) + " " + str(len(self.get_cnf())) + "\n")

        for disjunction in self.get_cnf():
            for literal in disjunction.literals:
                if literal.positive:
                    file.write(str(dimacs_enc[literal.atom]))
                else:
                    file.write(str(-dimacs_enc[literal.atom]))
                file.write(" ")
            file.write(str(0))
            file.write("\n")
        file.close()

    def get_weights(self):
        weights = []
        for literal in self.get_all_literals():
            if type(literal.atom) == ParameterVariable:
                if literal.positive:
                    weights.append(Weight(literal, self.graph.get_probability(literal.atom)))
                else:
                    weights.append(Weight(literal, 1))
            else:
                if literal.positive:
                    weights.append(Weight(literal, 1))
                else:
                    weights.append(Weight(literal, 1))
        return set(weights)

    def export_enc_to_latex(self, filename):
        file = open(filename, "w")
        for clause in self.get_cnf():
            file.write('$')
            for i in range(len(clause.literals)):
                m = re.match(r"([A-Za-z]+)_([A-Za-z0-9]+(?:\|[A-Za-z0-9]+)*)", str(clause.literals[i].atom))
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
            if weight.literal.positive:
                m = re.match(r"([A-Za-z]+)_([A-Za-z0-9]+(?:\|[A-Za-z0-9]+)*)", str(weight.literal))
                file.write('W(\\{0}_{{{1}}})={2}'.format(m.group(1), m.group(2), weight.probability))
            else:
                m = re.match(r"\\\+([A-Za-z]+)_([A-Za-z0-9]+(?:\|[A-Za-z0-9]+)*)", str(weight.literal))
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

    def get_all_literals(self):
        literals_list = [disjunction.literals for disjunction in self.get_cnf()]
        literals = list(itertools.chain(*literals_list))
        return literals

    def get_all_variables(self):
        literals = self.get_all_literals()
        return set([literal.atom for literal in literals])

    # def get_all_variables(self):
    #     return set(itertools.chain(*[disjunction.literals for disjunction in self.get_cnf()]))

    def get_dimacs_map(self):
        variables = self.get_all_variables()
        numbers = [i + 1 for i in range(len(variables))]
        return dict(zip(variables, numbers))

    def export_to_dimacs(self, filename):
        dimacs_enc = self.get_dimacs_map()

        file = open(filename, "w")
        file.write("c ENC2\n")
        file.write("c weights ")
        positive_weights = []
        negative_weights = []
        for key in dimacs_enc.keys():  # we assume the dimacs encoding is sorted from 1..N
            for w in self.get_weights():
                if w.literal.atom == key:
                    if w.literal.positive:
                        positive_weights.append(w.probability)
                    else:
                        negative_weights.append(w.probability)

        for i in range(len(positive_weights)):
            file.write(str(positive_weights[i]))
            file.write(" ")
            file.write(str(negative_weights[i]))
            if i < len(positive_weights)-1:
                file.write(" ")
            else:
                file.write("\n")
        file.write("p cnf " + str(len(positive_weights)) + " " + str(len(self.get_cnf())) + "\n")

        for disjunction in self.get_cnf():
            for literal in disjunction.literals:
                if literal.positive:
                    file.write(str(dimacs_enc[literal.atom]))
                else:
                    file.write(str(-dimacs_enc[literal.atom]))
                file.write(" ")
            file.write(str(0))
            file.write("\n")
        file.close()

    def get_weights(self):
        weights = []
        literals = list(self.get_all_literals())
        vars_map = {}
        for literal in literals:
            if type(literal.atom) == ParameterVariable:
                pv = literal.atom
                if not (pv.condition, pv.conditional_node.name) in vars_map.keys():
                    vars_map[(pv.condition, pv.conditional_node.name)] = [literal]
                else:
                    vars_map[(pv.condition, pv.conditional_node.name)].append(literal)

        # Create an ordered domain
        for k, v in vars_map.items():
            vars_map[k] = sorted(v, key=lambda x: x.atom.conditional_value)

        for k in vars_map.keys():
            s1 = 0
            s2 = 0
            for i in range(len(vars_map[k])):
                literal = vars_map[k][i]
                if literal.positive:
                    weights.append(Weight(literal, self.graph.get_probability(literal.atom)/(1-s1)))
                    s1 += self.graph.get_probability(literal.atom)
                else:
                    weights.append(Weight(literal, 1-(self.graph.get_probability(literal.atom) / (1 - s2))))
                    s2 += self.graph.get_probability(literal.atom)

        for literal in literals:
            if type(literal.atom) == IndicatorVariable:
                weights.append(Weight(literal, 1))
                #weights.append(Weight(literal, 1))
        return set(weights)

    def export_enc_to_latex(self, filename):
        file = open(filename, "w")
        for clause in self.get_cnf():
            file.write('$')
            for i in range(len(clause.literals)):
                m = re.match(r"([A-Za-z]+)_([A-Za-z0-9]+(?:\|[A-Za-z0-9]+)*)", str(clause.literals[i].atom).replace('theta', 'rho'))
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
            v = str(weight.literal)
            v.replace('theta', 'rho')
            if weight.literal.positive:
                m = re.match(r"([A-Za-z]+)_([A-Za-z0-9]+(?:\|[A-Za-z0-9]+)*)", v)
                file.write('W(\\{0}_{{{1}}})={2}'.format(m.group(1), m.group(2), weight.probability))
            else:
                m = re.match(r"\\\+([A-Za-z]+)_([A-Za-z0-9]+(?:\|[A-Za-z0-9]+)*)", v)
                file.write('W(\\neg\\{0}_{{{1}}})={2}'.format(m.group(1), m.group(2), weight.probability))
            file.write('$')
            file.write('\\\\\n')
        file.close()
