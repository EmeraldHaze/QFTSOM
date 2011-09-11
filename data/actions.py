from random import randint
from api.action import Action
from pdb import set_trace
def execmaker(dmg):
    def exec_listner(self):
        for target in self.targets:
            target.stats["HP"] -= dmg
            print(target.name, "lost", dmg, "health!")
    return exec_listner

def exec_from_dict(d):
    def exec_(self):
        for change in d.items():
            for target in self.targets:
                target.stats[change[0]] -= change[1]
    return exec_

poke = Action('poke', {"exec":execmaker(1)})
hit = Action('hit', {"exec":execmaker(2)})

dmg_rules = {"melee":"self.actor.stats['STR']+\
randint(self.actor.stats['MINWPNDMG'], self.actor.stats['MAXWPNDMG'])-\
target.stats['DEF']*self.metadata['change']",
"magic":"self.actor.stats['INT']*2*\
randint(self.actor.stats['MINWPNDMG'], self.actor.stats['MAXWPNDMG'])-\
target.stats['MDEF']*self.metadata['change']"}

def simple_exec(self):
    dmg = dmg_rules[self.metadata["type"]]
    self.actor.stats['MP'] -= self.metadata["MPcost"]
    for target in self.targets:
            dmg = eval(dmg)
            target.stats["HP"] -= dmg
            print(target.name, "lost", dmg, "health!")

def special_exec(self):
    n = 30
    self.actor.stats["HP"] += n
    print(self.actor.name, "has gained", n, "HP")

bolt = Action('bolt', {"exec":simple_exec}, metadata = {"delay":0, "type":"magic", "MPcost":60, 'change':1})
hack = Action('hack', {"exec":simple_exec}, metadata = {"delay":0, "type":"melee", 'change':1, 'MPcost': 0})
heal = Action("heal", {"exec":special_exec}, metadata = {"delay":1, "MPcost":20})
rest = Action("rest", {"exec":simple_exec}, metadata = {"delay":0, "type":"magic", "MPcost":0, 'change': 0})