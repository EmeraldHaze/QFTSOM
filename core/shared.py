from collections import defaultdict

limb_datarules = []
statrules = []
belongdata = []
name = "no-name"
battle_order = ("players", "exits", "rules")

modules = {}
current_module = "Not set"
registry = defaultdict(lambda :{}, {"rules":defaultdict(lambda :{})})
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