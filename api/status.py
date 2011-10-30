class Status:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__
    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        else:
            return self.func == other
    def __call__(self, player, battle):
        self.func(player, battle)

