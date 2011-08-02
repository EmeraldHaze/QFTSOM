class being:
    """Fully descrbes an entity. """
    def __init__(self, name, thinker, stats, belongings, params = {}):
        self.thinker = thinker
        self.stats = stats
        self.belongs = belongings
        self.params = params
        for belong in belongs.values():addbelong(belong)

    def addbelong(self, belong):
        if type(belong) == str: belong = self.belongs[belong]
        for stat in belong.items(): stat.stats[stat[0]] += stat[1]

    def rmbelong(self, belong):
        if type(belong) == str: belong = self.belongs[belong]
        for stat in belong.items(): self.stats[stat[0]] -= stat[1]
        
