import api, lib

def think_maker(gettarget):
    def thinker(self, battle):
        target = gettarget(self, battle)
        action = self.actions[0].copy(battle)
        action.complete(self, target)
        return action
    return thinker

def mosthp(self, battle):
    target = [None, float("inf")]
    for enemy in battle.player_list:
        if enemy != self:
            hp = enemy.stats["HP"]
            if hp < target[1]:
                target = [enemy, hp]
    return target[0]

def ptarget(self, battle):
    for num in range(len(battle.player_list)):
        t = battle.player_list[num]
        print("{}: {}, HP: {}".format(num, t.name, t.stats["HP"]))
    target = battle.player_list[int(input("Choice? "))]
    return target

thinker = think_maker(mosthp)
player = think_maker(ptarget)

stick = api.Belong("stick", {}, [lib.base.actions.poke])

man = api.Being("man", thinker, {"HP":6}, [stick])
player = api.Being("player", player, {"HP":7}, [stick])