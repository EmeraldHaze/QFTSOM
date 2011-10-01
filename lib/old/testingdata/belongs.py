from api.belong import Belong
from data import actions
stick = Belong('Stick', [actions.poke])
simplestaff = Belong('Staff', [actions.hit])

staff = Belong('Staff', [actions.bolt, actions.heal, actions.rest], {"MAXMP":10, "DEF":10, "MAXWPNDMG":15})
axe = Belong("Axe", [actions.hack], {"STR":20, "MAXWPNDMG":10})
helm = Belong("Helm", [], {"DEF":10, "MDEF":5, "MAXWPNDMG":5})

dagger = Belong("dagger", [actions.stab], {"INT":10, "STR":5})
bomb = Belong("bomb", [actions.boom])
shoes = Belong("shoes", [], {"Dodge": 600, "INT":5})