def same(battle, player):
    battle.timeline.addplayer(player, 1)

def next(battle, player):
    split = battle.timeline.player
    for tick in range(len(split)):
        if split[tick] == []:
            break
            #This leaves tick at the first tick when there's a nobody
    battle.timeline.addplayer(player, tick - battle.timeline.tick)

def get_actions(battle, player):
    player.actions = []
    for belong in player.belongs:
        for action in belong.actions:
            player.actions.append(action.copy(battle, "Start at "+player.name))
