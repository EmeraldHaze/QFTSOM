from core.utils import copy
from types import MethodType


class Thinker:
    """
    Represents something that makes discions as to the actions of a being
    Normally one function, think
    """
    def __init__(self, func, funcinit=(lambda self: None)):
        self.name = func.__name__
        self.func = func
        self.funcinit = funcinit

    def instance(self, being):
        return ThinkerInst(self, being)


class ThinkerInst:
    "Represents a specific thinker of a specific being"
    def __init__(self, parent, being):
        self.name = parent.name
        self.func = MethodType(parent.func, self)
        self.funcinit = MethodType(parent.funcinit, self)
        self.being = being

    def init(self, battle):
        self.battle = battle
        self.funcinit()

    def __call__(self):
        if len(self.being.actions):
            return self.func()
        else:
            from lib.base.actions import null
            return null.instance(self.being, [], self.battle)
