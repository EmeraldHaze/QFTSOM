"""
This module defines the Defaults class which is used to provide defaults
for several classes (Beings, etc) and objects (Battles, eventually Haggles)
"""

class Defaults:
    """
    This is a class used for various defaults
    It supports lazy values, so that values based on objects with default
    vaules of their own work
    """
    def __init__(self, **kwargs):
        self.defaults = kwargs
        self.made = {}
        #As not to calculate things twice

    def __getattr__(self, attr):
        if attr in self.made:
            return self.made[attr]
        else:
            if attr in self.defaults:
                value = self.defaults[attr]
                try:
                    #This works if it's lazy
                    value = value(self)
                    self.made[attr] = value
                    return value
                except TypeError:
                    #If it's not callable, e.g., not lazy
                    return self.defaults[attr]


beings = lambda self: {}

def exits(self):
    import lib
    return {
        "win": lib.base.exits.win,
        "die": lib.limb.limbdie
        }

def rules(self):
    from lib.base import rules
    return {
        "schedule": rules.speed,
        "get_actions": rules.get_all,
        "wipe_hist": rules.wipe_limbs
        }

battle = Defaults(
    beings=beings,
    exits=exits,
    rules=rules,
    args=lambda self: [self.beings, self.exits, self.rules]
    )

beings = Defaults(stats={"speed": 0}, data={})

actions = Defaults(data={"delay": 0, "target": "norm", "MPC": 0})
