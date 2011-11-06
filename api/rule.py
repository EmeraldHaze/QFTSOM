class Rule:
    def __init__(self, func, type_=None):
        self.func = func
        if type_ is None:
            type_ = func.__name__
        self.name = self.type_ = type_

    def __call__(self, *args):
        self.func(*args)

def rule(type_):
    return lambda func:Rule(func, type_)