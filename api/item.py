from core.utils import copy
from api import Real, PotentialReal

class RealItem(Real):
    """Represents an specific iteming of a specific person."""
    def __init__(self, parent, owner):
        copy(self, parent, 'name', 'equip', 'stats', 'actions', 'data')
        self.owner = owner
        self.limb = None
        #This item is equipped to no limb

    def applystats(self):
        "Applies this item's stats [e.g, when equipped]'"
        for stat, value in self.stats.items():
            self.owner.stats[stat] += value

    def removestats(self):
        "Removes this item's stats, as when unequipped'"
        for stat, value in self.stats.items():
            self.owner.stats[stat] -= value


class Item(PotentialReal):
    """
    Represents something that can be possesed (e.g, a sword, a spell)
    """
    inst = RealItem
    def __init__(self, name, equip,
            stats={}, actions=[], data={}, datarules=None):
        self.name = name
        self.equip = equip
        #What type of limb this item can be equipped to
        self.actions = actions
        #Actions this item confers
        self.stats = stats
        self.data = data
        if not datarules:
            from core import shared
            datarules = shared.itemdata
        for name, value in datarules:
            self.data[name] = eval(value)

    def __str__(self):
        return "<" + self.name + ">"

    __repr__ = __str__



