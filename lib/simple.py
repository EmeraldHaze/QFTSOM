import api
import lib
from lib.base import thinkers, actions, exits, rules
from core import shared

shared.blank()
shared.statrules = [("MAXHP", "self.stats['HP']")]
shared.modules["simple"] = """A basic no-frills module. Requires nothing,
but probably won't work with anything that requires something, like the
speed scheduler"""
shared.current_module = "simple"

manthinker = thinkers.think_maker(thinkers.mosttarget, thinkers.firstact)
oddthinker = thinkers.think_maker(thinkers.least,      thinkers.firstact)
pthinker   = thinkers.think_maker(thinkers.ptarget,    thinkers.firstact)

poke = actions.simplemaker("poke", 1)
hit  = actions.simplemaker("hit", 2)

finger = api.Limb("finger", [poke])
arm = api.Limb("arm", [hit])

baseman = api.Being([finger], manthinker, {"HP": 5})
player = baseman.instance(shared.name, pthinker, statchanges={"HP":1})
oddman = baseman.instance("Oddball", oddthinker)
man = baseman.instance("Man")
man2 = baseman.instance("OtherMan", manthinker, statchanges={'HP':-1})
#superman, superarm, new being
staffo = api.Being([arm], manthinker, {"HP": 5}).instance("Staffo")

game = api.Net(0, {
    0: api.Node([], [],
        {"say":
            "The folks you're to fight are simple: they attack he who has the "
            "least HP. The town fool, Oddball, does the reverse, whilst the "
            "puissant Staffo hits twice as hard as you stick-possesing fools.",
        "send": 1
        }),
    1: api.Node([], [], {
        'battle':
            [
                [man, player, man2, staffo, oddman],
                [exits.die],
                [rules.next, rules.wipe_normal]
            ]}, exit_="hub")
    })
