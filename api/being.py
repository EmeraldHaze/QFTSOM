from types import MethodType

from game import defaults
from core import shared
from core.utils import copy
from api import Real, PotentialReal


class RealBeing(Real):
    """Represents a specific entity in the game world"""
    plural = "beings"

    def __init__(self, parent, name,
                 thinker=None, items=[], statchanges={}, changes={}):
        copy(self, parent, 'stats', 'data', "base_actions")
        self.name = name

        if not thinker:
            thinker = parent.thinker
        self.thinker = thinker.instance(self)

        for stat, value in statchanges.items():
            self.stats[stat] += value
            #Local rules for stat modificiations

        for stat, value in parent.rules:
            self.stats[stat] = eval(value)
            #Personal rules for stat definition that default to global rules

        self.limbs = []
        self.limb_dict = {}
        self.buildbody(parent.body)

        self.equiped = []
        self.items = []
        self.item_dict = {}
        for item in parent.items + items:
            item = item.instance(self)
            self.additem(item)
        #self.equipall()

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
        Recursivly builds a body. A body looks roughly like this: (limb,
        limb, (rootlimb, *attached_limbs))
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
                    newlimbs.append(item.instance(self, uplimb, 'left '))
                    newlimbs.append(item.instance(self, uplimb, 'right '))
                else:
                    newlimbs.append(item.instance(self, uplimb))

        for limb in newlimbs:
            self.limbs.append(limb)
            self.limb_dict[limb.name] = limb

    def equip(self, item, limb):
        """Equips a item to a limb, by names (so that you can't spoof)"""
        if type(item) is not str:
            item = item.name
        if type(limb) is not str:
            limb = limb.name
        if item in self.item_dict:
            item = self.item_dict[item]
            if limb in self.limb_dict:
                limb = self.limb_dict[limb]
                if item.equip is limb.equip:
                    if not item.limb:
                        if limb.item:
                            self.unequip(limb.item.name)
                        limb.item = item
                        item.limb = limb
                        for action in item.actions:
                            self.addaction(action, self.thinker.game)
                        item.applystats()
                        self.equiped.append(item)
                        return True, "{} equiped his {} to his {}".format(
                            self.name,
                            item.name,
                            limb.name
                        )
                    else:
                        return False, "E: %s already equiped" % item.name
                else:
                    return False, "E: %s can't be equiped to %s" % (
                        item.name, limb.name)
            else:
                return False, "E: No such limb, " + limb
        else:
            return False, "E: No such item, " + item

    def equipall(self):
        "Attempts to equip everything."
        for item in self.items:
            if not self.equip(item.name, item.equip)[0]:
                if not self.equip(item.name, "right " + item.equip)[0]:
                    R = self.equip(item.name, "left " + item.equip)
                    if not R[0]:
                        #If it didn't sucessfully equip, print the error msg.
                        print(R[1])

    def unequip(self, item):
        "Removes an equiped item, by name"
        if item in self.item_dict:
            item = self.item_dict[item]
            if item.limb:
                limb = item.limb
                limb.item = None
                item.limb = None
                item.removestats()
                for action in item.actions:
                    self.rmaction(action)
                self.equiped.remove(item)
            else:
                return "Not equipped"
        else:
            return "No such item"

    def additem(self, item):
        "Adds a item to this being (this function does it right)"
        self.items.append(item)
        self.item_dict[item.name] = item

    def rmitem(self, item):
        "Removes a iteming from this being"
        if type(item) == str:
            item = self.item_dict[item]
        self.unequip(item.name)
        self.items.remove(item)
        del self.item_dict[item.name]

    def addaction(self, action, game=False):
        action = action.instance(self, game)
        self.actions.append(action)
        self.act_dict[action.name] = action

    def rmaction(self, action):
        if type(action) is str:
            action = self.act_dict[action]
        else:
            action = filter(self.actions, lambda a: a.parent is action)[0]
        self.actions.remove(action)
        del self.act_dict[action]

    def __str__(self):
        return self.name

    __repr__ = __str__


class Being(PotentialReal):
    """
    Represents a possible entity in the game world
    Has a thinker, limbs, stats, items, data
    """
    inst = RealBeing
    def __init__(self, body, thinker,
                 stats=None, items=None, data=None, rules=None):
        if stats is None:
            stats = defaults.beings.stats
        if items is None:
            items = []
        if data is None:
            data = defaults.beings.data

        self.body = body
        self.thinker = thinker
        self.stats = stats
        self.items = items
        self.data = data

        if rules is None:
            from core.shared import rules
            rules = rules.being_stats
        self.rules = rules

        from core.shared import misc
        self.base_actions = misc.base_actions
