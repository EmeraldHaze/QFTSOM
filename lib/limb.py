import api
from api.limb import sym
from lib.base import thinkers, statuses, exits, rules
from random import choice, randint
from core import shared

shared.blank()
shared.limb_datarules = [("MAXHP", "self.data['HP']"), ("DEF", "0"), ("evade", "0")]
shared.current_module = "limb"
shared.modules["limb"] = "This module allows you to attack limbs. It requires limbs that have HP, limbdie exit (for killing limbs). and "

def ldie_check(being, battle):
    total = 0
    dead = False
    for limb in being.limbs:
        total += limb.data["HP"]
        if limb.data["HP"] < 1:
            limb.kill()
            if 'vital' in limb.data:
                dead = True
                break
    if total < 10:
        dead = True
    return dead

limbdie = api.Exit('limbdie',
    ldie_check,
    lambda being, battle: print(being.name, "died!"),
    ["main", "HP"], ["beings"])
#####BEING#####
###THINKER###
def lthinkmaker(actchoice, targetchoice):
    @api.Thinker
    def limbthinker(self):
        target = next(target for target in self.battle.being_list if target != self.being)
        targetlimb = targetchoice(target.limbs)
        act = actchoice(self.being.act_dict)
        return act.instance(self.being, targetlimb, self.battle)
    return limbthinker

loony = lthinkmaker(
    lambda acts:  choice(list(acts.values())),
    lambda limbs: choice(limbs)
)

pthinker = lthinkmaker(
    thinkers.pchoice,
    lambda choices: thinkers.pchoice(
        choices,
        extra = ("HP", "choice.data['HP']")
    )
)

###ACTION###
@api.Status
def limbpoison(self):
    self.limb.status_list.append(self)
    being = self.being
    self.limb.data["HP"] -= self.poison
    print("{}'s {} took {} DMG from poison, it now has {}".format(being.name, self.limb.name, self.poison, self.limb.data["HP"]))
    self.poison -= 1
    if not self.poison:
        being.status_list.remove(self)

def limbexec(self):
    targetlimb = self.targets[0]
    target = targetlimb.being
    if randint(0, 100) > targetlimb.data["evade"]:
        #Hit
        dmg = self.data['dmg'] - targetlimb.data["DEF"]

        #if randint(0, 100) < self.actor.stats["crit"] + self.data["crit"]  - targetlimb.data["vuln"]:
         #   #Crit
          #  dmg *= 2
           # print("Critical!")
        targetlimb.data["HP"] -= dmg
        print("{}'s {} took {} DMG, it now has {} HP".format(target.name, targetlimb.name, self.data['dmg'], targetlimb.data["HP"]))
        if 'poison' in self.data:
            poison = limbpoison.instance(target, self.battle)
            poison.limb = targetlimb
            poison.poison = self.data['poison']
            target.status_list.append(poison)
            print("{}'s {} has been poisoned for {}".format(target.name, targetlimb.name, self.data['poison']))
    else:
        print("{}'s {} missed!".format(self.actor.name, self.name))

def enchant(self):
    self.targets[0].data['PWR'] *= 2

###REAL###
bite = api.Action('bite', {"exec":limbexec}, {"dmg":5, "poison":10, 'speed':2})
whip = api.Action('whip', {'exec':limbexec}, {"dmg":10, 'speed':2})
sting = api.Action('sting', {'exec':limbexec}, {'dmg':2, 'poison':20, 'speed':2})

fang = api.Limb("fang", [bite],  data={"HP":5, 'evade':60})
barb = api.Limb("barb", [sting], data={"HP":10, 'evade':40})
tail = api.Limb("tail", [whip],  data={"HP":40, 'evade':10}, stats={'speed':1})
head = api.Limb("head", data={"HP":30, "vital":True, "evade":30}, stats={'speed':1})

snake  = api.Being(((head, fang), tail), loony)
python = snake.instance('Python')
monty  = snake.instance('Montey')
flylord = api.Being((head, barb), loony).instance("Beezulbub")

stab  = api.Action('stab',  {'exec':limbexec}, {'dmg':5 , 'speed':1, 'poison':5})
punch = api.Action('punch', {'exec':limbexec}, {'dmg':15, 'speed':2})
kick  = api.Action('kick',  {'exec':limbexec}, {'dmg':20, 'speed':2})

knife = api.Belong("knife", 'arm', {}, [stab])
arm   = api.Limb("arm", [punch], 'arm', {"HP":30, "evade":20}, {'speed':0.5})
head  = api.Limb("head", [], data={"HP":20, "vital":True, "evade":40})
torso = api.Limb("torso", data={"HP":60, "vital":True}, stats={"speed":1})
leg   = api.Limb("leg", [kick], data={"HP":30, "evade":20}, stats={"speed":1})

man = api.Being((torso, (head, sym(fang)), sym(arm), sym(leg)), pthinker, {"speed": -3}, [knife])
player = man.instance("Player")
mad = man.instance("Huminoid Taco", loony, statchanges={"speed":1})

game = api.Net(0, {
    0: api.Node([], [], [
        ('say', "You'll fight an odd taco! (Hint: choose a limb, then an attack)"),
        ("battle", [player, mad]),
        ('say',"You must go on to fight wierder stuff!"),
        ("send", 1)
        ]),
    1: api.Node([], [], {'battle': [player, python],  "send": 2}),
    2: api.Node([], [], {'battle': [player, monty],   "send": 3}),
    3: api.Node([], [], {'battle': [player, flylord], "send": 4}),
    4: api.Node([], [], {"say": "That's all the battles to be had"}, exit_='hub')
})
