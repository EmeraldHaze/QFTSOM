from types import MethodType
from game import defaults
from core import shared
from core.utils import copy


class Being:
    """
    Represents a possible entity in the game world
    Has a thinker, limbs, stats, belongs, data
    """
    def __init__(self, body, thinker, stats=None, belongs=None, data=None, rules=None):
        if stats is None:
            stats = defaults.beings.stats
        if belongs is None:
            belongs = []
        if data is None:
            data = defaults.beings.data

        self.body = body
        self.thinker = thinker
        self.stats = stats
        self.belongs = belongs
        self.data = data

        if rules is None:
            from core.shared import statrules as rules
        self.rules = rules

    def instance(self, name, thinker=None, belongs=[], statchanges={},
                    **changes):
        return BeingInst(self, name, thinker, belongs, statchanges, changes)


class BeingInst:
    "Represents a specific entity in the game world"
    plural = "beings"

    def __init__(self, parent, name, thinker, belongs, statchanges, changes):
        copy(self, parent, 'stats', 'data')
        self.name = name

        if not thinker:
            thinker = parent.thinker
        self.thinker = thinker.instance(self)

        for stat, value in parent.rules:
            self.stats[stat] = eval(value)
            #Personal rules for stat definition that default to global rules
        for stat, value in statchanges.items():
            self.stats[stat] += value
            #Local rules for stat modificiations


        self.limbs = []
        self.limb_dict = {}
        self.buildbody(parent.body)

        self.equiped = []
        self.belongs = []
        self.belong_dict = {}
        for belong in parent.belongs + belongs:
            belong = belong.instance(self)
            self.addbelong(belong)
        self.equipall()

        for name, value in changes.items():
            if type(value) in (str, int, dict, list):
                value = type(value)(value)
                #Makes a copy of the value, so we don't change the original
            else:
                value = value.instance(self)
            setattr(self, name, value)

        shared.register(self)

    def buildbody(self, limbs, uplimb=None):
        """
        Recursivly builds a body.
        A body looks roughly like this: (limb, (rootlimb, *attached_limbs))
        """
        newlimbs = []
        for item in limbs:
            try:
                root, *limbs = item
                root = root.instance(self, uplimb)
                newlimbs.append(root)
                self.buildbody(limbs, root)
                #If it's not a sequance, this will error
            except TypeError:
                if item.sym:
                    #If it's symetric
                    newlimbs.append(item.instance(self, uplimb, 'Left '))
                    newlimbs.append(item.instance(self, uplimb, 'Right '))
                else:
                    newlimbs.append(item.instance(self, uplimb))

        for limb in newlimbs:
            self.limbs.append(limb)
            self.limb_dict[limb.name] = limb

    def equip(self, belong, limb):
        "Equips a belong to a limb, by names (so that you can't spoof)"
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
                        return True, "%s equiped to %s" % (belong.name,
                            limb.name)
                    else:
                        return False, "E: %s already equiped" % belong.name
                else:
                    return False, "E: %s can't be equiped to this limb, %s" % (
                        belong.name, limb.name)
            else:
                return False, "E: No such limb, " + limb
        else:
            return False, "E: No such belong, " + belong

    def equipall(self):
        "Attempts to equip everything."
        for belong in self.belongs:
            if not self.equip(belong.name, belong.equip)[0]:
                if not self.equip(belong.name, "Right " + belong.equip)[0]:
                    R = self.equip(belong.name, "Left " + belong.equip)
                    if not R[0]:
                        #If it didn't sucessfully equip, print the error msg.
                        print(R[1])

    def unequip(self, belong):
        "Removes an equiped belong, by name"
        if belong in self.belong_dict:
            belong = self.belong_dict[belong]
            if belong.limb:
                limb = belong.limb
                limb.belong = None
                belong.limb = None
                belong.removestats()
                self.equiped.remove(belong)
            else:
                return "Not equipped"
        else:
            return "No such belong"

    def addbelong(self, belong):
        "Adds a belong to this being (this function does it right)"
        self.belongs.append(belong)
        self.belong_dict[belong.name] = belong

    def rmbelong(self, belong):
        "Removes a belonging from this being"
        if type(belong) == str:
            belong = self.belong_dict[belong]
        self.unequip(belong.name)
        self.belongs.remove(belong)
        del self.belong_dict[belong.name]

    def __str__(self):
        return self.name

    __repr__ = __str__
