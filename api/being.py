from core.utils import copy
from types import MethodType

class Being:
    """Fully descrbes an entity. """
    def __init__(self, name, limbs, thinker, stats, belongs, data={}, rules=None):
        self.name = name
        self.limbs = limbs
        self.thinker = thinker
        self.stats = stats
        self.belongs = belongs
        self.data = data
        if rules == None:
            from core.shared import statrules as rules
        for rule in rules:
            self.stats[rule[0]] = eval(rule[1])

class BeingInst:
    def __init__(self, parent):
        copy(self, parent, 'name', 'stats', 'data')
        self.limbs = []
        self.limb_dict = {}
        for limb in parent.limbs:
            limb = limb.instance(self)
            self.limbs.append(limb)
            self.limb_dict[limb.name] = limb
        self.thinker = parent.thinker.instance(self)
        self.equiped = []
        self.belongs = []
        self.belong_dict = {}
        for belong in parent.belongs:
            belong = belong.instance(self)
            self.belongs.append(belong)
            self.belong_dict[belong.name] = belong

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
                        return "{} equiped to {}".format(belong.name, limb.belong)
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

    def __repr__(self):
        return '<' + self.name + '>'