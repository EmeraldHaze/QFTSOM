"""
The Action api
"""
from collections import defaultdict

class Action:
    def __init__(self, name, listners, metadata={}, mint=1, maxt=1, madeat="Uknown"):
        """
        This describes an Action. Args:
        name:str, used for IDing
        listners:dict. listners[event] is called at an event like exec. This is a defaultdict
        madeat:str, used for tracking
        metadata = {}, arbitrary data
        mint = 1, minimum targets
        maxt = 1, -1 = all, -2 = all but one, etc
        """
        self.name = name
        self.madeat = madeat
        self.listners = defaultdict(lambda :lambda *args:None, listners)
        self.mint = mint
        self.maxt = maxt
        self.metadata = {"delay":0, "target":"norm", "MPcost":0}
        self.metadata.update(metadata)

    def format(self, battle, actor, targets = None):
        """
        This formats the action details correctly. It also:
        checks targets against maxt/mint"""
        if targets == None:
            targets = []
        if type(targets) != list:
            targets = [targets]

        if self.mint >= 0 and self.maxt >= 0:
            #If both boundries are positive
            if not (self.mint <= len(targets) <= self.maxt):
                #If the targets are not within the boundrys
                raise Exception(actor.name+\
                "'s thinker passed an invalid amount of targets to action "+self.name)
        elif self.mint <= 0 and self.maxt <= 0:
            #If both boundrys are negative or 0
            if abs(self.mint + 1) <= len(targets) <= abs(self.maxt + 1):
                #Accept this as a dogmatic condition which works magically
                targets = [player for player in battle.players.values()\
                if player not in targets]
            else:
                raise Exception(actor.name+\
                "'s thinker passed an invalid amount of targets to action "+self.name)
        else:
            raise Exception("Wierd maxt-mint")
        self.listners['init'](actor, self, targets)
        return actor, self, targets

    def __repr__(self):
        return "<{} #{}, made at {}>".format(self.name,
            hex(id(self))[2:],
            self.madeat)