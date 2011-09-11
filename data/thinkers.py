"""
Thinkers files
Thinkers are functions that are given a player, players, and timeline.
Honest thinkers should not abuse this, and only use what info their player has
Returns an action with complete() called on it
"""
def man(self, battle):
    """A basic mundane thinker who
    attacks the player with the
    least HP with his first attack"""
    action = self.actions[0].copy()
    #Choose the first action
    action = action.copy('man thinker')
    #Use a copy so we don'y chnage the original
    others = [player for player in list(battle.players.values()) if player != self]
    #Make a dict of eavryone who isn't me
    lowest = (10, '')
    for player in others:
        otherHP = player.stats['HP']
        if otherHP < lowest[0]:
            lowest = (otherHP, player)
    action.complete(self, lowest[1])
    return action


def other_man(self, battle):
    """A wierd mundane thinker who
    attacks the player with the
    most HP"""

    action = self.actions[0].copy(battle)
    #Choose the first action
    others = [player for player in list(battle.players.values()) if player != self]
    #Make a dict of eavryone who isn't me
    most = (0, '')
    for player in others:
        otherHP = player.stats['HP']
        if otherHP > most[0]:
            most = (otherHP, player)
    action.complete(self, most[1])
    return action


def player(self, battle):
    available_acts = [action for action in self.actions if action.metadata['MPcost'] < self.stats['MP']]
    other = [player for player in list(battle.players.values()) if player != self][0]
    print("You have {} HP, {} MP, the Dwarf has {} HP".format(self.stats['HP'], self.stats["MP"], other.stats["HP"]))
    for p in range(len(available_acts)):
        print("{p}: {name} MP cost: {mp}".format(p = p, name = available_acts[p].name, mp = available_acts[p].metadata["MPcost"]))
    choice = eval(input('Choice? '))
    action = available_acts[choice].copy(battle)
    action = action.copy(battle)
    action.complete(self, other)
    return action

def dwarf(self, battle):
    other = [player for player in list(battle.players.values()) if player != self][0]
    action = self.actions[0].copy(battle)
    action.complete(self, other)
    return action
