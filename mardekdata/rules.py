from collections import defaultdict

def same(battle, player):
    battle.timeline.addplayer(player, 1)

def next(battle, player):
    split = battle.timeline.player
    for tick in range(len(split)):
        if split[tick] == []:
            break
    battle.timeline.addplayer(player, tick - battle.timeline.tick)

def agl(battle, player):
    if len(battle.cycle) < battle.cycletick:
        battle.cycle = sort(battle.player_list, key = lambda player:player.stats["AGL"])
        battle.cycletick = 0
    battle.cycletick += 0
    tick = battle.cycle.index[player]
    battle.timeline.schedule(player, tick)

def teams(battle):
    battle.teams = deafultdict(lambda :[])
    for player in battle.player_list:
        battle.teams[player.data["team"]].append(player)

def init(battle):
    teams(battle)
    battle.cycle = []
    battle.cycletick = 1