class being:
    """Fully descrbes an entity. """
    def __init__(self, name, thinker, stats, belongings, params = {}):
        self.think = thinker
        self.stats = stats
        self.belongs = belongings
        self.params = params
        self.actions = []
        for belong in self.belongs.values:addbelong(belong)

    def addbelong(self, belong):
        if type(belong) == str: belong = self.belongs[belong]
        for stat in belong.stats.items(): stat.stats[stat[0]] += stat[1]

    def rmbelong(self, belong):
        if type(belong) == str: belong = self.belongs[belong]
        for stat in belong.stats.items(): self.stats[stat[0]] -= stat[1]
        
