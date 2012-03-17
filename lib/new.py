import api
import lib
from lib.base import thinkers, actions, exits, rules
from lib.base.user import user
from core import shared
from random import choice

shared.statrules = [("MAXHP", "self.stats['HP']")]
shared.current_module = "new"
shared.modules["new"] = """This is a module for trying out the refactored
changes"""
shared.misc.base_actions = actions.normal_base_actions
shared.actions.blank()
shared.actions.listners = {"choosen": actions.basic_choosen}


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
        choices = eval(info)
        try:
            args[arg] = choice(list(choices.values()))
        except AttributeError:
            args[arg] = choice(choices)
    return action.instance(**args)


def power_exec(self):
    act = self.args["act"]
    act.data["dmg"] += self.data["dmg"]
    print(act.name, "powered up!")

power_choosen = lambda self: print(self.actor, "powers up!")
power = api.AbstractAction(
    "power",
    {"exec": power_exec, "choosen": power_choosen},
    {"dmg": 1, "type": "buff", "speed": 1},
    0,
    0,
    argsinfo={"act": "self.being.actions"}
)

poke = actions.simplemaker("poke", 1)
punch = actions.simplemaker("punch", 2)
stab = actions.simplemaker("stab", 5)

ab = api.Limb("finger", [power])
arm = api.Limb("arm", [punch, poke])

knife = api.Item("arm", {}, [stab]).instance("knife")
rknife = api.Item("arm", {}, [stab]).instance("red knife")

player = api.Being(
    [ab, arm],
    user,
    {"HP": 6},
    [rknife]
).instance(shared.name)

drunkard = api.Being(
    [arm],
    drunk,
    {"HP": 10}
).instance("Drunkard")
