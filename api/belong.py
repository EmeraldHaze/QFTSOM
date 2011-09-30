class Belong:
    def __init__(self, name, stats={}, actions=[]):
        self.name = name
        self.actions = actions
        self.stats = stats

    def __str__(self):
        return "<" + self.name + ">"