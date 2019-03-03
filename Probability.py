from Graph import Node
from Instance import Instance
from Variables import ParameterVariable


class Probability:

    def __init__(self, instance, probability, conditions=None):
        # Prob(a) = p, non-conditional
        if not conditions:
            self.parameter_variable = ParameterVariable(instance[0], instance[1])

        # Prob(a|x1,x2,...xn) = p, conditional
        else:
            self.parameter_variable = ParameterVariable(instance[0], instance[1], [Instance(c[0], c[1]) for c in conditions])

        self.probability = probability
