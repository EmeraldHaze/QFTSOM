"""
This module sets battle defaults, as well as defaults for some classes
Will eventually include haggel defaults
"""

import lib
from lib.base import rules, exits

players = {}

exits = {"win": exits.win,
        "die":  lib.limb.limbdie}

rules = {"schedule":   rules.speed,
        "get_actions": lib.base.rules.get_all,
        "wipe_hist":   rules.wipe_limbs}

battle = [players, exits, rules]

##Being deafaults
stats = {"speed": 0}
data = {}

##Action defaults
data = {"delay": 0, "target": "norm", "MPC": 0}
