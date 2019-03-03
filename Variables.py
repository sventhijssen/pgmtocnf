class IndicatorVariable:
    """
    We assume indicator variables are boolean and thus only
    """
    def __init__(self, node, value):
        self.node = node
        self.value = value

    def __str__(self):
        return "lambda_{0}{1}".format(str(self.node.name), str(self.value))

    def __repr__(self):
        return "lambda_{0}{1}".format(str(self.node.name), str(self.value))

    def __eq__(self, other):
        if isinstance(other, IndicatorVariable):
            return self.node == other.node and self.value == other.value
        return False

    def __hash__(self):
        return hash(self.node) ^ hash(self.value)


class ParameterVariable:
    def __init__(self, node, value, incoming=None):
        if incoming is None:
            incoming = []
        self.conditional_node = node
        self.conditional_value = value
        self.condition = incoming

    def __eq__(self, other):
        if isinstance(other, ParameterVariable):
            return self.conditional_node == other.conditional_node and self.conditional_value == other.conditional_value and self.condition == other.condition
        return False

    def _getstr_(self):
        if not self.condition:
            return "theta_{0}{1}".format(str(self.conditional_node.name), str(self.conditional_value))
        else:
            out = "theta_" + str(self.conditional_node.name) + str(self.conditional_value) + "|"
            for i in range(len(self.condition)):
                out += str(self.condition[i].get_node().name)
                out += str(self.condition[i].get_value())
                if i != len(self.condition)-1:
                    out += ","
            return out

    def __str__(self):
        return self._getstr_()

    def __repr__(self):
        return self._getstr_()

    def __hash__(self):
        return hash(self.conditional_node) ^ hash(self.conditional_value)
