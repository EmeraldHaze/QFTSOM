from types import MethodType
from collections import defaultdict
from core.utils import copy
from api import Real, PotentialReal


class RealThinker(Real):
    "Represents a specific thinker of a specific being"
    def __init__(self, parent, being):
        self.name = parent.name
        self.func = MethodType(parent.func, self)
        self.funcinit = MethodType(parent.funcinit, self)
        self.being = being
        self.typed_acts = defaultdict(lambda *a: [])

    def init(self, game):
        self.game = game
        self.funcinit()

    def __call__(self):
        if len(self.being.actions):
            return self.func()
        else:
            from lib.base.actions import null
            return null.instance(self.being, [], self.game)


class Thinker(PotentialReal):
    """
    Represents something that makes discions as to the actions of a being
    Normally one function, think
    """
    inst = RealThinker
    def __init__(self, func, funcinit=(lambda self: None)):
        self.name = func.__name__
        self.func = func
        self.funcinit = funcinit
