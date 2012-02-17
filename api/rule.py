from core import shared

ruletypes = {
    "schedule": ("How a player choice is be scheduled (timeline)", ["player"]),
    "get_actions": ("How to build a player's actionlist", ["player"]),
    "wipe_hist": ("How to remove previous battle history", ["player"]),
    "init": ("What to do once, at first", []),
    "tick": ("What to do each tick", []),
    "being_init": ("What to do when a being is init'd", ["being"])
}

class Rule:
    """
    Represents a way of doing something. Mainly a wrapper for functions.
    These functions are called when the thing the rule is about needs to be
    done, e.g, scheduling someone
    """
    plural = "rules"

    def __init__(self, func, type_=None):
        self.func = func
        self.name = func.__name__
        self.info = self.func.__doc__
        self.type_ = type_
        shared.register(self)

    def __call__(self, *args):
        self.func(*args)

    def __str__(self):
        return self.type_ + ": " + self.name

    __repr__ = __str__


def rule(type_):
    return lambda func: Rule(func, type_)
