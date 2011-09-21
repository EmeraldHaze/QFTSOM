from collections import defaultdict
class Action:
    def __init__(self, name, listners, metadata = {}, mintargets = 1, maxtargets = 1):
        self.name = name
        self.listners = defaultdict(lambda :lambda *args:None, listners)
        self.mint = mintargets
        self.maxt = maxtargets
        self.metadata = {"delay":0, "target":"norm"}
        self.metadata.update(metadata)
        self.copy_status = 0
        self.completed = False

    def copy(self, battle):
        new = Action(self.name, self.listners, self.metadata, self.mint, self.maxt)
        for item in dir(self):
            try:
                setattr(new, item, getattr(self, item))
            except AttributeError: pass
        new.battle = battle
        return new

    def complete(self, actor, targets = []):
        self.actor = actor
        if type(targets) != list:
            targets = [targets]

        if self.mint >= 0 and self.maxt >= 0:
            if self.mint <= len(targets) <= self.maxt:
                self.targets = targets
            else:
                raise Exception(self.actor.name+\
                "'s thinker passed an invalid amount of targets to action "+self.name)

        elif self.mint <= 0 and self.maxt <= 0:
            if abs(self.mint + 1) <= len(targets) <= abs(self.maxt + 1):
                self.targets = [player for player in self.battle.players.values() if player not in targets]
            else:
                raise Exception(self.actor.name+\
                "'s thinker passed an invalid amount of targets to action "+self.name)
        else:
            print("Wierd mint/maxt")
        self.listners['init'](self)
        self.completed = True
    def __repr__(self):
        return "<"+self.name+">"
