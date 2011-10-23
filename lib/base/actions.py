from api import Action

def simplemaker(name, dmg, madeat):
    def sexec(self):
        target = self.targets[0]
        print(target.name, "has lost", dmg, " health!")
        target.stats["HP"] -= dmg
    return Action(name, {"exec":sexec}, madeat)
###AT
poke = simplemaker("poke", 1, "lib")
hit = simplemaker("hit", 2, "lib")