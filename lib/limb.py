import api
from api.limb import sym
from lib.base import thinkers, statuses, exits, rules
from random import choice, randint
from core import shared

shared.blank()
shared.limb_datarules = [("MAXHP", "self.data['HP']"), ("DEF", "0"), ("evade", "0")]
shared.current_module = "limb"
shared.modules["limb"] = "This module allows you to attack limbs. It requires limbs that have HP, limbdie exit (for killing limbs). and "

def ldie_check(player, battle):
    total = 0
    dead = False
    for limb in player.limbs:
        total += limb.data["HP"]
        if limb.data["HP"] < 1:
            limb.kill()
            if 'vital' in limb.data:
                dead = True
                break
    if total < 10:
        dead = True
    return dead

limbdie = api.Exit('limbdie', ldie_check, lambda p,b:print(p.name, "died!"), ["main", "HP"], ["players"])
#####BEING#####
###THINKER###
def lthinkmaker(actchoice, targetchoice):
    @api.Thinker
    def limbthinker(self):
        target = next(target for target in self.battle.player_list if target != self.player)
        targetlimb = targetchoice(target.limbs)
        act = actchoice(self.player.act_dict)
        return act.instance(self.player, targetlimb, self.battle)
    return limbthinker

loony = lthinkmaker(lambda acts:choice(list(acts.values())), lambda limbs:choice(limbs))
pthinker = lthinkmaker(thinkers.pchoice, lambda choices:thinkers.pchoice(choices, extra = ("HP", "choice.data['HP']")))

###ACTION###
@api.Status
def limbpoison(self):
    self.limb.status_list.append(self)
    player = self.player
    self.limb.data["HP"] -= self.poison
    print("{}'s {} took {} DMG from poison, it now has {}".format(player.name, self.limb.name, self.poison, self.limb.data["HP"]))
    self.poison -= 1
    if not self.poison:
        player.status_list.remove(self)

def limbexec(self):
    targetlimb = self.targets[0]
    target = targetlimb.player
    if randint(0, 100) > targetlimb.data["evade"]:
        #Hit
        dmg = self.metadata['dmg'] - targetlimb.data["DEF"]
        targetlimb.data["HP"] -= dmg
        print("{}'s {} took {} DMG, it now has {}".format(target.name, targetlimb.name, self.metadata['dmg'], targetlimb.data["HP"]))
        if 'poison' in self.metadata:
            poison = limbpoison.instance(target, self.battle)
            poison.limb = targetlimb
            poison.poison = self.metadata['poison']
            target.status_list.append(poison)
            print("{}'s {} has been poisoned for {}".format(target.name, targetlimb.name, self.metadata['poison']))
    else:
        print("{}'s {} missed!".format(self.actor.name, self.name))

def enchant(self):
    self.targets[0].data['PWR'] *= 2
###REAL###

bite = api.Action('bite', {"exec":limbexec}, {"dmg":5, "poison":10, 'speed':2})
whip = api.Action('whip', {'exec':limbexec}, {"dmg":10, 'speed':2})
sting = api.Action('sting', {'exec':limbexec}, {'dmg':2, 'poison':20, 'speed':2})

fang = api.Limb("Fang", [bite],  data={"HP":5, 'evade':60})
barb = api.Limb("Barb", [sting], data={"HP":10, 'evade':40})
tail = api.Limb("Tail", [whip],  data={"HP":40, 'evade':10}, stats={'speed':1})
head = api.Limb("Head", data={"HP":30, "vital":True, "evade":30}, stats={'speed':1})

snake  = api.Being(((head, fang), tail), loony)
python = snake.instance('Python')
monty  = snake.instance('Montey')
flylord = api.Being((head, barb), loony).instance("Beezulbub")

stab  = api.Action('stab',  {'exec':limbexec}, {'dmg':5 , 'speed':1, 'poison':5})
punch = api.Action('punch', {'exec':limbexec}, {'dmg':15, 'speed':2})
kick  = api.Action('kick',  {'exec':limbexec}, {'dmg':20, 'speed':2})

knife = api.Belong("knife", 'Arm', {}, [stab])
arm   = api.Limb("Arm", [punch], 'Arm', {"HP":30, "evade":20}, {'speed':0.5})
head  = api.Limb("Head", [], data={"HP":20, "vital":True, "evade":40})
torso = api.Limb("Torso", data={"HP":60, "vital":True}, stats={"speed":1})
leg   = api.Limb("Leg", [kick], data={"HP":30, "evade":20}, stats={"speed":1})

man = api.Being((torso, (head, sym(fang)), sym(arm), sym(leg)), pthinker, {"speed": -3}, [knife])
player = man.instance("Player")
player.equip("knife", "Right Arm")
mad = man.instance("Huminoid Taco", loony, statchanges={"speed":1})
mad.equip("knife", "Left Arm")
fight = [("say","Limbic rage awaits ye!"), ("battle",[[player, mad], [limbdie], [rules.speed]])]