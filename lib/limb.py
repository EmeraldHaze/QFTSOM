import api
from lib.base import thinkers, statuses, exits
from random import choice

from core import shared
shared.statrules = {}

def ldie_check(player, battle):
    total = 0
    dead = False
    for belong in player.belongs:
        total += belong.data["HP"]
        if 'vital' in belong.data and belong.data["HP"] < 1:
            dead = True
            break
    if total < 10:
        dead = True
    return dead

limbdie = api.Exit('die', ldie_check, exits.die_effect, ["main", "HP"], ["players"])

def lthinkmaker(actchoice, targetchoice):
    def limbthinker(self, battle):
        act = actchoice(self.actions)
        target = next((target for target in battle.player_list if target != self))
        targetlimb = targetchoice(target.belongs)
        return act.format(self, targetlimb, battle)
    return limbthinker

loony = lthinkmaker(lambda acts:choice(acts), lambda limbs:choice(limbs))
pthinker = lthinkmaker(thinkers.pchoice, lambda choices:thinkers.pchoice(choices, extra = ("HP:", "t.data['HP']")))

def limbexec(actor, self, targets, battle):
    targetlimb = targets[0]
    target = next(target for target in battle.player_list if target != self)
    targetlimb.data["HP"] -= self.metadata['dmg']
    print("{}'s {} took {} DMG, it now has {}".format(target.name, targetlimb.name, self.metadata['dmg'], targetlimb.data["HP"]))
    if 'poison' in self.metadata:
        target.data['poison'] = self.metadata["poison"]
        target.status_list.append(statuses.poison)


bite = api.Action('bite', {"exec":limbexec}, {"dmg":5})#, "poison":10})
whip = api.Action('whip', {'exec':limbexec}, {"dmg":10})

head = api.Belong("Head", {}, [bite], {"HP":20, "vital": True})
tail = api.Belong("Tail", {}, [whip], {"HP":30})

python = api.Being('Python', loony, {}, [head, tail])
monty  = api.Being('Montey', pthinker, {}, [head, tail])