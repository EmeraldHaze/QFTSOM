from core import shared
class Rule:
    plural = "rules"
    def __init__(self, func, type_=None):
        self.func = func
        self.info = self.__doc__
        if type_ is None:
            type_ = func.__name__
        self.name = self.type_ = type_
        self.info = self.func.__doc__
        shared.register(self)

    def __call__(self, *args):
        self.func(*args)

    def __str__(self):
        return self.type_ + ": " + self.func.__name__

    __repr__ = __str__

def rule(type_):
    return lambda func:Rule(func, type_)