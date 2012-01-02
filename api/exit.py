from core import shared
class Exit:
    """This represents a possible way to get out of a battle, and the
    consqeuances of doing so. Has a condition function that should return
    weather the given player exited or not, and an effect function"""
    def __init__(self, name, condition, effect=(lambda p, b: None), deps = [], changes = []):
        shared.registry["exits"][name] = self
        self.name = name
        self.condition = condition
        self.effect = effect
        self.deps = deps
        self.changes = changes
