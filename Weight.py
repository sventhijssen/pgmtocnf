class Weight:
    def __init__(self, variable, positive, probability):
        self.variable = variable
        self.positive = positive
        self.probability = probability

    def __str__(self):
        if self.positive:
            return "W({0}) = {1}".format(self.variable, self.probability)
        return "W(\\+{0}) = {1}".format(self.variable, self.probability)
