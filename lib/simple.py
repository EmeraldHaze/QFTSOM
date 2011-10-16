import api, lib
from lib.base import thinkers, actions
from game import defaults

defaults.statrules  = [("MAXHP", "self.stats['HP']")]

manthinker = thinkers.think_maker(thinkers.mosttarget, thinkers.firstact)
oddthinker = thinkers.think_maker(thinkers.least,      thinkers.firstact)
pthinker   = thinkers.think_maker(thinkers.ptarget,    thinkers.firstact)
thinker    = manthinker

poke = actions.simplemaker("poke", 1, "lib")
hit  = actions.simplemaker("hit" , 2, "lib")

stick = api.Belong("stick", {}, [poke])
staff = api.Belong("staff", {}, [hit])

##                 NAME        THINKER     STATS     BELONGS
player = api.Being('Player',   pthinker,   {'HP': 6}, [stick])
man    = api.Being('Man',      manthinker, {'HP': 5}, [stick])
man2   = api.Being('OtherMan', manthinker, {'HP': 4}, [stick])
oddman = api.Being('Oddball',  oddthinker, {'HP': 5}, [stick])
staffo = api.Being('Staffo',   manthinker, {'HP': 5}, [staff])