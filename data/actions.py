from random import randint
from api.action import Action
from pdb import set_trace
def execmaker(dmg):
    def exec_listner(self):
        for target in self.targets:
            target.stats["HP"] -= dmg
            print(target.name, "lost", dmg, "health!")
    return exec_listner

poke = Action('poke', {"exec":execmaker(1)})
hit = Action('hit', {"exec":execmaker(2)})

dmg_rules = {"melee":"self.actor.stats['STR']+\
randint(self.actor.stats['MINWPNDMG'], self.actor.stats['MAXWPNDMG'])-\
target.stats['DEF']",
"magic":"self.actor.stats['INT']*2*\
randint(self.actor.stats['MINWPNDMG'], self.actor.stats['MAXWPNDMG'])-\
target.stats['MDEF']"}

def simple_exec(self):
    dmg = dmg_rules[self.metadata["type"]]

    for target in self.targets:
            try:
                dmg = eval(dmg)
            except: set_trace()
            target.stats["HP"] -= dmg
            print(target.name, "lost", dmg, "health!")

bolt = Action('bolt', {"exec":simple_exec}, metadata = {"delay":0, "type":"magic"})
hack = Action('hack', {"exec":simple_exec}, metadata = {"delay":0, "type":"melee"})
heal = Action("heal", {"exec":execmaker(-10)}, metadata = {"delay":1})
