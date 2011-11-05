import api, lib
from lib.base import thinkers, actions
from core import shared
shared.statrules  = [("MAXHP", "self.stats['HP']")]

manthinker = thinkers.think_maker(thinkers.mosttarget, thinkers.firstact)
oddthinker = thinkers.think_maker(thinkers.least,      thinkers.firstact)
pthinker   = thinkers.think_maker(thinkers.ptarget,    thinkers.firstact)

poke = actions.simplemaker("poke", 1, "lib")
hit  = actions.simplemaker("hit" , 2, "lib")

stick = api.Belong("stick", {}, [poke])
staff = api.Belong("staff", {}, [hit])

baseman = api.Being('Model', manthinker, {"HP":5}, [stick])

##                 NAME        THINKER     STATS     BELONGS
player = api.Being('Player',   pthinker,   {'HP': 6}, [stick]).instance("")
man    = baseman.instnace("Man")
man2   = api.Being('OtherMan', manthinker, {'HP': 4}, [stick])
oddman = api.Being('Oddball',  oddthinker, {'HP': 5}, [stick])
staffo = api.Being('Staffo',   manthinker, {'HP': 5}, [staff])

fight = {"battle": [man, player, man2, staffo, oddman]}