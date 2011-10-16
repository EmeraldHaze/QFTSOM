def simple(self, battle):
    process_threat(self)
    target = sorted(self.enemies, key = compare_threat)[0][0]
    #print(self.enemies)
    action = self.actions[0]
    action.complete(self, target)
    return action

def process_threat(self):
    for enemy in self.enemies:
        dmg = 0
        lastact = enemy[0].last_act
        if lastact:
            if self in lastact.metadata['dmg']:
                dmg = lastact.metadata['dmg'][self]

        if enemy[1]['admg given'] == None:
            enemy[1]['admg given'] = dmg
        else:
            enemy[1]['admg given'] = (dmg + enemy[1]['admg given']) / 2

        dmgtaken = enemy[0].stats["HP"] - enemy[1]["lasthp"]
        if enemy[1]['admg taken'] == None:
            enemy[1]['admg given'] = dmg
        else:
            enemy[1]['admg taken'] = (dmg + enemy[1]['admg taken']) / 2

def compare_threat(player):
    player, stats = player
    taken = stats["admg taken"]
    if taken == None or taken <= 0:
        life_turns = float("inf")
    else:
        life_turns = player.stats["HP"]/taken
    return life_turns*stats["admg given"]

def stdinit(self, battle):
    self.enemies = [(player, {"admg given":None, "admg taken":None, "lasthp":player.stats["HP"]}) for player in battle.players.values() if player != self]