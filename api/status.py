class Status:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__

    def instance(self, affected):
        return StatusInst(self, affected)

class StatusInst:
    def __init__(self, parent, affected, battle):
        self.func = parent.func
        self.name = parent.name
        self.affected = affected

    def __call__(self):
        self.func(self)

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        else:
            return self.func == other