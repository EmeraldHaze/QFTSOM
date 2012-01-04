import api, lib
from lib.base import thinkers, actions
from core import shared

shared.blank()
shared.statrules  = [("MAXHP", "self.stats['HP']")]
shared.modules["simple"] = "A basic no-frills module. Requires nothing, but will probably not work with anything that requires something, like the speed scheduler"
shared.current_module = "simple"

manthinker = thinkers.think_maker(thinkers.mosttarget, thinkers.firstact)
oddthinker = thinkers.think_maker(thinkers.least,      thinkers.firstact)
pthinker   = thinkers.think_maker(thinkers.ptarget,    thinkers.firstact)

poke = actions.simplemaker("poke", 1)
hit  = actions.simplemaker("hit" , 2)

finger = api.Limb("finger", [poke])
arm    = api.Limb("arm", [hit])

baseman = api.Being([finger], manthinker, {"HP":5})
player = baseman.instance("Player", pthinker, statchanges={"HP":1})
oddman = baseman.instance("Oddball", oddthinker)
man    = baseman.instance("Man")
man2   = baseman.instance("OtherMan", manthinker, statchanges={'HP':-1})
staffo = baseman.instance("Staffo", limbs=[arm])

fight = {"battle": [man, player, man2, staffo, oddman]}