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

@api.Thinker
def smarty(self):
    action = thinkers.pchoice(self.being.actions)
    args = {}
    for arg, info in action.argsinfo.items():
        if arg is "targets":
            value = thinkers.pchoice(eval(info), ("HP", "choice.stats['HP']"))
        else:
            value = thinkers.pchoice(eval(info))
        args[arg] = value
    return action.instance(**args)

def power_exec(self):
    act = self.args["act"]
    act.data["dmg"] += self.data["mod"]
    print(act.name, "powered up!")

power_choosen = lambda self: print(self.actor, "powers up!")
power = api.AbstractAction(
    "power",
    {"exec": power_exec, "choosen": power_choosen},
    {"mod": 1},
    0,
    0,
    argsinfo={"act": "self.being.actions"}
)
poke = actions.simplemaker("poke", 1)
hit  = actions.simplemaker("hit", 2)

finger = api.Limb("finger", [poke])
arm = api.Limb("arm", [hit])

fist = api.Item("fist", "arm", {}, [power])

baseman = api.Being([finger], manthinker, {"HP": 5})
#player = baseman.instance(shared.name, pthinker, statchanges={"HP":1})
oddman = baseman.instance("Oddball", oddthinker)
man = baseman.instance("Man")
man2 = baseman.instance("OtherMan", manthinker, statchanges={'HP':-1})
#superman, superarm, new being
staffo = api.Being([arm], manthinker, {"HP": 5}).instance("Staffo")

player = api.Being([finger, arm], smarty, {"HP": 6}, [fist]).instance(shared.name)

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
