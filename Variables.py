class IndicatorVariable:
    """
    We assume indicator variables are boolean and thus only
    """
    def __init__(self, node, value):
        self.node = node
        self.value = value

    def __str__(self):
        return "lambda_{0}{1}".format(str(self.node.name), str(self.value))


class ParameterVariable:
    def __init__(self, node, value, incoming_node=None, incoming_value=None):
        self.conditional_node = node
        self.conditional_value = value
        self.condition_node = incoming_node
        self.condition_value = incoming_value

    def __str__(self):
        if not self.condition_node:
            return "theta_{0}{1}".format(str(self.conditional_node.name), str(self.conditional_value))
        else:
            return "theta_{0}{1}|{2}{3}".format(str(self.conditional_node.name), str(self.conditional_value),
                                            str(self.condition_node.name), str(self.condition_value))
