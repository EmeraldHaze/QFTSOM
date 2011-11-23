"""
The Limb class
"""
from core.utils import copy

def sym(limb):
    limb.sym = True
    return limb

class Limb:
    """
    Represents a possible limb of a being
    Normally used for equips, but exits and actions can be based on there data
    which could, for example, have an 'HP' key
    """
    def __init__(self, name, actions=None, equip=None, data=None, stats=None):
        if actions is None: actions = []
        if data is None:    data = {}
        if stats is None:   stats = {}
        self.name = name
        self.equip = equip
        self.actions = actions
        self.data = data
        self.stats = stats
        self.sym = False
        #This will be used for symetric-ness

    def instance(self, player, uplimb=None, prefix=''):
        return LimbInst(self, player, uplimb, prefix)

class LimbInst:
    """
    Represents a specific player's specific limb
    """
    def __init__(self, parent, player, uplimb, prefix):
        copy(self, parent, 'data', 'actions', 'stats', 'equip')
        self.prefix = prefix
        self.name = prefix + parent.name
        self.player = player
        self.belong = None
        self.attached = []
        self.uplimb = uplimb
        if uplimb:
            uplimb.attached.append(self)
        self.applystats()

    def kill(self):
        print("{} has lost his {}!".format(self.player.name, self.name))
        self.player.limbs.remove(self)
        del self.player.limb_dict[self.name]
        for act in self.actions:
            self.player.actions.remove(act)
            self.player.act_dict = {n: v for n, v in self.player.act_dict.items() if v is not act}
        for limb in self.attached:
            limb.kill()

    def applystats(self):
        for stat, value in self.stats.items():
            self.player.stats[stat] += value

    def removestats(self):
        for stat, value in self.stats:
            self.player.stats[stat] -= value