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


class ParameterVariable:
    def __init__(self, node, value, incoming=None):
        if incoming is None:
            incoming = []
        self.conditional_node = node
        self.conditional_value = value
        self.condition = incoming

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
