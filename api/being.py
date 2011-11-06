from core.utils import copy
from types import MethodType

class Being:
    """
    Represents a possible entity in the game world
    Has a thinker, limbs, stats, belongs, data
    """
    def __init__(self, limbs, thinker, stats=None, belongs=None, data=None, rules=None):
        if stats is None:   stats = {"speed":0}
        if belongs is None: belongs = []
        if data is None:    data = {}
        self.limbs = limbs
        self.thinker = thinker
        self.stats = stats
        self.belongs = belongs
        self.data = data
        if rules == None:
            from core.shared import statrules as rules
        self.rules = rules

    def instance(self, name, thinker=None, statchanges={}, **changes):
        return BeingInst(self, name, thinker, statchanges, changes)

class BeingInst:
    """
    Represents a specific entity in the game world
    """
    def __init__(self, parent, name, thinker, statchanges, changes):
        copy(self, parent, 'stats', 'data', 'rules')
        self.name = name
        if not thinker:
            thinker = parent.thinker
        self.thinker = thinker.instance(self)

        for stat, value in statchanges.items():
            self.stats[stat] += value
        self.applyrules()

        self.limbs = []
        self.limb_dict = {}
        for limb in parent.limbs:
            limb = limb.instance(self)
            self.limbs.append(limb)
            self.limb_dict[limb.name] = limb

        self.equiped = []
        self.belongs = []
        self.belong_dict = {}
        for belong in parent.belongs:
            belong = belong.instance(self)
            self.addbelong(belong)

        for name, value in changes.items():
            if type(value) in (str, int, dict, list):
                value = type(value)(value)
            else:
                value = value.instance(self)
            setattr(self, name, value)

    def equip(self, belong, limb):
        if belong in self.belong_dict:
            belong = self.belong_dict[belong]
            if limb in self.limb_dict:
                limb = self.limb_dict[limb]
                if belong.equip is limb.equip:
                    if not belong.limb:
                        if limb.belong:
                            self.unequip(limb.belong.name)
                        limb.belong = belong
                        belong.limb = limb
                        belong.applystats()
                        self.equiped.append(belong)
                        return "{} equiped to {}".format(belong.name, limb.name)
                    else:
                        return "E: Belong already equiped"
                else:
                    return "E: Belong can not be equiped to this limb"
            else:
                return "E: No such limb"
        else:
            return "E: No such belong"

    def unequip(self, belong):
        if belong in self.belong_dict:
            belong = self.belong_dict[belong]
            limb = belong.limb
            limb.belong = None
            belong.limb = None
            belong.removestats()
            self.equiped.remove(belong)
        else:
            return "No such belong"

    def applyrules(self):
        for name, value in self.rules:
            self.stats[name] = eval(value)

    def addbelong(self, belong):
        """Adds a belonging to this being"""
        self.belongs.append(belong)
        self.belong_dict[belong.name] = belong

    def rmbelong(self, belong):
        """Removes a belonging from this being"""
        if type(belong) == str:
            belong = self.belongs_dict[belong]
        self.belongs.remove(belong)
        del self.belong_dict[belong.name]

    def __str__(self):
        return "<" + self.name + ">"
    __repr__ = __str__