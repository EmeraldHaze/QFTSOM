from core.utils import copy

class Limb:
    def __init__(name, equip = None, data={}, stats={}):
        self.equip = equip
        self.name = name
        self.data = data
        self.stats = stats

    def instance(self, player):
        return LimbInst(self, player)

class LimbInst:
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
