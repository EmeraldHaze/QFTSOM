"""
Thinkers files
Thinkers are functions that are given a player, players, and timeline.
Honest thinkers should not abuse this, and only use what info their player has
Returns an action with complete() called on it
"""
def player(self, battle):
    people = list(battle.players.values())
    print("Targets:")
    for i in range(len(people)):
        print("{i}: {name}, HP:{hp}".format(i = i, name = people[i].name, hp = people[i].stats["HP"]))

    possib_acts = [action for action in self.actions if action.metadata['MPcost'] <= self.stats['MP']]
    print("Actions:")
    for i in range(len(possib_acts)):
        print("{i}: {name} MP cost: {mp}".format(i = i, name = possib_acts[i].name, mp = possib_acts[i].metadata["MPcost"]))

    target = int(input('Target? '))
    action = int(input('Action? '))
    action = possib_acts[action].copy(battle)
    action.complete(self, people[target])
    return action

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
