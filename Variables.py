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
    def __init__(self, node, value, incoming_nodes=None, incoming_values=None):
        if incoming_values is None:
            incoming_values = []
        if incoming_nodes is None:
            incoming_nodes = []
        self.conditional_node = node
        self.conditional_value = value
        self.condition_nodes = incoming_nodes
        self.condition_values = incoming_values

    def _getstr_(self):
        if not self.condition_nodes:
            return "theta_{0}{1}".format(str(self.conditional_node.name), str(self.conditional_value))
        else:
            out = "theta_" + str(self.conditional_node.name) + str(self.conditional_value) + "|"
            for i in range(len(self.condition_nodes)):
                out += str(self.condition_nodes[i].name)
                out += str(self.condition_values[i])
                if i != len(self.condition_nodes):
                    out += ","
            return out

    def __str__(self):
        return self._getstr_()

    def __repr__(self):
        return self._getstr_()
