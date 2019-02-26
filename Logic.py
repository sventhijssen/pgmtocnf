class Clause:

    def __init__(self):
        self.variables = []

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
            return "-" + str(self.name)


class Equivalence:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def get_implications(self):
        return [Implication(self.left, self.right), Implication(self.right, self.left)]


class Implication:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def get_cnfs(self):
        return "-" + self.left


class Conjunction:
    def __init__(self, literals):
        self.literals = literals


class Disjunction:
    def __init__(self, literals):
        self.literals = literals
