from api import rule, Rule

@rule('schedule')
def same(battle, player):
    "All the players go at the same turn, with deaths being figured after everyone makes choices."
    battle.timeline.addplayer(player, 1)

@rule('schedule')
def next(battle, player):
    "Players go one after the other in a pre-determined order, with there actions having consequances immideatly."
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
    "Players go their speed stat + last action's speed turns from now, these turns may overlap. Will error when speed is not defined."
    speed = player.stats["speed"]
    if player.last_act is not None:
        speed += player.last_act.metadata["speed"]
        print("{}'s {} has {} speed".format(player.name, player.last_act.name, speed))
    battle.timeline.addplayer(player, int(speed))

@rule('get_actions')
def get_all(battle, player):
    "Gets actions from both equipment and limbs. Should always work."
    player.actions = []
    player.act_dict = {}
    for actgiver in player.limbs + player.equiped:
        for action in actgiver.actions:
            try:
                name = actgiver.prefix + action.name
            except AttributeError:
                name = action.name
            player.actions.append(action)
            player.act_dict[name] = action

@rule('wipe_hist')
def wipe_normal(battle, player):
    "resets HP to MAXHP if such exists, and some internals. Should always work."
    if "MAXHP" in player.stats:
       player.stats["HP"] = player.stats["MAXHP"]
    player.actions = []
    player.status_list = []

@rule("wipe_hist")
def wipe_limbs(battle, player):
    "Resets HP to MAXHP per-limb. Only works when limb HP is defined."
    for limb in player.limbs:
        limb.data["HP"] = limb.data["MAXHP"]
    player.actions = []
    player.status_list = []
