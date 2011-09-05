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

    action = self.actions[0]
    #Choose the first action
    action = action.copy('man thinker')
    #Use a copy so we don'y chnage the original
    others = dict([(k, v) for k, v in battle.players.items() if v != self])
    #Make a dict of eavryone who isn't me
    lowest = (10, '')
    for player in others.items():
        otherhp = player[1].stats['hp']
        if otherhp < lowest[0]:
            lowest = (otherhp, player[0])
    action.complete(self, lowest[1])
    return action


def other_man(self, battle):
    """A wierd mundane thinker who
    attacks the player with the
    most HP"""

    action = self.actions[0]
    #Choose the first action
    others = dict([(k, v) for k, v in battle.players.items() if v != self])
    #Make a dict of eavryone who isn't me
    most = (0, '')
    for player in others.items():
        otherhp = player[1].stats['hp']
        if otherhp > most[0]:
            most = (otherhp, player[0])
    action.complete(self, most[1])
    return action


def player(self, battle):
    for p in range(len(battle.players)):
        player = battle.players.values()[p]
        print '[T] {n}. {name}: {hp}'.format(n=p,
            name=player.name,
            hp=player.stats['hp'])
    choice = input('Choice? ')
    action = self.actions[0]
    action = action.copy('player thinker')
    action.complete(self, battle.players.keys()[choice])
    return action
