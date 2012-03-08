from collections import defaultdict

limb_datarules = []
#These rules apply to limb.data

statrules = []
#These rules apply to being.stats

belongdata = []
#These rules apply to belong.data

name = "no-name"
#The player's name, used for logs and suchlike

battle_order = ("beings", "exits", "rules")
#The order in which battle arguments are across the project

#The following items are used for the registry. So that your module's objects
#register right, set current_module to the module's name and add {name: info}
#to modules, by importing shared

modules = {}
current_module = "Not set"
registry = defaultdict(lambda *a: {}, {"rules": defaultdict(lambda *a: {})})
reg_list = []


def register(obj):
    obj.selected = False
    obj.module = current_module
    if not hasattr(obj, "info"):
        obj.info = "This componant has no description."

    reg_list.append(obj)
    if obj.plural == "rules":
        registry["rules"][obj.type_][obj.name] = obj
    else:
        registry[obj.plural][obj.name] = obj


def blank():
    global limb_datarules, statrules, belongdata
    limb_datarules = []
    statrules = []
    belongdata = []
