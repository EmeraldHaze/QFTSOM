from api.abstract import Abstract

class Exit(Abstract):
    """
    This represents a possible way to exit a battle, and the consqeuances
    of doing so. It has a condition function that should return whether
    the given being exited or not, and an effect (consequance) function.
    It should also list it's dependancies (what the condition depends on)
    and what the effect changes
    '"""
    def __init__(self, name, condition, effect=None, deps=None, changes=None):
        self.name = name
        self.condition = condition
        self.effect = effect or (lambda p, b: None)
        self.deps = deps or []
        self.changes = changes or []

    def __str__(self):
        return self.name

    __repr__ = __str__
