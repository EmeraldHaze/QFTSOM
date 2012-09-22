import types
from core import config


class Settings:
    """
    Stores settings (like defaults), which can be changed and reset.
    """
    def __init__(self, **settings):
        self.default = settings
        for setting, value in settings.items():
            setattr(self, setting, value)

    def reset(self):
        for setting, value in self.default.items():
            setattr(self, setting, value)


def copy_attrs(target, source, *tocopy):
    """
    Copies attributes listed in tocopy from source to target, making new
    instances of str, dict, list objects
    """
    for attr in tocopy:
        value = getattr(source, attr)
        if type(value) in [str, dict, list]:
            value = type(value)(value)
            #This makes a new object with the same content
        setattr(target, attr, value)

###debug levels
def info(*msg):
    if config.DEBUG_LEVEL >= 1:
        print(config.DEBUG_PREFIX, end="")
        print(*msg)


def at(loc):
    if config.DEBUG_LEVEL >= 1:
        print(config.DEBUG_REFIX + "at %s" % loc)


def debug(*msg):
    if config.DEBUG_LEVEL >= 2:
        print(config.DEBUG_PREFIX, end="")
        print(*msg)
