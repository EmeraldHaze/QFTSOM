"""
The Action api
"""
from collections import defaultdict
from core.utils import copy

class Action:
    def __init__(self, name, listners, metadata={}, mint=1, maxt=1):
        """
        Represents a possible actions. Args:
        name:str
        listners:dict, listners[event] is called at event (e.g, exec)
        metadata = {}, arbitrary data
        mint = 1, minimum targets
        maxt = 1, -1 = all, -2 = all but one, etc
        """
        self.name = name
        self.listners = defaultdict(lambda :lambda *args:None, listners)
        self.mint = mint
        self.maxt = maxt
        self.metadata = {"delay":0, "target":"norm", "MPC":0}
        self.metadata.update(metadata)

    def instance(self, actor, targets, battle):
        """
        Creates an instance of this action
        """
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
        new = ActionInstance(self, actor, targets, battle)
        new.listners["init"](new)
        return new

    def __repr__(self):
        return "<{}>".format(self.name)

class ActionInstance:
    def __init__(self, parent, actor, targets, battle):
        copy(self, parent, "name", "listners", "metadata")
        self.actor = actor
        self.targets = targets
        self.battle = battle

    def __repr__(self):
        return "<{}>".format(self.name)