import api, lib

def think_maker(gettarget):
    def thinker(self, battle):
        gettarget(self, battle)
        action = self.actions[0]
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
    return target

def ptarget(self, battle):
    for num in range(len(battle.player_list)):
        t = battle.player_list[num]
        print("{}: {}, HP: {}".format(num, target.name, target.stats["HP"]))
    return battle.player_list[int(input("Choice? "))]

thinker = think_maker(mosthp)
player = think_maker(ptarget)

stick = api.Belong("stick", {}, [lib.base.actions.poke])

man = api.Being("Man", thinker, {"HP":6}, {"stick": stick})
player = api.Being("Player", player, {"HP":7}, {"stick": stick})