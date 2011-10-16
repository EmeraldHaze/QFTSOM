import api
import lib
statrules = [("HP", "self.stats['STR']*5+50"),
    ("MP", "self.stats['INT']*5+50"),
    ("DEF", "self.stats['STR']"),
    ("MDEF", "self.stats['INT']"),
    ("MAXMP", "self.stats['MP']"),
    ("MAXHP",   "self.stats['HP']"),
    ("MAXWPNDMG", "0"),
    ("MINWPNDMG", "0"),
    ("Dodge", "self.stats['STR']*self.stats['INT']")]

bolt = Action('bolt', {"exec":simple_exec, "init":simpleinit}, metadata = {"delay":0, "type":"magic", "MPcost":60, 'change':1})
hack = Action('hack', {"exec":simple_exec, "init":simpleinit}, metadata = {"delay":0, "type":"melee", 'MPcost': 0, 'change':1})
rest = Action("rest", {"exec":simple_exec, "init":simpleinit}, metadata = {"delay":0, "type":"magic", "MPcost": -40, 'change':0})
heal = Action("heal", {"exec":special_exec, "init":simpleinit}, metadata = {"delay":1, "type":"magic", "MPcost":20})

boom = Action("explode", {"exec":boom, "init":simpleinit}, -1, 0, metadata = {"delay":1, "type":"melee", "MPcost":0, "change":1})
poison = Action("poison", {"exec":poisoned})
stab = Action("stab", {"exec":simple_exec, "init":simpleinit}, metadata = {"delay":0, "type":"melee", "MPcost":0, "change":1, "extra":poison})

staff = api.Belong('Staff', [actions.bolt, actions.heal, actions.rest], {"MAXMP":10, "DEF":10, "MAXWPNDMG":15})
axe = api.Belong("Axe", [actions.hack], {"STR":20, "MAXWPNDMG":10})
helm = api.Belong("Helm", [], {"DEF":10, "MDEF":5, "MAXWPNDMG":5})

dagger = api.Belong("dagger", [actions.stab], {"INT":10, "STR":5})
bomb = api.Belong("bomb", [actions.boom])
shoes = api.Belong("shoes", [], {"Dodge": 600, "INT":5})

dwarf = api.Being('Dwarf', lib.simple.thinkers,
    {'STR':13,'INT':7}, {'Axe':axe, "Helm":helm}, thinkinit = thinkers.stdinit)

player = api.Being('Player', lib.simple.player,
    {'STR': 10, 'INT':10}, {'Staff': staff})

dwarf2 = api.Being('Dwarf2', lib.simple.thinkers,
    {'STR':13,'INT':7}, {'Axe':axe, "Helm":helm}, thinkinit = thinkers.stdinit)

rouge = api.Being("Rouge", lib.simple.player,
    {"STR":10, "INT":12}, {"Dagger":dagger, "Bomb":bomb, "Quick Shoes":shoes})


