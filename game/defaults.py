"""
This module defines the Defaults class which is used to provide defaults
for several classes (Beings, etc) and objects (Battles, eventually Haggles)
"""

from importlib import import_module

class Defaults:
    """
    This is a class used for various defaults. It supports lazy values, so
    that values based on objects with default vaules of their own work.
    """
    def __init__(self, req, defaults):
        self.defaults = defaults
        self.req = req
        self._module = False
        self.made = {}
        #As not to calculate things twice

    @property
    def module(self):
        """
        The module(s) from which this collection of defaults draws it's values
        '"""
        if self._module is not False:
            return self._module
        else:
            if type(self.req) is list:
                self._module = {}
                for mod in self.req:
                    self._module[mod.split(".")[-1]] = import_module(mod)
            elif type(self.req) is str:
                self._module = import_module(self.req)
            else:
                self._module = None
            return self._module

    def __getattr__(self, attr):
        if attr in self.made:
            return self.made[attr]
        else:
            value = self.defaults[attr]
            if "__call__" in dir(value):
                #if it has a call interface,  and is therefor lazy
                value = value(self.module)
                #call it with it's module, which is also lazily imported
                self.made[attr] = value
                return value
            else:
                #If it's not not lazy
                self.made[attr] = value
                return value

##Classes
beings = Defaults(None, {"stats": {"speed": 0}, "data": {}})

actions = Defaults("lib.base.actions", {
    "data": {"delay": 0, "target": "norm", "MPC": 0},
    "listeners": lambda m: {"choosen": m.basic_choosen},
    })

##Other

battle = Defaults(["lib.base.rules", "lib.base.exits", "lib.limb", "game.defaults"], {
    "beings": {},
    "exits": lambda m: {
            "win": m["exits"].win,
            "die": m["limb"].limbdie
        },
    "rules": lambda m: {
            "schedule":     m["rules"].speed,
            "get_actions":  m["rules"].get_all,
            "wipe_hist":    m["rules"].wipe_limbs
        },
    "args": lambda m: [
        m["defaults"].battle.beings,
        m["defaults"].battle.exits,
        m["defaults"].battle.rules
    ]
})

