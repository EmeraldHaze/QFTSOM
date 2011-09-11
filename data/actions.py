from api.action import Action
def simplelistners(dmg):
    def exec_listner(self):
        for target in self.targets:
            target.stats["HP"] -= dmg
    return {"exec":exec_listner}
poke = Action('poke', simplelistners(1))
hit = Action('hit', simplelistners(2))

