def man(self, players):
    action = self.actions[0]
    action.target = players.keys()[0]
    return action

def player(self, players):
    print '(Thinker)HP (him):',players.values()[0].stats['hp']
    choice = input('Choice? ')
    action = self.actions[choice]
    action.target = players.keys()[1]
    return action
