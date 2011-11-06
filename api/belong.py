"""
The Belong class
"""
from core.utils import copy

class Belong:
    """
    Represents something that can be possesed (e.g, a sword, a spell)
    """
    def __init__(self, name, equip, stats={}, actions=[], data ={}, datarules = None):
        self.name = name
        self.equip = equip
        self.actions = actions
        self.stats = stats
        self.data = {}
        if not datarules:
            from core import shared
            datarules = shared.belongdata
        for name, value in datarules:
            self.data[name] = eval(value)
        self.data.update(data)

    def instance(self, owner):
        return BelongInst(self, owner)

    def __str__(self):
        return "<" + self.name + ">"

    __repr__ = __str__

class BelongInst:
    """
    Represents an specific belonging of a specific person
    """
    def __init__(self, parent, owner):
        copy(self, parent, 'name', 'equip', 'stats', 'actions', 'data')
        self.owner = owner
        self.limb  = None

    def applystats(self):
        for stat, value in self.stats:
            self.player.stats[stat] += value

    def removestats(self):
        for stat, value in self.stats:
            self.player.stats[stat] -= value