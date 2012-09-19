from collections import defaultdict
from types import MethodType

from core.utils import copy, Settings
from api import Real, PotentialReal


class RealAction(Real):
    """Represents a concrete action done by a being to another being(s)"""
    def __init__(self, parent, targets=[], **args):
        copy(self, parent, "name", "data", "actor", "game")
        if type(targets) != list:
            targets = [targets]
        self.targets = targets
        self.args = args
        self.parent = parent
        self.listeners = defaultdict(lambda *a: lambda *a: None)
        for name, listener in parent.listeners.items():
            self.listeners[name] = MethodType(listener, self)

        if not (parent.min_targets <= len(targets) <= parent.max_targets):
            raise Exception("%s tried to %s an invalid amount of targets" % (
                                self.actor.name,
                                self.name
                            ))

        if parent.inverted_targets:
            newtargets = []
            for being in game.beings.values():
                if being not in targets:
                    newtargets.append(target)
            targets = newtargets

    def __repr__(self):
        return "<{}>".format(self.name)


class PotentialAction(PotentialReal):
    """Represents an action that an specific being is capable of doing"""
    inst = RealAction

    def __init__(self, parent, actor, game=None):
        copy(
            self,
            parent,
            "name",
            "listeners",
            "data",
            "max_targets",
            "min_targets",
            "inverted",
            "argsinfo"
        )
        self.parent = parent
        self.actor = actor
        if not game:
            import main
            game = main.game
        self.game = game

    def __repr__(self):
        return "<{}'s potential {}>".format(self.actor.name, self.name)

class AbstractAction(PotentialReal):
    "Represents a potential action that a potential being could do"
    inst = PotentialAction
    defaults = Settings(
        min_targets=1,
        max_targets=1,
        listeners={},
        argsinfo={"targets": "self.being.location.beings"},
        data={}
    )
    def __init__(self, name, listeners, data={}, min_targets=None,
                 max_targets=None, inverted_targets=False, argsinfo=None):
        """
        Represents a possible action. Args:
        name = ""
        listeners = {}, listeners[event] is called at event (e.g, exec)
        data = {}, arbitrary data
        min_targets = 1, minimum targets
        max_targets = 1, -1 = all, -2 = all but one, etc
        inverted_targets = False, selects every being but the targetted ones
        argsinfo = ?, ???
        """

        self.name = name
        self.listeners = defaultdict(
            lambda : (lambda *args: None),
            self.defaults.listeners
        )
        #creates a dict the values of which default to a function that takes
        #any number of args and returns None
        self.listeners.update(listeners)

        if max_targets is None:
            max_targets = self.defaults.max_targets
        if min_targets is None:
            min_targets = self.defaults.min_targets

        if max_targets < min_targets:
            raise Exception(name + "'s max is greater than it's min")

        self.min_targets = min_targets
        self.max_targets = max_targets
        self.inverted_targets = inverted_targets

        self.data = self.defaults.data.copy()
        self.data.update(data)

        if argsinfo is None:
            argsinfo = self.defaults.argsinfo

        if type(argsinfo) is dict:
            argsinfo = list(argsinfo.items())

        self.argsinfo = argsinfo

    def __repr__(self):
        return "<abstract %s>" % self.name

    def __str__(self):
        return self.name

Action = AbstractAction

class ActionFactory:
    def __init__(self, func):
            self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)
