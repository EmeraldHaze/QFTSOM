import api
import lib
from lib.base import thinkers, actions, exits, rules
from core import shared
from random import choice

shared.statrules = [("MAXHP", "self.stats['HP']")]
shared.current_module = "new"
shared.modules["new"] = """This is a module for trying out the refactored
changes"""
shared.misc.base_actions = actions.normal_base_actions

@api.Thinker
def smart_user(self):
    action = thinkers.pchoice(self.being.actions)
    args = {}
    for arg, info in action.argsinfo:
        if arg is "targets":
            value = thinkers.pchoice(eval(info), ("HP", "choice.stats['HP']"))
        else:
            value = thinkers.pchoice(eval(info))
        args[arg] = value
    return action.instance(**args)


@api.Thinker
def drunk(self):
    if len(self.being.location.beings) > 1:
        action = choice([
            act for act in self.being.actions if act.data["type"] is "attack"
        ])
    else:
        action = self.being.act_dict["move"]
    args = {}
    for arg, info in action.argsinfo:
        args[arg] = choice(eval(info))
    return action.instance(**args)


def power_exec(self):
    act = self.args["act"]
    act.data["dmg"] += self.data["dmg"]
    print(act.name, "powered up!")

power_choosen = lambda self: print(self.actor, "powers up!")
power = api.AbstractAction(
    "power",
    {"exec": power_exec, "choosen": power_choosen},
    {"dmg": 1, "type": "buff"},
    0,
    0,
    argsinfo={"act": "self.being.actions"}
)

poke = actions.simplemaker("poke", 1)
punch = actions.simplemaker("punch", 2)
stab = actions.simplemaker("stab", 5)

ab = api.Limb("finger", [power])
arm = api.Limb("arm", [punch, poke])

knife = api.Item("knife", "arm", {}, [stab])

player = api.Being(
    [ab, arm],
    smart_user,
    {"HP": 6},
    [knife]
).instance(shared.name)

drunkard = api.Being(
    [arm],
    drunk,
    {"HP": 10}
).instance("Drunkard")
