from random import randint, choice
from api.action import Action

from pdb import set_trace

def execer(self):
    for target in self.targets:
        target.status.update(self.metadata["status"])

def attack(self):
    target = self.targets[0]
    actor = self.actor
    dmg = actor.stats["STR"]+actor.stats["POW"]-target.stats["DEF"]
    dmg *= target.stats[self.element+"Res"]
    if randint(0, 100)<=self.actor.stats["CRIT"]:
        print("Crit!", end = " ")
        dmg *= dmg
    print(target.name, "has taken", dmg, " damadge!")
    target.stats["HP"]-=dmg

msheild = Action("m. sheild", {"exec":execer}, metadata = {"delay":0, "status":{"m. sheild":"")