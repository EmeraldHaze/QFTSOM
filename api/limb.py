"""
The Limb class
"""
from core.utils import copy

class Limb:
    """
    Represents a possible limb of a being
    Normally used for equips, but exits and actions can be based on there data
    which could, for example, have an 'HP' key
    """
    def __init__(name, equip = None, data={}, stats={}):
        self.equip = equip
        self.name = name
        self.data = data
        self.stats = stats

    def instance(self, player):
        return LimbInst(self, player)

class LimbInst:
    """
    Represents a specific player's specific limb
    """
    def __init__(self, parent, player):
        copy(self, parent, 'name', 'data', 'stats', 'equip')
        self.player = player
        self.belong = None
        self.applystats()

    def applystats(self):
        for stat, value in self.stats:
            self.player.stats[stat] += value

    def removestats(self):
        for stat, value in self.stats:
            self.player.stats[stat] -= value
