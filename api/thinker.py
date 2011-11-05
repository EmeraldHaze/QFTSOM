"""
The Thinker class
"""
from types import MethodType

class Thinker:
    """
    Represents something that makes discions as to the actions of a being
    Normally one function, think
    """
    def __init__(self, func, init = lambda *a:None):
        self.name = func.__name__
        self.func = func
        self.funcinit = init

    def instance(self, player):
        return LimbInst(self, player)

class ThinkerInst:
    """
    Represents a specific thinker of a specific player
    """
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