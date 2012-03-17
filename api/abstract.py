class Abstract:
    """Base class for abstract things"""

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name
