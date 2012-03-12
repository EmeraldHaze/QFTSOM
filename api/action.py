from collections import defaultdict
from inspect import getargspec

from core.utils import copy
from game import defaults
from api import Real, PotentialReal


class RealAction(Real):
    """Represents a concrete action done by a being to another being(s)"""
    def __init__(self, parent, targets=[], **args):
        if type(targets) != list:
            targets = [targets]

        if not (parent.min_targets <= len(targets) <= parent.max_targets):
            raise Exception("%s tried to %s an invalid amount of targets" % (
                                self.actor.name,
                                self.name
                            ))

        if parent.inverted:
            newtargets = []
            for being in battle.beings.values():
                if being not in targets:
                    newtargets.append(target)
            targets = newtargets

        copy(self, parent, "name", "listeners", "data", "actor", "battle")
        self.args = args
        self.targets = targets
        self.parent = parent
        self.listeners["init"](self)

    def __repr__(self):
        return "<{}>".format(self.name)


class PotentialAction(PotentialReal):
    """Represents an action that an specific being is capable of doing"""
    inst = RealAction

    def __init__(self, parent, actor, battle):
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
        self.battle = battle

    def __repr__(self):
        return "<{}'s potential {}>".format(self.actor.name, self.name)

class AbstractAction(PotentialReal):
    inst = PotentialAction

    def __init__(self, name, listeners, data={},
                 min_targets=1, max_targets=1, inverted=False, argsinfo=None):
        """
        Represents a possible action. Args:
        name: str
        listeners:dict, listeners[event] is called at event (e.g, exec)
        data = {}, arbitrary data
        min_targets = 1, minimum targets
        max_targets = 1, -1 = all, -2 = all but one, etc
        """

        self.name = name
        self.listeners = defaultdict(
            lambda *a: (lambda *args: None),
            defaults.actions.listeners
        )
        self.listeners.update(listeners)

        if max_targets < min_targets:
            raise Exception(name + "'s max is greater than it's min")

        self.min_targets = min_targets
        self.max_targets = max_targets
        self.inverted = inverted

        self.data = defaults.actions.data.copy()
        self.data.update(data)

        if not argsinfo:
            argsinfo = {"targets": "self.battle.beings"}
        self.argsinfo = argsinfo

    def __repr__(self):
        return "<%s>" % self.name

Action = AbstractAction

class ActionFactory:
    def __init__(self, func):
            self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)
