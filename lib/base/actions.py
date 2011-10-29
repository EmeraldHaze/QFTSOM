from api import Action

def simplemaker(name, dmg, madeat = 'Unknown with simplemaker'):
    def sexec(actor, self, targets, battle):
        target = targets[0]
        print(target.name, "has lost", dmg, " health!")
        target.stats["HP"] -= dmg
    return Action(name, {"exec":sexec}, madeat = madeat)

def complete_exec(actor, self, targets, battle):
    rules = self.dmgrules
    if "extra" in self.metadata:
        extra = self.metadata["extra"]
        battle.timeline.addaction(extra.format(actor, targets, battle),
            self.metadata["extra"].metadata['delay'])
    for target in targets:
        dmg = eval(rules[self.metadata["type"]])
        target.stats["HP"] -= dmg
        self.metadata['dmg'][target] = dmg
        print(target.name, "lost", dmg, "health!")

def manainit(self):
    self.metadata['dmg'] = {}
    self.actor.stats['MP'] -= self.metadata["MPcost"]

