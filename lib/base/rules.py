from api import rule, Rule

@rule('schedule')
def same(battle, player):
    battle.timeline.addplayer(player, 1)

@rule('schedule')
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

@rule('schedule')
def speed(battle, player):
    speed = player.data["speed"]
    if player.last_act is not None:
        speed += player.last_act.metadata["speed"]
        print("{}'s {} has {} speed".format(player.name, player.last_act.name, speed))
    battle.timeline.addplayer(player, speed)

@rule('get_actions')
def get_actions(battle, player):
    player.actions = []
    player.act_dict = {}
    for belong in player.belongs:
        for action in belong.actions:
            player.actions.append(action)
            player.act_dict[action.name] = action
