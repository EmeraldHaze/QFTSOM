from types import MethodType
from pdb import set_trace

class Being:
    """Fully descrbes an entity. """
    def __init__(self, name, thinker, stats, belongs, data = {},  thinkinit = lambda *args:None, rules=None):
        self.think = MethodType(thinker, self)
        self.thinkinit = MethodType(thinkinit, self)
        self.stats = stats
        self.data = data
        self.status_list = []
        self.name = name
        if rules == None:
            from core.shared import statrules as rules
        for rule in rules:
            self.stats[rule[0]] = eval(rule[1])

        self.belongs = []
        for belong in belongs:
            self.addbelong(belong)

    def __repr__(self):
        return '<' + self.name + '>'

    def addbelong(self, belong):
        """Adds a belonging to this being"""
        for stat in list(belong.stats.items()):
            self.stats[stat[0]] += stat[1]
        self.belongs.append(belong)

    def rmbelong(self, belong):
        """Removes a belonging from this being"""
        if type(belong) == str:
            name = belong
            for belong in self.belongs:
                if belong.name == name:
                    break#this leaves belong at the right value
        for stat in list(belong.stats.items()):
            self.stats[stat[0]] -= stat[1]
        self.belongs.remove(belong)

    def changestats(self, stat, change, actor):
        self.stats[stat] += change
        self.happenings.append([stat, change, actor])