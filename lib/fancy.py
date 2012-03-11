import api
import lib
from api.limb import sym
from lib.base import actions, thinkers, statuses, exits, rules
from lib.simple import manthinker as simplethink

from random import randint
from core import shared

shared.blank()
shared.statrules = [("HP", "self.stats['STR']*5+50"),
    ("MP", "self.stats['INT']*5+50"),
    ("DEF", "self.stats['STR']"),
    ("MDEF", "self.stats['INT']"),
    ("MAXMP", "self.stats['MP']"),
    ("MAXHP",   "self.stats['HP']"),
    ("MAXWPNDMG", "0"),
    ("MINWPNDMG", "0"),
    ("Dodge", "self.stats['STR']*self.stats['INT']")]

dmg_rules = {\
"melee": "self.actor.stats['STR']+\
        randint(self.actor.stats['MINWPNDMG'], self.actor.stats['MAXWPNDMG'])-\
        target.stats['DEF']*self.data['change']",
"magic": "(self.actor.stats['INT']*\
        randint(self.actor.stats['MINWPNDMG'], self.actor.stats['MAXWPNDMG'])-\
        target.stats['MDEF'])*self.data['change']"}


@api.ActionFactory
def healf(name, heal, stat, **data):
    if "type" not in data:
        data["type"] = "magic"

    def healer(self):
        self.targets[0].stats[stat] += heal
        print(self.targets[0].name, "has gained", heal, stat)

    return api.Action(name, {"exec": healer, "init": completeinit}, data=data)


@api.ActionFactory
def attackf(name, **data):
    if "change" not in data:
        data["change"] = 1
    return api.Action(name,
        {"exec": actions.complete_exec, "init": completeinit},
        data=data
    )


def completeinit(self):
    self.dmgrules = dmg_rules
    actions.manainit(self)


def boom(self):
    "The bomb executor"
    print("Boom!")
    for being in self.targets:
        dodge = being.stats['Dodge']
        dodge = int(randint(0, 1000) < dodge)
        if dodge:
            dmg = 0
            print(being.name, "dodged the bomb!")
        else:
            dmg = randint(0, 100) * self.actor.stats['INT']
            being.stats["HP"] -= dmg
            print(being.name, "lost ", dmg, "vital energy in the blast!")

    self.actor.rmitem("Bomb")
    self.actor.actions.remove(self)


bolt = attackf('bolt', type="magic", MPC=60)
hack = attackf('hack', type="melee", MPC=0)
heal = healf("heal", 30, "HP", delay=1, MPC=30)
rest = healf("rest", 20, "MP", delay=0, MPC=0, type="melee")

boom = api.Action(
        "explode",
        {"exec": boom, "init": completeinit},
        {"delay": 1, "type": "melee", "MPC": 0, "change": 1},
        -1,
        0
    )

stab = attackf(
    "stab",
    type="melee",
    MPC=0,
    status=statuses.poison,
    status_data={"poison": 5}
)

staff = api.Item(
    'Staff',
    "arm",
    {"MAXMP": 10, "DEF": 10, "MAXWPNDMG": 15},
    [bolt, heal, rest]
)
axe = api.Item("Axe",  "arm", {"STR": 20, "MAXWPNDMG": 10}, [hack])
helm = api.Item("Helm", "arm", {"DEF": 10, "MDEF": 5, "MAXWPNDMG": 5})

knife = api.Item("Knife", "arm", {"INT": 10, "STR": 5}, [stab])
shoes = api.Item("Shoes", "leg", {"Dodge": 600, "INT": 5})
bomb = api.Item("Bomb",  "bag", {}, [boom])

arm = api.Limb("arm")
leg = api.Limb("leg")
bag = api.Limb("bag")

Humanoid = api.Being(
    (arm, sym(arm), sym(leg), bag),
    simplethink,
    {'STR': 13, 'INT': 7}
)

dwarf = Humanoid.instance("Dwarf I",  items=[axe, helm])
dwarf2 = Humanoid.instance("Dwarf II", items=[axe, helm])
rouge = Humanoid.instance(
    "Rouge " + shared.name,
    thinkers.pthinker,
    [knife, bomb, shoes],
    {"STR": -3, "INT": 5}
)
mage = Humanoid.instance(
    "Smart " + shared.name,
    thinkers.pthinker,
    [staff],
    {'STR': -3, 'INT': 5}
)

game = api.Node([], [], [
    ("battle",
        [
            [dwarf, dwarf2, mage, rouge],
            [exits.die],
            [rules.next, rules.wipe_normal]
        ]
    ), ("send", "hub")
])
