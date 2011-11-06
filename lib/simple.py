import api, lib
from lib.base import thinkers, actions
from core import shared
shared.statrules  = [("MAXHP", "self.stats['HP']")]

manthinker = thinkers.think_maker(thinkers.mosttarget, thinkers.firstact)
oddthinker = thinkers.think_maker(thinkers.least,      thinkers.firstact)
pthinker   = thinkers.think_maker(thinkers.ptarget,    thinkers.firstact)

poke = actions.simplemaker("poke", 1)
hit  = actions.simplemaker("hit" , 2)

finger = api.Limb("finger", [poke])
arm    = api.Limb("arm", [hit])

baseman = api.Being([finger], manthinker, {"HP":5})
player = baseman.instance("Player", pthinker, {"HP":1})
oddman = baseman.instance("Oddball", oddthinker)
man    = baseman.instance("Man")
man2   = baseman.instance("OtherMan", manthinker, {'HP':-1})
staffo = baseman.instance("Staffo", limbs=[arm])

fight = {"battle": [man, player, man2, staffo, oddman]}