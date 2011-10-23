def think_maker(gettarget, getaction):
    def thinker(self, battle):
        target = gettarget(self, battle)
        action = getaction(self, battle).copy(battle, at = "Copyed at "+self.name)
        ###AT
        action.complete(self, target, at="Pre-return at "+self.name)
        return action
    return thinker

def mosttarget(self, battle, cmp = int.__lt__):
    target = [None, float("inf")]
    for enemy in battle.player_list:
        if enemy != self:
            hp = enemy.stats["HP"]
            if cmp(hp, target[1]):
                target = [enemy, hp]
    return target[0]

least = lambda self, battle: mosttarget(self, battle, int.__gt__)

firstact = lambda self, battle: self.actions[0]

def ptarget(self, battle):
    print("Go", self.name + "!")
    for num in range(len(battle.player_list)):
        t = battle.player_list[num]
        print("{}: {}, HP: {}".format(num, t.name, t.stats["HP"]))
    target = battle.player_list[int(input("Target? "))]
    return target

def paction(self, battle):
    for num in range(len(self.actions)):
        a = self.actions[num]
        print("{}: {}, MP: {}".format(num, a.name, a.metadata["MPcost"]))
    action = self.actions[int(input("Action? "))]
    return action