class Belong:
    def __init__(self, name, stats={}, actions=[], data ={}, datarules = None):
        self.name = name
        self.actions = actions
        self.stats = stats
        self.data = {}
        if not datarules:
            from core import shared
            datarules = shared.belongdata
        for name, value in datarules:
            self.data[name] = eval(value)
        self.data.update(data)

    def __str__(self):
        return "<" + self.name + ">"