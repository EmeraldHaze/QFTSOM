from api.exit import Exit

def reset(player):
    player.actions = []
    player.stats['HP'] = player.stats["MAXHP"]
    player.stats['MP'] = player.stats["MAXMP"]

def die_effect(player, battle):
    print(player.name, 'has become sane!')
    reset(player)

def win_effect(player, battle):
    print(player.name, "has attained insanity!")
    reset(player)
def win_check(player, battle):
    return len(battle.players) == 1 and list(battle.players.values())[0] == player


die = Exit('die', lambda player, players: player.stats['HP'] <= 0, die_effect, ["main", "HP"], ["players"])
win = Exit('win', win_check, win_effect, ['players'], ["players"])
