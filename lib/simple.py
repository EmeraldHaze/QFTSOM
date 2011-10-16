import api, lib

default = {"MAXHP": "self.stats['HP']"}

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
    for num in range(len(battle.player_list)):
        t = battle.player_list[num]
        print("{}: {}, HP: {}".format(num, t.name, t.stats["HP"]))
    target = battle.player_list[int(input("Target? "))]
    return target

def paction(self, battle):
    for num in range(len(self.actions)):
        a = self.actions[num]
        print("{}: {}, HP: {}".format(num, a.name))
    target = battle.player_list[int(input("Action? "))]
    return target

manthinker = think_maker(mosttarget, firstact)
oddthinker = think_maker(least, firstact)
player = think_maker(ptarget, firstact)
thinker = manthinker

stick = api.Belong("stick", {}, [lib.base.actions.poke])
staff = api.Belong("staff", {}, [lib.base.actions.hit])

##                 NAME        THINKER     STATS     BELONGS
player = api.Being('Player',   player,     {'HP': 6}, [stick])
man    = api.Being('Man',      manthinker, {'HP': 5}, [stick])
man2   = api.Being('OtherMan', manthinker, {'HP': 4}, [stick])
oddman = api.Being('Oddball',  oddthinker, {'HP': 5}, [stick])
staffo = api.Being('Staffo',   manthinker, {'HP': 5}, [staff])