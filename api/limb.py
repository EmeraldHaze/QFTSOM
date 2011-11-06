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
    def __init__(self, name, actions=None, equip=None, data=None, stats=None, attached=[]):
        if actions is None: actions = []
        if data is None:    data = {}
        if stats is None:   stats = {}
        self.name = name
        self.equip = equip
        self.actions = actions
        self.attached = attached
        self.data = data
        self.stats = stats

    def instance(self, player):
        return LimbInst(self, player)

class LimbInst:
    """
    Represents a specific player's specific limb
    """
    def __init__(self, parent, player):
        copy(self, parent, 'name', 'data', 'actions', 'stats', 'equip')
        self.player = player
        self.belong = None
        self.attached = []
        for limb in parent.attached:
            limb = limb.instance(player)
            player.limbs.append(limb)
            if limb.name in player.limb_dict:
                limb.name += 2
            player.limb_dict[limb.name] = limb
            self.attached.append(limb)
        self.applystats()

    def kill(self):
        print("{} has lost his {}!".format(self.player.name, self.name))
        self.player.limbs.remove(self)
        del self.player.limb_dict[self.name]
        for act in self.actions:
            self.player.actions.remove(act)
            del self.player.act_dict[act.name]
        for limb in self.attached:
            limb.kill()

    def applystats(self):
        for stat, value in self.stats.items():
            self.player.stats[stat] += value

    def removestats(self):
        for stat, value in self.stats:
            self.player.stats[stat] -= value