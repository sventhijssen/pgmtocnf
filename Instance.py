class Instance:
    def __init__(self, node, value):
        self.node = node
        self.value = value

    def get_node(self):
        return self.node

    def get_node_name(self):
        return self.node.name

    def get_value(self):
        return self.value

    def __str__(self):
        return str(self.node.name) + str(self.value)

    def __repr__(self):
        return str(self.node.name) + str(self.value)

    def __eq__(self, other):
        if isinstance(other, Instance):
            return self.node == other.node and self.value == other.value
        return False

    def __hash__(self):
        return hash(self.node) ^ self.value
