from api import Action
from game import defaults

def simplemaker(name, dmg, madeat):
    def sexec(self):
        target = self.targets[0]
        print(target.name, "has lost", dmg, " health!")
        target.stats["HP"] -= dmg
    return Action(name, {"exec":sexec}, madeat)

def complete_exec(self, rules = defaults.dmg_rules):
    if "extra" in self.metadata:
        extra = self.metadata["extra"].copy(self.battle)
        extra.complete(self.actor, self.targets)
        self.battle.timeline.addaction(extra,
            self.metadata["extra"].metadata['delay'])
    for target in self.targets:
        dmg = eval(rules[self.metadata["type"]])
        target.stats["HP"] -= dmg
        self.metadata['dmg'][target] = dmg
        print(target.name, "lost", dmg, "health!")

def manainit(self):
    self.metadata['dmg'] = {}
    self.actor.stats['MP'] -= self.metadata["MPcost"]

