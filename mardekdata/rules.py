from collections import defaultdict
def same(battle, player):
    battle.timeline.addplayer(player, 1)

def next(battle, player):
    split = battle.timeline.player
    for tick in range(len(split)):
        if split[tick] == []:
            break
    battle.timeline.addplayer(player, tick - battle.timeline.tick)

def init(battle):
    battle.teams = deafultdict(lambda :[])
    for player in battle.player_list:
        battle.teams[player.data["team"]].append(player)