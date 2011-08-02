from api.exit import exit
def ex(code): exec code

die = exit(lambda player:player.stats['hp']<0, lambda player, players:ex("if len(players) == 1: players.values()[0].stats['win'] = 1"))
win = exit(lambda player:player.stats['win'])
