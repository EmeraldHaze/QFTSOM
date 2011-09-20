from collections import defaultdict

def same(battle, player):
    battle.timeline.addplayer(player, 1)

def next(battle, player):
    split = battle.timeline.player
    for tick in range(len(split)):
        if split[tick] == []:
            break
    battle.timeline.addplayer(player, tick - battle.timeline.tick)

def cycel_tick(battle):
    try:
        #print("len:", battle.cycel_len, "tick", battle.timeline.tick, "mod:", battle.timeline.tick % battle.cycel_len)
        new = battle.timeline.tick % battle.cycel_len == 0
    except ZeroDivisionError:
        new = True

    if new:
        print("New cycel!")
        cycel = sorted(battle.player_list, key = lambda player:player.stats["AGL"])
        battle.cycel_len = len(cycel)
        for tick in range(len(cycel)):
            battle.timeline.addplayer(cycel[tick], tick)

null = lambda battle, player:None

def teams(battle):
    battle.teams = defaultdict(lambda :[])
    for player in battle.player_list:
        battle.teams[player.data["team"]].append(player)
    cycl(battle)

def cycl(battle):
    battle.cycel_len = 0


