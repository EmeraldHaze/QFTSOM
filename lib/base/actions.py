from api import Action

def simplemaker(name, dmg):
    def sexec(self):
        target = self.targets[0]
        print(target.name, "has lost", dmg, " health!")
        target.stats["HP"] -= dmg
    return Action(name, {"exec":sexec})

poke = simplemaker("poke", 1)
hit = simplemaker("hit", 2)