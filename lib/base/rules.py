def same(battle, player):
    battle.timeline.addplayer(player, 1)

def next(battle, player):
    split = battle.timeline.player
    for tick in range(len(split)):
        try:
            go = split[tick] == [] and split[tick+1] == []
        except:
            go = split[tick] == []
        if go:
            break
            #This leaves tick at the first tick when there's a nobody
    battle.timeline.addplayer(player, tick - battle.timeline.tick)

def get_actions(battle, player):
    player.actions = []
    player.act_dict = {}
    for belong in player.belongs:
        for action in belong.actions:
            player.actions.append(action)
            player.act_dict[action.name] = action
