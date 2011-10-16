from types import MethodType
from pdb import set_trace

class Being:
    """Fully descrbes an entity. """
    def __init__(self, name, thinker, stats, belongs, data = {},  thinkinit = lambda *args:None, rules=None):
        self.think = MethodType(thinker, self)
        self.thinkinit = MethodType(thinkinit, self)
        self.stats = stats
        self.belongs = []
        self.data = data
        self.name = name
        if rules == None:
            from game.defaults import statrules as rules
        for rule in rules:
            self.stats[rule[0]] = eval(rule[1])
        for belong in belongs:
            self.addbelong(belong)

    def __repr__(self):
        return '<' + self.name + '>'

    def addbelong(self, belong):
        """Adds a belonging to this being"""
        self.belongs.append(belong)
        for stat in list(belong.stats.items()):
            self.stats[stat[0]] += stat[1]

    def changestats(self, stat, change, actor):
        self.stats[stat] += change
        self.happenings.append([stat, change, actor])

    def rmbelong(self, belong):
        """Removes a belonging from this being"""
        self.belongs.remove(belong)
        if type(belong) == str:
            belong = self.belongs[belong]
        for stat in list(belong.stats.items()):
            self.stats[stat[0]] -= stat[1]
