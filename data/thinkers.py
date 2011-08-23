def man(self, players):
    """A basic mundane thinker who
    attacks the player with the
    least HP with his first attack"""
    
    action = self.actions[0]
    #Choose the first action
    others = dict((k, v) for k, v in players.items() if v != self)
    #Make a dict of eavryone who isn't me
    lowest = (10, '')
    for player in others.items():
        otherhp = player[1].stats['hp']
        if otherhp < lowest[0]:
            lowest = (otherhp, player[0])
    action.target = lowest[1]
    return action

def player(self, players):
    for p in range(len(players)):
        player = players.values()[p]
        print '[T] {n}. {name}: {hp}'.format(n = p, name = player.name, hp = player.stats['hp'])
    choice = input('Choice? ')
    action = self.actions[0]
    action.target = players.keys()[choice]
    return action
