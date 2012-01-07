import api, lib
from api.limb import sym
from lib.base import actions, thinkers, statuses, exits, rules
from lib.simple import manthinker as simplethink
from core import shared
from random import randint

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
"melee":"self.actor.stats['STR']+\
        randint(self.actor.stats['MINWPNDMG'], self.actor.stats['MAXWPNDMG'])-\
        target.stats['DEF']*self.metadata['change']",
"magic":"(self.actor.stats['INT']*\
        randint(self.actor.stats['MINWPNDMG'], self.actor.stats['MAXWPNDMG'])-\
        target.stats['MDEF'])*self.metadata['change']"}

def healmaker(name, heal, stat, delay, cost, type = "magic"):
    healvalue = 30
    def healer(self):
        self.targets[0].stats[stat] += heal
        print(self.targets[0].name, "has gained", heal, stat)
    return api.Action(name, {"exec":healer, "init":completeinit}, metadata = {"type":type, "MPC":cost, "delay":delay})

def completeinit(self):
    self.dmgrules = dmg_rules
    actions.manainit(self)

def boom(self):
    print("Boom!")
    for player in self.targets:
        dodge = player.stats['Dodge']
        dodge = int(randint(0, 1000)<dodge)
        if dodge:
            dmg = 0
            print(player.name, "dodged the bomb!")
        else:
            dmg = randint(0, 100) * self.actor.stats['INT']
            player.stats["HP"]-=dmg
            print(player.name, "lost ", dmg, "vital energy in the blast!")

    self.actor.actions = [action for action in self.actor.actions if action.name != self.name]
    #Removes bomb from actions
    self.actor.rmbelong("Bomb")

bolt = api.Action('bolt', {"exec":actions.complete_exec, "init":completeinit}, metadata = {"type":"magic", "MPC":60, 'change':1})
hack = api.Action('hack', {"exec":actions.complete_exec, "init":completeinit}, metadata = {"type":"melee", 'MPC': 0, 'change':1})
heal = healmaker ("heal", 30, "HP", 1, 30)
rest = healmaker ("rest", 20, "MP", 0,  0)

boom = api.Action("explode", {"exec":boom, "init":completeinit}, {"delay":1, "type":"melee", "MPC":0, "change":1}, -1, 0)
stab = api.Action("stab"   , {"exec":actions.complete_exec, "init":completeinit}, metadata = {"type":"melee", "MPC":0, "change":1, "status":statuses.poison, "data":('poison', 30)})

staff = api.Belong('Staff', "Arm", {"MAXMP":10, "DEF":10, "MAXWPNDMG":15}, [bolt, heal, rest])
axe   = api.Belong("Axe",   "Arm", {"STR":20, "MAXWPNDMG":  10}, [hack])
helm  = api.Belong("Helm",  "Head", {"DEF":10, "MDEF":5, "MAXWPNDMG":5})

knife = api.Belong("Knife", "Arm", {"INT":10, "STR":5}, [stab])
shoes = api.Belong("Shoes", "Leg", {"Dodge": 600, "INT":5})
bomb  = api.Belong("Bomb",  "Bag", {}, [boom])

head = api.Limb("Head")
arm  = api.Limb("Arm")
leg  = api.Limb("Leg")
bag  = api.Limb("Bag")

Humanoid = api.Being((head, sym(arm), sym(leg), bag), simplethink, {'STR':13,'INT':7})
dwarf  = Humanoid.instance("Dwarf I", belongs=[axe, helm])
dwarf2 = Humanoid.instance("Dwarf II", belongs=[axe, helm])
rouge  = Humanoid.instance("Rouge", thinkers.pthinker, [knife, bomb, shoes], {"STR":-3, "INT":+5})
mage   = Humanoid.instance('Magus', thinkers.pthinker, [staff], {'STR':-3, 'INT':+5})

game = api.Node([], [], [("battle", [[dwarf, dwarf2, mage, rouge], [exits.die], [rules.next, rules.reset]]), ("send", "hub")])