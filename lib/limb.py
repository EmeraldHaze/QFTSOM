import api
from lib.base import thinkers, statuses, exits
from random import choice, randint

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

@api.Status
def limbpoison(player, battle):
    limb, poison = player.data["poison"]
    limb.data["HP"] -= poison
    player.data['poison'][1] -= 1
    if player.data['poison'][1] < 1:
        player.status_list.remove(self)
    print("{}'s {} took {} DMG from poison, it now has {}".format(player.name, limb.name, poison, limb.data["HP"]))
    
def limbexec(actor, self, targets, battle):
    targetlimb = targets[0]
    target = next(target for target in battle.player_list if target != self)
    if "evade" in targetlimb.data:
        targetlimb.data["evade"] = 0
    if randint(0, 100) > targetlimb.data["evade"]:
        targetlimb.data["HP"] -= self.metadata['dmg']
        print("{}'s {} took {} DMG, it now has {}".format(target.name, targetlimb.name, self.metadata['dmg'], targetlimb.data["HP"]))
        if 'poison' in self.metadata:
            target.data['poison'] = (targetlimb, self.metadata["poison"])
            target.status_list.append(statuses.limbpoison)
            print("{}'s {} has been poisoned for {}".format(target.name, targetlimb.name, self.metadata['poison']))
        if targetlimb.data["HP"] < 1:
            print("{} has lost his {}!".format(target.name, targetlimb.name)
            target.rmbelong(targetlimb)
            for act in targetlimb.actions:
               target.actions.remove(act)
               del target.act_dict[act.name]
    else:
        print("{}'s {} missed!".format(actor.name, self.name)

bite = api.Action('bite', {"exec":limbexec}, {"dmg":5, "poison":10})
whip = api.Action('whip', {'exec':limbexec}, {"dmg":10})
sting = api.Action('sting', {'exec':limbexec}, {'dmg':2, 'poison':20})

head = api.Belong("Head", {}, [], {"HP":20, "vital": True})
tail = api.Belong("Tail", {}, [whip], {"HP":30})
stinger = api.Belong("Stinger", {}, [sting], {"HP":10}

python = api.Being('Python', loony, {}, [head, tail])
monty  = api.Being('Montey', pthinker, {}, [head, tail])
flylord = api.Being("Beezulbub", pthinker, {}, [head, tail])

stab = api.Action('stab', {'exec':limbexec}, {'dmg':10, 'poison':5})
punch = api.Action('punch', {'exec':limbexec}, {'dmg':15})


head = api.Belong("Head", {}, [], {"HP":20, "vital":True, "evade":40})
arm  = api.Belong("Arm", {}, [stab], {"HP":30, "evade":20})
larm = api.Belong("Arm", {}, [punch], {"HP":30, "evade":20})
torso = api.Belong("Torso", {}, [], {"HP":60, "vital":True})
leg = api.Beling("Leg", {}, [kick], {"HP":30, "evade":20})
