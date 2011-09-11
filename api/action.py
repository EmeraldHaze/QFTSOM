from collections import defaultdict
class Action:
    def __init__(self, name, listners, mintargets = 1, maxtargets = 1, metadata = {"delay":0}):
        self.name = name
        self.listners = defaultdict(lambda :lambda *args:None, listners)
        self.mint = mintargets
        self.maxt = maxtargets
        self.metadata = metadata
        self.copy_status = 0

    def copy(self, battle):
        new = Action(self.name, self.listners, self.mint, self.maxt, self.metadata)
        new.battle = battle
        new.copy_stats = self.copy_status + 1
        return new

    def complete(self, actor, targets):
        self.actor = actor
        if type(targets) != list:
            targets = [targets]

        if self.mint >= 0 and self.maxt >= 0:
            if self.mint <= len(targets) <= self.maxt:
                self.targets = targets
            else:
                raise Exception(self.actor.name+\
                "'s thinker passed an invalid amount of targets to action "+self.name)

        elif self.mint < 0 and self.maxt < 0:
            if abs(self.mint + 1) <= len(targets) <= abs(self.maxt + 1):
                self.targets = [player for player in self.battle.players.values if player not in targets]
            else:
                raise Exception(self.actor.name+\
                "'s thinker passed an invalid amount of targets to action "+self.name)
        self.listners['init'](self)
