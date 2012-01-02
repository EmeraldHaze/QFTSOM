from core import shared
class Rule:
    def __init__(self, func, type_=None):
        shared.registry["rules"][type_][func.__name__] = self
        #{"rules":{"schedule":{"next":self}} is what the registry looks like for us
        self.func = func
        if type_ is None:
            type_ = func.__name__
        self.name = self.type_ = type_

    def __call__(self, *args):
        self.func(*args)

def rule(type_):
    return lambda func:Rule(func, type_)