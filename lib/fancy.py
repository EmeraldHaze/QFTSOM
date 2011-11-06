import api, lib
from lib.base import actions, thinkers, statuses
from core import shared
from random import randint

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
"melee":"actor.stats['STR']+\
        randint(actor.stats['MINWPNDMG'], actor.stats['MAXWPNDMG'])-\
        target.stats['DEF']*self.metadata['change']",
"magic":"(actor.stats['INT']*\
        randint(actor.stats['MINWPNDMG'], actor.stats['MAXWPNDMG'])-\
        target.stats['MDEF'])*self.metadata['change']"}

def healmaker(name, heal, stat, delay, cost, type = "magic"):
    healvalue = 30
    def healer(self):
        self.targets[0].stats[stat] += heal
        print(self.targets[0].name, "has gained", heal, stat)
    return api.Action(name, {"exec":healer, "init":completeinit}, metadata = {"type":type, "MPcost":cost, "delay":delay})

def completeinit(actor, self, targets):
    self.dmgrules = dmg_rules
    actions.manainit(actor, self, targets)

def boom(self):
    print("Boom!")
    for player in self.targets:
        dodge = player.stats['Dodge']
        dodge = int(randint(0, 1000)<dodge)
        if dodge:
            dmg = 0
            print(player.name, "dodged the bomb!")
        else:
            dmg = randint(0, 100)*actor.stats['INT']
            player.stats["HP"]-=dmg
            print(player.name, "lost ", dmg, "sanity in the blast!")

    self.actor.actions = [action for action in actor.actions if action.name != self.name]
    #Removes bomb from actions
    actor.rmbelong("Bomb")

bolt = api.Action('bolt', {"exec":actions.complete_exec, "init":completeinit}, metadata = {"type":"magic", "MPcost":60, 'change':1})
hack = api.Action('hack', {"exec":actions.complete_exec, "init":completeinit}, metadata = {"type":"melee", 'MPcost': 0, 'change':1})
heal = healmaker ("heal", 30, "HP", 1, 30)
rest = healmaker ("rest", 20, "MP", 0,  0)

boom = api.Action("explode", {"exec":boom, "init":completeinit}, {"delay":1, "type":"melee", "MPcost":0, "change":1}, -1, 0)
stab = api.Action("stab"   , {"exec":actions.complete_exec, "init":completeinit}, metadata = {"type":"melee", "MPcost":0, "change":1, "status":statuses.poison, "data":('poison', 30)})

staff  = api.Belong('Staff', {"MAXMP":10, "DEF":10, "MAXWPNDMG":15}, [bolt, heal, rest])
axe    = api.Belong("Axe", {"STR":20, "MAXWPNDMG":10}, [hack])
helm   = api.Belong("Helm", {"DEF":10, "MDEF":5, "MAXWPNDMG":5})

dagger = api.Belong("dagger", {"INT":10, "STR":5}, [stab])
shoes  = api.Belong("shoes", {"Dodge": 600, "INT":5})
bomb   = api.Belong("bomb", {}, [boom])

pthinker = thinkers.think_maker(thinkers.ptarget, thinkers.paction)

dwarf  = api.Being('Dwarf' , lib.simple.thinker, {'STR':13,'INT':7}, [axe, helm])
dwarf2 = api.Being('Dwarf2', lib.simple.thinker, {'STR':13,'INT':7}, [axe, helm])
rouge  = api.Being("Rouge" , pthinker, {"STR":10, "INT":12},[dagger, bomb, shoes])
mage   = api.Being('Player', pthinker, {'STR':10, 'INT':10},[staff])

fight = {'battle': [mage, rouge, dwarf, dwarf2]}