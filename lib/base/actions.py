from api import Action, ActionFactory
from random import randint
from core import shared

shared.actions.max_targets = 0
shared.actions.min_targets = 0
shared.actions.argsinfo = {}
def sexec(self):
        target = self.targets[0]
        dmg = self.data["dmg"]
        print(target.name, "has lost", dmg, "health!")
        target.stats["HP"] -= dmg

@ActionFactory
def simplemaker(name, dmg):
    return Action(name, {"exec": sexec}, {"dmg": dmg, "speed": 1, "type": "attack"})


def complete_exec(self):
    rules = self.dmgrules
    if "status" in self.data:
        status = self.data["status"].instance(
            self.targets[0],
            self.battle,
            **self.data["status_data"]
        )
        self.targets[0].status_list.append(status)
    for target in self.targets:
        dmg = eval(rules[self.data["type"]])
        target.stats["HP"] -= dmg
        print(target.name, "lost", dmg, "health!")


def manainit(self):
    self.actor.stats['MP'] -= self.data["MPC"]


def basic_choosen(action):
    print("{} has {}'d {}!".format(
                        action.actor.name,
                        action.name,
                        ', '.join([target.name for target in action.targets])
                    )
                )


def move_exec(self):
    being = self.actor
    dest = self.args["go where"]
    loc = being.location
    if dest in loc.links.values():
        loc.beings.remove(being)
        dest.beings.append(being)
        being.location = dest
        print(being.name, "has moved too", dest.name)
        if being.name is shared.name:
            print(dest.info)
    else:
        print("Bad location")

move = Action(
    "move",
    {"exec": move_exec, "choosen": lambda a: None},
    {"speed": 1, "type": "move"},
    argsinfo={"go where": "self.being.location.links"}
)

null = Action(
    "pass",
    {
        "exec": (lambda self: print("%s does nothing." % self.actor.name)),
        "choosen": (lambda self: print("%s passes." % self.actor.name))
    },
    {"speed": 1, "type": "misc"}
)

def equip_init(self):
    if self.args["item"] in self.actor.items and\
       self.args["limb"] in self.actor.limbs and\
       self.args["item"].equip is self.args["limb"].equip:
        self.data["speed"] = 1
    else:
        self.data["speed"] = 0

equip = Action(
    "equip",
    {
        "exec": (
            lambda s: print(s.actor.equip(s.args["item"], s.args["limb"])[1])
        ),
        "choosen": lambda s: None,
        "init": equip_init
    },
    {"speed": 0, "type": "items"},
    argsinfo=[("item", "self.being.items"), ("limb", "self.being.limbs")]
)

unequip = Action(
    "unequip",
    {
        "exec": (
            lambda s: print(s.actor.equip(
                s.args["item"].name,
                s.args["limb"].name
            )[1])
        ),
        "choosen": lambda s: None
    },
    {"speed": 0, "type": "items"},
    argsinfo=[("item", "self.being.items")]
)

def look_init(self):
    loc = self.actor.location
    print(loc.info)
    print("Beings in", loc.name)
    for n, being in enumerate(loc.beings):
        print(str(n) + ".", being.name + ", HP:", being.stats["HP"])
    if loc.items:
        print("Items in", loc.name)
        for n, item in enumerate(loc.items):
            print(str(n) + ".", item.name.capitalize())
    else:
        print("There are no items in", loc.name)

look = Action(
    "look",
    {
        "init": look_init,
        "choosen": lambda s: None
    },
    {"delay": 0, "speed": -1, "type": "misc"},
    #-1 speed compensates for waiting for the turn after it's executed
)

def pickup_exec(self):
    item = self.args["item"]
    self.actor.additem(item)
    self.actor.location.items.remove(item)
    print(self.actor.name, "picked up", item.name)

pickup = Action(
    "pick up",
    {"exec": pickup_exec},
    {"speed": 1, "type": "items"},
    argsinfo={"item": "self.being.location.items"})

def drop_exec(self):
    item = self.args["item"]
    if item in self.actor.equipped:
        print(self.actor.unequip(item.name))
    self.actor.rmitem(item)
    self.actor.location.items.append(item)
    print(self.actor.name, "dropped", item.name)

drop = Action(
    "drop",
    {"exec": drop_exec},
    {"speed": 1, "type": "items"},
    argsinfo={"item": "self.being.items"})

def viewinv_init(self):
    if self.actor.items:
        print("Your items:")
        for n, item in enumerate(self.actor.items):
            msg = item.name.capitalize()
            if item.limb:
                msg += ", which is equipped to your " + item.limb.name + ". "
            else:
                prefix = "a" + "n" if item.equip[0] in "aeiouy" else ""
                msg += ", which could be equipped to {} {}. ".format(
                    prefix,
                    item.equip
                )
            if item.actions:
                msg += "It allows you to "
                msg += ", ".join(map(str, item.actions))
                msg += ". "
            else:
                msg += "It doesn't allow you to do any actions. "
            if item.stats:
                msg += "It gives you "
                for stat, value in item.stats.items():
                    msg += "{}: {}".format(stat, value)
                msg += "."
            else:
                msg += "It doesn't change your stats."
            print(msg)
    else:
        print("You don't have any items")

viewinv = Action(
    "view inventory",
    {
        "init": viewinv_init,
    },
    {"delay": 0, "speed": -1, "type": "items"},
    #-1 speed compensates for waiting for the turn after it's executed
)


normal_base_actions = [move, null, equip, unequip, look, drop, pickup, viewinv]
