from api import Action
from random import randint
def simplemaker(name, dmg):
    def sexec(self, battle):
        target = self.targets[0]
        print(target.name, "has lost", dmg, " health!")
        target.stats["HP"] -= dmg
    return Action(name, {"exec":sexec})

def complete_exec(self):
    rules = self.dmgrules
    if "status" in self.metadata:
        status = self.metadata["status"].instance(targets[0])
        targets[0].status_list.append(status)
    if "data" in self.metadata:
        name, value = self.metadata["data"]
        targets[0].data[name] = value
    for target in targets:
        dmg = eval(rules[self.metadata["type"]])
        target.stats["HP"] -= dmg
        print(target.name, "lost", dmg, "health!")

def manainit(actor, self, targets):
    actor.stats['MP'] -= self.metadata["MPcost"]