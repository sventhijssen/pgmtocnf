class Clause:

    def __init__(self, variables=None):
        if variables is None:
            variables = []
        self.variables = variables

    def __add__(self, other):
        self.variables.append(other)

    def __str__(self):
        return " \/ ".join(map(str, self.variables))


class Literal:

    def __init__(self, name, positive=True):
        self.name = name
        self.positive = positive

    def __str__(self):
        if self.positive:
            return str(self.name)
        else:
            return "\+" + str(self.name)

    def __repr__(self):
        if self.positive:
            return str(self.name)
        else:
            return "\+" + str(self.name)

    def __eq__(self, other):
        if isinstance(other, Literal):
            return self.name == other.name
        return False

    def __hash__(self):
        return hash(self.name)

    def negate(self):
        if self.positive:
            return Literal(self.name, False)
        return Literal(self.name, True)


class Equivalence:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def get_implications(self):
        return [Implication(self.left, self.right), Implication(self.right, self.left)]

    def __str__(self):
        return str(self.left) + " <=> " + str(self.right)

    def get_cnf(self):
        return [imp.get_cnf() for imp in self.get_implications()]


class Implication:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def get_clause(self):
        return Clause([Literal(self.left, False), Literal(self.right)])

    def __str__(self):
        return str(self.left) + " => " + str(self.right)

    def get_cnf(self):
        if type(self.right) is not Conjunction and type(self.left) is not Conjunction:
            return [Disjunction([self.left.negate(), self.right])]
        if type(self.right) is Conjunction and type(self.left) is not Conjunction:
            return [Disjunction([self.left.negate(), lit]) for lit in self.right.literals]
        if type(self.right) is not Conjunction and type(self.left) is Conjunction:
            lit = []
            for l in self.left.literals:
                lit.append(l.negate())
            lit.append(self.right)
            return [Disjunction(lit)]
        if type(self.right) is Conjunction and type(self.left) is Conjunction:
            lit = []
            for l in self.left.literals:
                lit.append(l.negate())
            return [Disjunction([lit, lit2]) for lit2 in self.left.literals]


class Conjunction:
    def __init__(self, literals):
        self.literals = literals

    def __str__(self):
        return " /\ ".join(map(str, self.literals))

    def __repr__(self):
        return " /\ ".join(map(str, self.literals))

    def negate(self):
        return Disjunction(lit.negate() for lit in self.literals)


class Disjunction:
    def __init__(self, literals):
        lst = []
        for lit in literals:
            if type(lit) == Disjunction:
                lst.extend(lit.literals)
            else:
                lst.append(lit)
        self.literals = lst
        self.i = -1

    def __str__(self):
        return " \/ ".join(map(str, self.literals))

    def __repr__(self):
        return " \/ ".join(map(str, self.literals))

    def __iter__(self):
        return self

    def __next__(self):
        if(len(self.literals)<self.i+1):
            self.i = self.i + 1
        else:
            raise StopIteration
        return self.literals[self.i]
