from api import rule, Rule

@rule('schedule')
def same(battle, player):
    battle.timeline.addplayer(player, 1)

@rule('schedule')
def next(battle, player):
    split = battle.timeline.player
    for tick in range(len(split)):
        try:
            go = (split[tick] == [] and split[tick+1] == [])
        except IndexError:
            go = (split[tick] == [])
        if go:
            break
            #This leaves tick at the first tick when there's a nobody
    battle.timeline.addplayer(player, tick - battle.timeline.tick)

@rule('schedule')
def speed(battle, player):
    speed = player.stats["speed"]
    if player.last_act is not None:
        speed += player.last_act.metadata["speed"]
        print("{}'s {} has {} speed".format(player.name, player.last_act.name, speed))
    battle.timeline.addplayer(player, int(speed))

@rule('get_actions')
def get_actions(battle, player):
    player.actions = []
    player.act_dict = {}
    for actgiver in set(player.equiped) | set(player.limbs):
        for action in actgiver.actions:
            try:
                name = actgiver.prefix + action.name
            except AttributeError:
                name = action.name
            player.actions.append(action)
            player.act_dict[name] = action

@rule('wipe_hist')
def reset(battle, player):
    if "MAXHP" in player.stats:
       player.stats["HP"] = player.stats["MAXHP"]
    player.actions = []
    player.status_list = []