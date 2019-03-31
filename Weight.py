class Weight:
    def __init__(self, variable, probability):
        self.variable = variable
        self.probability = probability

    def __str__(self):
        return "W({0}) = {1}".format(self.variable, self.probability)
