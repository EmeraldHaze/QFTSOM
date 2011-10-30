def think_maker(gettarget, getaction):
    def thinker(self, battle):
        action = getaction(self, battle)
        target = gettarget(self, battle)
        return action.format(self, target, battle)
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

def pchoice(choices, extra = None, query = "Choice? "):
    for num, t in enumerate(choices):
        if not extra:
            print("{}: {}".format(num, t.name))
        else:
            name, code = extra
            print("{}: {}, {}: {}".format(num, t.name, name, eval(code)))
    choice_ = choices[int(input(query))]
    return choice_

def ptarget(self, battle):
    for num, t in enumerate(battle.player_list):
        print("{}: {}, HP: {}".format(num, t.name, t.stats["HP"]))
    target = battle.player_list[int(input("Target? "))]
    return target

def paction(self, battle):
    for num, a in enumerate(self.actions):
        print("{}: {}, MP: {}".format(num, a.name, a.metadata['MPcost']))
    target = self.actions[int(input("Action? "))]
    return target