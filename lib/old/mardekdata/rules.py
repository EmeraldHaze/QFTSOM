from collections import defaultdict
from functools import reduce

####Tickers
def cycel_tick(battle):
    try:
        new = battle.timeline.tick % battle.cycel_len == 0
    except ZeroDivisionError:
        new = True
    if new:
        #print("New cycel!")
        cycel = sorted(battle.player_list, key = lambda player:player.stats["AGL"])
        battle.cycel_len = len(cycel)
        for tick in range(len(cycel)):
            battle.timeline.addplayer(cycel[tick], tick)
    statuses(battle)

def statuses(battle):
    for player in battle.player_list:
        for name, value in player.statuses.items():
            status, effect, value = value
            if status == -1:
                #Remove
                if effect == "sets":
                    for effect in value.split(", "):
                            sign, *rest = effect
                            if sign == "+":
                                if rest == "*":
                                    player.actionset = player.actionset.difference(*player.act_types.values())
                                else:
                                    player.actionset -= player.act_types[rest]
                            else:
                                if rest == "-":
                                    player.actionset = player.actionset.union(*player.act_types.values())
                                else:
                                    player.actionset |= player.act_types[rest]
                elif effect == "special":
                    if name == "paralysis":
                        player.actionset = player.actionset.union(*player.act_types.values())

                    elif name == "blind":
                        player.stats["ACC"] += 50

                    elif name == "berserk":
                        player.stats["STR"] /= 2
                        player.stats["random"] = True
                del player.statuses[status]
            elif status == 0:
                #Ignore
                pass
            elif status == 1:
                #Add
                if effect == "sets":
                    for effect in value.split(", "):
                        sign, *rest = effect
                        if sign == "-":
                            if rest == "*":
                                player.actionset = player.actionset.difference(*player.act_types.values())
                            else:
                                player.actionset -= player.act_types[rest]
                        else:
                            if rest == "*":
                                player.actionset = player.actionset.union(*player.act_types.values())
                            else:
                                player.actionset |= player.act_types[rest]
                elif effect == "special":
                    if name == "paralysis":
                        stop = randint(0, 1) > 0
                        if stop:
                            print(player.name, "is paralysed")
                            player.actionset = player.actionset.difference(*player.act_types.values())
                        else:
                            player.actionset = player.actionset.union(*player.act_types.values())

                    elif name == "blind":
                        player.stats["ACC"] -= 50

                    elif name == "Berserk":
                        player.stats["STR"] *= 2
                        player.stats["random"] = True

            elif status == 2:
                #Repeat
                if effect == "exec":
                    exec(value)

#####Inits#####
def teams(battle):
    battle.teams = defaultdict(lambda :[])
    for player in battle.player_list:
        battle.teams[player.data["team"]].append(player)
    cycl(battle)

#####Player actions#####
def act_divide(battle, player):
    player.act_types = defaultdict(lambda :set())
    for belong in player.belongs.values():
        for act in belong.actions:
            player.act_types[act.metadata["type"]].add(act.copy(battle))
    player.actionset = reduce(set.union, player.act_types.values())