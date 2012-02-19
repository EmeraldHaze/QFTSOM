from core.utils import copy


class Belong:
    """
    Represents something that can be possesed (e.g, a sword, a spell)
    """
    def __init__(self, name, equip,
            stats={}, actions=[], data={}, datarules=None):
        self.name = name
        self.equip = equip
        #What type of limb this belong can be equipped to
        self.actions = actions
        #Actions this belong confers
        self.stats = stats
        self.data = data
        if not datarules:
            from core import shared
            datarules = shared.belongdata
        for name, value in datarules:
            self.data[name] = eval(value)

    def instance(self, owner):
        return BelongInst(self, owner)

    def __str__(self):
        return "<" + self.name + ">"

    __repr__ = __str__


class BelongInst:
    """
    Represents an specific belonging of a specific person.
    """
    def __init__(self, parent, owner):
        copy(self, parent, 'name', 'equip', 'stats', 'actions', 'data')
        self.owner = owner
        self.limb = None
        #This belong is equipped to no limb

    def applystats(self):
        "Applies this belong's stats [e.g, when equipped]'"
        for stat, value in self.stats.items():
            self.owner.stats[stat] += value

    def removestats(self):
        "Removes this belong's stats, as when unequipped'"
        for stat, value in self.stats.items():
            self.owner.stats[stat] -= value
