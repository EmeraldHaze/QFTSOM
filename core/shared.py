from collections import defaultdict

class Settings:
    def __init__(self, **settings):
        self.default = settings
        for setting, value in settings.items():
            setattr(self, setting, value)

    def blank(self):
        for setting, value in self.default.items():
            setattr(self, setting, value)


rules = Settings(
    limb_data=[],
    being_stats=[],
    item_data=[]
)

misc = Settings(
    base_actions=[]
)

actions = Settings(
    min_targets=1,
    max_targets=1,
    listeners={},
    argsinfo={"targets": "self.being.location.beings"},
    data={}
)
name = "no-name"


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

