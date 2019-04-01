class Weight:
    def __init__(self, variable, probability):
        self.variable = variable
        self.probability = probability

    def __str__(self):
        return "W({0}) = {1}".format(self.variable, self.probability)

    def __eq__(self, other):
        return self.variable == other.variable

    def __hash__(self):
        return hash(self.variable)
