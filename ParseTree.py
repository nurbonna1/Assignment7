class ParseTree:
    def __init__(self, node_type):
        self.node_type = node_type
        self.children = []

    def addChild(self, child):
        self.children.append(child)

    def __repr__(self, level=0):
        ret = "  " * level + f"{self.node_type}\n"
        for child in self.children:
            if isinstance(child, ParseTree):
                ret += child.__repr__(level + 1)
            else:
                ret += "  " * (level + 1) + repr(child) + "\n"
        return ret
