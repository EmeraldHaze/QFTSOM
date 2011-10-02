def next(battle, player):
    battle.timeline.addplayer(player, 1)

def actions(battle, player):
    player.actions = []
    for belong in player.belongs:
        for action in belong.actions:
            player.actions.append(action.copy(battle))
