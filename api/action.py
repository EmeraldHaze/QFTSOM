from collections import defaultdict
seen_targets = []
class Action:
    def __init__(self, name, listners, metadata = {}, mintargets = 1, maxtargets = 1, madeat = "Not Given", ):
        """
        This describes an Action. Args:
        name:str, used for IDing
        listners:dict. listners[event] is called at an event like exec. This is a defaultdict
        madeat:str, used for tracking
        metadata = {}, arbitrary data
        mintargets = 1,
        maxtargets = 1, -1 = all, -2 = all but one, etc
        """
        ###AT
        self.name = name
        self.madeat = madeat
        self.listners = defaultdict(lambda :lambda *args:None, listners)
        self.mint = mintargets
        self.maxt = maxtargets
        self.metadata = {"delay":0, "target":"norm", "MPcost":0}
        self.metadata.update(metadata)
        self.copy_status = 0
        self.completed = False

    def copy(self, battle, at = 'Unkown'):
        ###AT
        new = Action(self.name, self.listners, self.metadata, self.mint, self.maxt, madeat = at)
        #for item in dir(self):
        #    if not item.startswith("_") and item != "madeat":
        #        try:
        #            setattr(new, item, getattr(self, item))
        #        except AttributeError:
        #            pass
        new.battle = battle
        return new

    def complete(self, actor, targets = None, at = "Unknown"):
        if targets == None:
            targets = []
        self.actor = actor
        self.completer = at
        if targets in seen_targets:
            raise Exception("Target is the same")
        else:
            pass
            #seen_targets.append(targets)
        if type(targets) != list:
            targets = [targets]

        if self.mint >= 0 and self.maxt >= 0:
            if not (self.mint <= len(targets) <= self.maxt):
                raise Exception(self.actor.name+\
                "'s thinker passed an invalid amount of targets to action "+self.name)

        elif self.mint <= 0 and self.maxt <= 0:
            if abs(self.mint + 1) <= len(targets) <= abs(self.maxt + 1):
                targets = [player for player in self.battle.players.values() if player not in targets]
            else:
                raise Exception(self.actor.name+\
                "'s thinker passed an invalid amount of targets to action "+self.name)
        else:
            raise Exception("Wierd maxt-mint")
        self.targets = targets
        self.listners['init'](self)
        self.completed = True
        #print("TID:", hex(id(self.targets)))

    def __repr__(self):
        if self.completed:
            return "<{} #{}, made at {} targets: {}".format(self.name,
                hex(id(self))[2:],
                self.madeat,
                self.targets)
        else:
            return "<{} #{}, made at {}>".format(self.name,
                hex(id(self))[2:],
                self.madeat)


