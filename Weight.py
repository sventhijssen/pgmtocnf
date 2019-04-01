class Weight:
    def __init__(self, variable, probability):
        self.literal = variable
        self.probability = probability

    def __str__(self):
        return "W({0}) = {1}".format(self.literal, self.probability)

    def __eq__(self, other):
        return self.literal == other.literal

    def __hash__(self):
        return hash(self.literal)
