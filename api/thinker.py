from types import MethodType

class Thinker:
    def __init__(self, func, init = lambda *a:None):
        self.name = func.__name__
        self.func = func
        self.funcinit = init

    def instance(self, player):
        return LimbInst(self, player)

class ThinkerInst:
    def __init__(self, parent, player):
        self.name = parent.name
        self.func = MethodType(parent.func, self)
        self.init = parent.init
        self.player = player

    def init(self, battle):
        self.battle = battle
        self.funcinit()

    def __call__(self):
        self.func()