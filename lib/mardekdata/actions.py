from random import randint, choice
from api.action import Action

from pdb import set_trace

def execer(self):
    for target in self.targets:
        target.statuses.update(self.metadata["statuses"])

def attacker(self, target = None):
    if not target: target = self.targets[0]
    actor = self.actor
    dmg = actor.stats["STR"]+actor.stats["POW"]-target.stats["DEF"] if self.metadata["type"] == "Physical"\
    else actor.stats["SPR"]+actor.stats["POW"]-target.stats["MDEF"]

    reschange = (100-target.stats[self.metadata["element"]+"Res"])/100

    if "miss" in self.metadata:
        if randint(0, 100) > (self.actor.stats["ACC"] - self.metadata["miss"]):
            print("Miss!", end = " ")
            dmg *= 0

    if randint(0, 100) < target.stats["EVE"]:
        print("Evade!", end = " ")
        dmg *= 0

    if randint(0, 100)<=self.actor.stats["CRIT"]:
        print("Crit!", end = " ")
        dmg *= 2

    if self.metadata["type"] == "Physical" and "shield" in target.statuses:
        print("Shield'd!", end = " ")
        dmg /= 2

    elif self.metadata["type"] == "Magical" and "m. shield" in target.statuses:
        print("M. Shield'd!", end = " ")
        dmg /= 2

    if "mod" in self.metadata:
        dmg *= self.metadata["mod"]

    dmg = int(dmg)
    print(target.name, "has taken", dmg, " damadge!")
    target.stats["HP"]-=dmg

    if "statuses" in self.metadata:
        for status, value in self.metadata["statuses"].items():
            chance, value = value
            print("chance", chance)
            if randint(0, 100) > chance:
                print(target.name, "was", status+"'d")
                target.statuses[status] = value
    return dmg

def attacks(self):
    for target in self.targets:
        attacker(self, target)

special = (1, 'special', None)
shi = (0, "shi", None)
hp = lambda mod:(1, 'exec', "change = player.stat['MAXHP']*"+str(mod)+"\nprint(player.name, '\'s HP has changed by', change)\nplayer.stat['HP'] += change")
sets = lambda mod:(1, 'sets', mod)

attack = Action("attack", {"exec":attacker}, {"type":"Physical", "element":"Physical"})
powerattack = Action("attacker", {"exec":attacker}, {"type":"Physical", "element":"Physical", "mod":2})
avengance = Action("Avengance!", {"exec":execer}, {"statuses":{"berserk":special}, "type":"Magical"})

mshield = Action("m. shield", {"exec":execer}, {"statuses": {"m. shield":shi}, "type":"Magical"})
shield = Action("shield", {"exec":execer}, {"statuses": {"shield":shi}, "type":"Magical"})
regen = Action("regen", {"exec":execer}, {"statuses": {"regen":hp(0.1)}, "type":"Magical"})
cure = Action("cure", {"exec":attacker}, {"type":"Magical", "element":"Light", "mod":-1})

immolate = Action("immolate", {"exec":attacker}, {"type":"Magical", "element":"Fire"})
glaciate = Action("glaciate", {"exec":attacker}, {"type":"Magical", "element":"Water"})
thunderstorm = Action("thunderstorm", {"exec":attacks}, {"type":"Magical", "element":"Fire", "statuses":{"paralysis":(25, (2, "special", None))}, "target":"multi"}, 2, 10)

viperfang = Action("viperfang", {"exec":attacker}, {"type":"Physical", "element":"Earth", "statuses":{"poison":(95, hp(-0.02))}})
eyegouge = Action("eye gouge", {"exec":attacker}, {"type":"Physical", "element":"Dark", "statuses":{"blind":(95, special)}})
slumberstab = Action("slumberstab", {"exec":attacker}, {"type":"Physical", "element":"Air", "statuses":{"sleep":(95, sets("-*"))}})