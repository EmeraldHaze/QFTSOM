from collections import defaultdict

registry = defaultdict(lambda :{}, {"rules":defaultdict(lambda :{})})
limb_datarules = []
statrules = []
belongdata = []
name = "no-name"
battle_order = ("players", "exits", "rules")