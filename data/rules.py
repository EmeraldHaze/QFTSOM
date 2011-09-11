def same(battle, player):
    battle.timeline.addplayer(player, 1)

def next(battle, player):
    battle.timeline.addplayer(player, len(battle.timeline.player)-1)
