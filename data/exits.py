from api.exit import Exit

def die_effect(player, battle):
    print player.name, 'has died!'

def win_effect(player, battle):
    print player.name, "has won!"
    player.stats['hp'] = player.stats["maxhp"]

def win_check(player, battle):
    return len(players) == 1 and players.values()[0] == player


die = Exit(lambda player, players: player.stats['hp'] <= 0, die_effect, ["main", "hp"], ["players"])
win = Exit(win_check, win_effect, ['players'], ["players"])
