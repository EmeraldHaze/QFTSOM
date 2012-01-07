import lib
from lib.base import rules, exits
players = {}
exits = {"win":exits.win, "die":lib.limb.limbdie}
rules = {"schedule":rules.speed,
        "get_actions":lib.base.rules.get_all,
        "wipe_hist":rules.wipe_limbs}
battle = [players, exits, rules]