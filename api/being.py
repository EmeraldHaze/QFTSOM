from data import statrules
from types import MethodType

class Being:
    """Fully descrbes an entity. """
    def __init__(self, name, thinker, stats, belongings,
        params={}, rules=statrules.default):
        self.think = MethodType(thinker, self, Being)
        self.stats = stats
        self.belongs = belongings
        self.params = params
        self.actions = []
        self.name = name
        for belong in self.belongs.values():
            self.addbelong(belong)
        for rule in rules.items():
            self.stats[rule[0]] = eval(rule[1])

    def __repr__(self):
        return '<' + self.name + '>'

    def addbelong(self, belong):
        if type(belong) == str:
            belong = self.belongs[belong]
        for stat in belong.stats.items():
            stat.stats[stat[0]] += stat[1]

    def rmbelong(self, belong):
        if type(belong) == str:
            belong = self.belongs[belong]
        for stat in belong.stats.items():
            self.stats[stat[0]] -= stat[1]
