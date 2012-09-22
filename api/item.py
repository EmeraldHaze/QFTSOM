from core.utils import copy_attrs, Settings
from api import Real, PotentialReal


class RealItem(Real):
    """Represents an specific iteming of a specific person."""
    def __init__(self, parent, name):
        copy_attrs(self, parent, 'equip', 'stats', 'actions', 'data')
        self.name = name
        self.owner = None
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
    defaults = Settings(
        datarules = [],
        data = {}
    )
    def __init__(self, equip, stats={}, actions=[], data={}, datarules=None):
        self.equip = equip
        #What type of limb this item can be equipped to
        self.actions = actions
        #Actions this item confers
        self.stats = stats
        self.data = data
        if datarules is None:
            datarules = self.defaults.datarules
        for name, value in datarules:
            self.data[name] = eval(value)

    def __str__(self):
        return "<" + self.name + ">"

    __repr__ = __str__



