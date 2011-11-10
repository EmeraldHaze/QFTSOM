from api import Thinker

def think_maker(gettarget, getaction):
    @Thinker
    def thinker(self):
        action = getaction(self.player, self.battle)
        target = gettarget(self.player, self.battle)
        return action.instance(self.player, target, self.battle)
    return thinker

def mosttarget(player, battle, cmp = int.__lt__):
    target = [None, float("inf")]
    for enemy in battle.player_list:
        if enemy is not player:
            hp = enemy.stats["HP"]
            if cmp(hp, target[1]):
                target = [enemy, hp]
    return target[0]

least = lambda player, battle: mosttarget(player, battle, int.__gt__)
firstact = lambda player, battle: player.actions[0]

def pchoice(choices, extra = None, query = "Choice? "):
    for num, choice in enumerate(choices):
        if not extra:
            print("{}: {}".format(num, choice.name))
        else:
            name, code = extra
            print("{}: {}, {}: {}".format(num, choice.name, name, eval(code)))
    choice_ = None
    while not choice_:
        try:
            choice_ = choices[int(input(query))]
        except (ValueError, IndexError):
            print("Bad choice! Bad!")
    return choice_

ptarget = lambda player, battle: pchoice(battle.player_list, ("HP", "choice.stats['HP']"), "Target? ")
paction = lambda player, battle: pchoice(player.battle_list, ("MP", "choice.metadata['MPC']"), "Actions? ")