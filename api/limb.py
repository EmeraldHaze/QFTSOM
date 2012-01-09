from core.utils import copy


class Limb:
    """
    Represents a possible limb of a being
    Normally used as equip slots, but exits and actions can be based on their
    data which could, for example, have an 'HP' key.
    """
    def __init__(self, name,
            actions=None, equip=None, data=None, stats=None, rules=None):

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

    def instance(self, player, uplimb=None, prefix=''):
        return LimbInst(self, player, uplimb, prefix)


class LimbInst:
    """
    Represents a specific player's specific limb
    """
    def __init__(self, parent, player, uplimb, prefix):
        copy(self, parent, 'data', 'stats', 'actions', 'equip', 'rules')
        self.prefix = prefix
        self.name = prefix + parent.name
        self.player = player
        self.belong = None
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
        print("{} has lost his {}!".format(self.player.name, self.name))
        self.player.limbs.remove(self)
        del self.player.limb_dict[self.name]

        for act in self.actions:
            self.player.actions.remove(act)
            del self.player.act_dict[act.name]

        for limb in self.attached:
            limb.kill()

        for status in self.status_list:
            if status in self.player.status_list:
                self.player.status_list.remove(status)
        if self.uplimb:
            self.uplimb.attached.remove(self)

    def applydatarules(self):
        for name, value in self.rules:
            self.data[name] = eval(value)

    def applystats(self):
        for stat, value in self.stats.items():
            self.player.stats[stat] += value

    def removestats(self):
        for stat, value in self.stats:
            self.player.stats[stat] -= value

    def __str__(self):
        return self.player.name + "'s " + self.name


def sym(limb):
    limb.sym = True
    return limb
