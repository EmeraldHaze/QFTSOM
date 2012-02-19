from core import shared


class Exit:
    """
    This represents a possible way to exit a battle, and the consqeuances
    of doing so. It has a condition function that should return whether
    the given being exited or not, and an effect (consequance) function.
    It should also list it's dependancies (what the condition depends on)
    and what the effect changes
    '"""
    plural = "exits"

    def __init__(self, name, condition,
            effect=(lambda p, b: None), deps=[], changes=[]):
        self.name = name
        self.condition = condition
        self.effect = effect
        self.deps = deps
        self.changes = changes
        shared.register(self)

    def __str__(self):
        return self.name

    __repr__ = __str__
