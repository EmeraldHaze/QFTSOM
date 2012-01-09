from core import shared


class Rule:
    "Represents a way of doing something. Mainly a wrapper for functions."
    plural = "rules"

    def __init__(self, func, type_=None):
        self.func = func
        self.name = func.name
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
