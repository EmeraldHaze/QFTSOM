from api.exit import Exit

def ex(code): exec code

def die_effect(player, players):
    if len(players) == 1: players.values()[0].stats['win'] = 1
    print player.name, 'has died!'
    
die = Exit(lambda player:player.stats['hp']<=0, die_effect)
win = Exit(lambda player:player.stats['win'], lambda player, players:ex('print player.name, "has won!"'))
