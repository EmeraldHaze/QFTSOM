from random import randint, choice
from api.action import Action

from pdb import set_trace

def execer(self):
    for target in self.targets:
        target.status.update(self.metadata["status"])

def attack(self):
    target = self.targets[0]
    actor = self.actor
    dmg = actor.stats["STR"]+actor.stats["POW"]-target.stats["DEF"] if self.metadata["type"] == "Physical"\
    else actor.stats["SPR"]+actor.stats["POW"]-target.stats["MDEF"]

    dmg *= target.stats[self.element+"Res"]

    if "miss" in self.metadata:
        if randint(0, 100) < self.metadata["miss"]:
            print("Miss!", end = " ")
            dmg *= 0

    if randint(0, 100) < target.stats["EVE"]:
        print("Evade!", end = " ")
        dmg *= 0

    if randint(0, 100)<=self.actor.stats["CRIT"]:
        print("Crit!", end = " ")
        dmg *= 2

    if self.metadata["type"] == "Physical" and "m. sheild" in target.status or self.metadata["type"] == "Magical" and "sheild" in target.status:
        print("Sheild'd", end = " ")
        dmg /= 2

    if "mod" in self.metadata:
        dmg *= self.metadata["mod"]

    dmg = int(dmg)
    print(target.name, "has taken", dmg, " damadge!")
    target.stats["HP"]-=dmg

    if "status" in self.metadata:
        for status, chance in self.metadata["status"].items():
            if randint(0, 100) > chance:
                print(target.name, "was", status+"'d")
                target.status[status] = 1
    return dmg

attack = Action("attack", {"exec":attack}, {"type":"Physical", "element":"Physical"})
powerattack = Action("attack", {"exec":attack}, {"type":"Physical", "element":"Physical", "mod":2})
avengance = Action("Avengance!", {"exec":execer}, {"status":{"berserk":1}})

msheild = Action("m. sheild", {"exec":execer}, {"status":{"m. shield":1}, "type":"Magical"})
sheild = Action("sheild", {"exec":execer}, {"status":{"shield":1}, "type":"Magical"})
regen = Action("regen", {"exec":execer}, {"status":{"regen":1}, "type":"Magical"})
cure = Action("cure", {"exec":attack}, {"type":"Magical", "element":"Light", "mod":-1})

immolate = Action("immolate", {"exec":attack}, {"type":"Magical", "element":"Fire"})
glaciate = Action("glaciate", {"exec":attack}, {"type":"Magical", "element":"Water"})
thunderstorm = Action("immolate", {"exec":attack}, {"type":"Magical", "element":"Fire", "status":{"paralysis":25}}, 2, 10)

viperfang = Action("viperfang", {"exec":attack}, {"type":"Physical", "element":"Earth", "status":{"poison":35}})
eyegouge = Action("eye gouge", {"exec":attack}, {"type":"Physical", "element":"Dark", "status":{"blind":35}})
slumberstab = Action("slumberstab", {"exec":attack}, {"type":"Physical", "element":"Air", "status":{"sleep":35}})