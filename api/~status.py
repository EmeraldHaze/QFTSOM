class Status:
    "Represents a possible status of a being (e.g, poison)"
    def __init__(self, func):
        self.func = func
        self.name = func.__name__

    def instance(self, being, battle):
        return StatusInst(self, being, battle)


class StatusInst:
    "Represents a status of a specific person"
    def __init__(self, parent, being, battle):
        self.func = parent.func
        self.name = parent.name
        self.being = being

    def __call__(self):
        self.func(self)

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        else:
            return self.func == other
