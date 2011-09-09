from api.exit import Exit

def die_effect(player, battle):
    print player.name, 'has died!'

def win_effect(player, battle):
    print player.name, "has won!"
    player.stats['HP'] = player.stats["MAXHP"]

def win_check(player, battle):
    return len(battle.players) == 1 and battle.players.values()[0] == player


die = Exit(lambda player, players: player.stats['HP'] <= 0, die_effect, ["main", "HP"], ["players"])
win = Exit(win_check, win_effect, ['players'], ["players"])
