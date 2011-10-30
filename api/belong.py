class Belong:
    def __init__(self, name, stats={}, actions=[], data ={}):
        self.name = name
        self.actions = actions
        self.stats = stats
        self.data = data

    def __str__(self):
        return "<" + self.name + ">"