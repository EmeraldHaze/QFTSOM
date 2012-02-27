from collections import defaultdict
from core.utils import copy
from game import defaults


class Action:
    def __init__(self, name, listeners, data={}, mint=1, maxt=1):
        """
        Represents a possible action. Args:
        name:str
        listeners:dict, listeners[event] is called at event (e.g, exec)
        data = {}, arbitrary data
        mint = 1, minimum targets
        maxt = 1, -1 = all, -2 = all but one, etc
        """
        self.name = name
        self.listeners = defaultdict(lambda : lambda *args: None, listeners)
        self.listeners.update(defaults.actions.listeners)
        self.mint = mint
        self.maxt = maxt
        self.data = defaults.actions.data.copy()
        #Prevents the defaults from being changed
        self.data.update(data)

    def instance(self, actor, targets, battle):
        """
        Creates an instance of this action
        """
        if type(targets) != list:
            targets = [targets]

        ##Check that # of argumenst is within boundries
        invalid = Exception("%s tried to %s an invalid amount of targets" % (
            actor.name, self.name))

        if self.mint >= 0 and self.maxt >= 0:
            #If both boundries are positive
            if not (self.mint <= len(targets) <= self.maxt):
                #If the targets are not within the boundrys
                raise invalid

        elif self.mint <= 0 and self.maxt <= 0:
            #If both boundrys are negative or 0
            if abs(self.mint + 1) <= len(targets) <= abs(self.maxt + 1):
                #Accept this as a dogmatic condition which works magically
                targets = [being for being in battle.beings.values()\
                            if being not in targets]
            else:
                raise invalid
        else:
            raise Exception("Wierd maxt-mint")
        new = ActionInstance(self, actor, targets, battle)
        new.listeners["init"](new)
        return new

    def __repr__(self):
        return "<%s>" % self.name


class ActionInstance:
    "Represents a concrete action done by a being to another being(s)"
    def __init__(self, parent, actor, targets, battle):
        copy(self, parent, "name", "listeners", "data")
        self.actor = actor
        self.targets = targets
        self.battle = battle

    def __repr__(self):
        return "<{}>".format(self.name)
