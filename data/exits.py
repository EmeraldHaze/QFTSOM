from api.exit import Exit


def ex(code):
    exec code


def die_effect(player, players):
    if len(players) == 1:
        players.values()[0].stats['win'] = 1
    player.stats['win'] = 0
    print player.name, 'has died!'


def win_effect(player, players):
    print player.name, "has won!"
    player.stats['hp'] = player.stats["maxhp"]
    player.stats['win'] = 0


def win_check(player, players):
    return len(players) == 1 and players.values[0] == player

die = Exit(lambda player, players: player.stats['hp'] <= 0, die_effect)
win = Exit(win_check, win_effect)
