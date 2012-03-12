from core.utils import copy
from api import Real, PotentialReal

class RealLimb(Real):
    """Represents a specific being's specific limb"""
    def __init__(self, parent, being, uplimb=None, prefix=""):
        copy(self, parent, 'data', 'stats', 'actions', 'equip', 'rules')
        self.prefix = prefix
        self.name = prefix + parent.name
        self.being = being
        self.item = None
        self.status_list = []
        self.attached = []
        self.uplimb = uplimb
        if uplimb:
            uplimb.attached.append(self)

        self.applydatarules()
        self.applystats()

    def kill(self):
        """
        Kills this limb. Removes from limb lists, removes limb's actions,
        removes statuses, kills sub-limbs, removes from uplimb.
        """
        print("{} has lost his {}!".format(self.being.name, self.name))
        self.being.limbs.remove(self)
        del self.being.limb_dict[self.name]

        for act in self.actions:
            for being_act in self.being.actions:
                if being_act.parent is act:
                    self.being.actions.remove(being_act)
            for name, act in self.being.act_dict.copy().items():
                if being_act.parent is act:
                    del self.being.act_dict[name]

        for limb in self.attached:
            limb.kill()

        for status in self.status_list:
            if status in self.being.status_list:
                self.being.status_list.remove(status)
        if self.uplimb:
            self.uplimb.attached.remove(self)

    def applydatarules(self):
        for name, value in dict(self.rules).items():
            #self.rules is sometimes a dict and sometimes a [(k, v)*]
            try:
                self.data[name] = eval(value)
            except TypeError:
                #if it's not code
                self.data[name] = value

    def applystats(self):
        for stat, value in self.stats.items():
            self.being.stats[stat] += value

    def removestats(self):
        for stat, value in self.stats:
            self.being.stats[stat] -= value

    def __str__(self):
        return self.being.name + "'s " + self.name


def sym(limb):
    limb.sym = True
    return limb


class Limb(PotentialReal):
    """
    Represents a possible limb of a being
    Normally used as equip slots, but exits and actions can be based on their
    data which could, for example, have an 'HP' key.
    """
    inst = RealLimb

    def __init__(self, name,
            actions=None, data=None, stats=None, rules=None, equip=None):

        if actions is None:
            actions = []
        if data is None:
            data = {}
        if stats is None:
            stats = {}

        self.name = name
        if equip:
            self.equip = equip
        else:
            self.equip = name

        self.actions = actions
        self.data = data
        self.stats = stats
        self.sym = False
        #This will be used for symetric-ness
        if rules is None:
            from core.shared import limb_datarules as rules
        self.rules = rules
