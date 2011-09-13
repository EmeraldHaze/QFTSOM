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
"magic":"(self.actor.stats['INT']*\
randint(self.actor.stats['MINWPNDMG'], self.actor.stats['MAXWPNDMG'])-\
target.stats['MDEF'])*self.metadata['change']"}

def simple_exec(self):
    for target in self.targets:
            dmg = eval(self.dmg)
            self.metadata['dmg'][target] = dmg
            print(target.name, "lost", dmg, "health!")

def special_exec(self):
    self.actor.stats['MP'] -= self.metadata["MPcost"]
    n = 30
    self.actor.stats["HP"] += n
    print(self.actor.name, "has gained", n, "HP")

def simpleinit(self):
    self.dmg = dmg_rules[self.metadata["type"]]
    self.metadata['dmg'] = {}
    self.actor.stats['MP'] -= self.metadata["MPcost"]

bolt = Action('bolt', {"exec":simple_exec, "init":simpleinit}, metadata = {"delay":0, "type":"magic", "MPcost":60, 'change':1})
hack = Action('hack', {"exec":simple_exec, "init":simpleinit}, metadata = {"delay":0, "type":"melee", 'MPcost': 0, 'change':1})
rest = Action("rest", {"exec":simple_exec, "init":simpleinit}, metadata = {"delay":0, "type":"magic", "MPcost": -40, 'change':0})
heal = Action("heal", {"exec":special_exec}, metadata = {"delay":1, "MPcost":20})