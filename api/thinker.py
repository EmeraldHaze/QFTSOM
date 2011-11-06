"""
The Thinker class
"""
from core.utils import copy
from types import MethodType

class Thinker:
    """
    Represents something that makes discions as to the actions of a being
    Normally one function, think
    """
    def __init__(self, func, funcinit = lambda self:None):
        self.name = func.__name__
        self.func = func
        self.funcinit = funcinit

    def instance(self, player):
        return ThinkerInst(self, player)

class ThinkerInst:
    """
    Represents a specific thinker of a specific player
    """
    def __init__(self, parent, player):
        self.name = parent.name
        self.func = MethodType(parent.func, self)
        self.funcinit = MethodType(parent.funcinit, self)
        self.player = player

    def init(self, battle):
        self.battle = battle
        self.funcinit()

    def __call__(self):
        return self.func()