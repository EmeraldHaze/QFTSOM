import api
from lib.base import thinkers, statuses, exits, rules
from random import choice, randint

def ldie_check(player, battle):
    total = 0
    dead = False
    for belong in player.belongs:
        if belong.data["limb"]:
            total += belong.data["HP"]
            if belong.data["HP"] < 1:
                print("{} has lost his {}!".format(player.name, belong.name))
                player.rmbelong(belong)
                for act in belong.actions:
                   player.actions.remove(act)
                   del player.act_dict[act.name]
                if 'vital' in belong.data:
                    dead = True
                    break
    if total < 10:
        dead = True
    return dead

limbdie = api.Exit('die', ldie_check, exits.die_effect, ["main", "HP"], ["players"])
#####BEING#####
###THINKER###
def lthinkmaker(actchoice, targetchoice):
    def limbthinker(self, battle):
        act = actchoice(self.actions)
        target = next((target for target in battle.player_list if target != self))
        targetlimb = targetchoice([target for target in target.belongs if target.data['limb']])
        return act.format(self, targetlimb, battle)
    return limbthinker

loony = lthinkmaker(lambda acts:choice(acts), lambda limbs:choice(limbs))
pthinker = lthinkmaker(thinkers.pchoice, lambda choices:thinkers.pchoice(choices, extra = ("HP", "t.data['HP']")))

###ACTION###
@api.Status
def limbpoison(player, battle):
    limb, poison = player.data["poison"]
    limb.data["HP"] -= poison
    player.data['poison'][1] -= 1
    if player.data['poison'][1] < 1:
        player.status_list.remove(limbpoison)
    print("{}'s {} took {} DMG from poison, it now has {}".format(player.name, limb.name, poison, limb.data["HP"]))

def limbexec(actor, self, targets, battle):
    targetlimb = targets[0]
    target = next(target for target in battle.player_list if target != actor)
    if "evade" not in targetlimb.data:
        targetlimb.data["evade"] = 0
    if randint(0, 100) > targetlimb.data["evade"]:
        targetlimb.data["HP"] -= self.metadata['dmg']
        print("{}'s {} took {} DMG, it now has {}".format(target.name, targetlimb.name, self.metadata['dmg'], targetlimb.data["HP"]))
        if 'poison' in self.metadata:
            target.data['poison'] = [targetlimb, self.metadata["poison"]]
            target.status_list.append(limbpoison)
            print("{}'s {} has been poisoned for {}".format(target.name, targetlimb.name, self.metadata['poison']))
    else:
        print("{}'s {} missed!".format(actor.name, self.name))

###REAL###
from core import shared
shared.belongdata = [("limb", 'True')]
shared.statrules = []

bite = api.Action('bite', {"exec":limbexec}, {"dmg":5, "poison":10, 'speed':2})
headbutt = api.Action("headbut", {"exec":limbexec}, {"dmg":3, 'speed':3})
whip = api.Action('whip', {'exec':limbexec}, {"dmg":10, 'speed':2})
sting = api.Action('sting', {'exec':limbexec}, {'dmg':2, 'poison':20, 'speed':2})

head = api.Belong("Head", {}, [headbutt], {"HP":30, "vital": True})
tail = api.Belong("Tail", {}, [whip], {"HP":40})
stinger = api.Belong("Stinger", {}, [sting], {"HP":10})

python = api.Being('Python', loony, {}, [head, tail], {'speed':2})
monty  = api.Being('Montey', pthinker, {}, [head, tail], {'speed':2})
flylord = api.Being("Beezulbub", pthinker, {}, [head, stinger], {'speed':2})

stab = api.Action('stab', {'exec':limbexec}, {'dmg':5, 'poison':5, 'speed':1})
punch = api.Action('punch', {'exec':limbexec}, {'dmg':15, 'speed':2})
kick = api.Action('kick', {'exec':limbexec}, {'dmg':20, 'speed':2})

knife = api.Belong("Knife", {}, [stab],{"limb":False})
head = api.Belong("Head", {}, [headbutt], {"HP":20, "vital":True, "evade":40})
arm  = api.Belong("Arm", {}, [punch], {"HP":30, "evade":20})
torso = api.Belong("Torso", {}, [], {"HP":60, "vital":True})
leg = api.Belong("Leg", {}, [kick], {"HP":30, "evade":20})

man = api.Being("MAN", pthinker, {}, [head, arm, knife, arm, torso, leg, leg], {'speed':5})

fight = {"say":"Limbic rage awaits ye!", "battle":[[python, man], [limbdie], [rules.speed]]}