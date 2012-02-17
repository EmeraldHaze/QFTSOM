api/exit.py:    the given player exited or not, and an effect (consequance) function.
api/limb.py:    def instance(self, player, uplimb=None, prefix=''):
api/limb.py:        return LimbInst(self, player, uplimb, prefix)
api/limb.py:    Represents a specific player's specific limb
api/limb.py:    def __init__(self, parent, player, uplimb, prefix):
api/limb.py:        self.player = player
api/limb.py:        print("{} has lost his {}!".format(self.player.name, self.name))
api/limb.py:        self.player.limbs.remove(self)
api/limb.py:        del self.player.limb_dict[self.name]
api/limb.py:            self.player.actions.remove(act)
api/limb.py:            del self.player.act_dict[act.name]
api/limb.py:            if status in self.player.status_list:
api/limb.py:                self.player.status_list.remove(status)
api/limb.py:            self.player.stats[stat] += value
api/limb.py:            self.player.stats[stat] -= value
api/limb.py:        return self.player.name + "'s " + self.name
api/net.py:    exit_: If set, exits the player to a higher network as named.
api/rule.py:    "schedule": ("How a player choice is be scheduled (timeline)", ["player"]),
api/rule.py:    "get_actions": ("How to build a player's actionlist", ["player"]),
api/rule.py:    "wipe_hist": ("How to remove previous battle history", ["player"]),
api/status.py:    def instance(self, player, battle):
api/status.py:        return StatusInst(self, player, battle)
api/status.py:    def __init__(self, parent, player, battle):
api/status.py:        self.player = player
api/thinker.py:    def instance(self, player):
api/thinker.py:        return ThinkerInst(self, player)
api/thinker.py:    "Represents a specific thinker of a specific player"
api/thinker.py:    def __init__(self, parent, player):
api/thinker.py:        self.player = player
api/thinker.py:        if len(self.player.actions):
api/thinker.py:            return null.instance(self.player, [], self.battle)
core/shared.py:#The player's name, used for logs and suchlike
game/nodeutils.py:    battleargs should be a list, of the form [{name:player}, {ruletype:rule},
game/nodeutils.py:             '(rules, which determine how to do a given thing, like player '
lib/base/rules.py:def same(battle, player):
lib/base/rules.py:    "All the players go at the same turn, with deaths being figured after everyone makes choices."
lib/base/rules.py:    battle.timeline.addplayer(player, 1)
lib/base/rules.py:def next(battle, player):
lib/base/rules.py:    split = battle.timeline.player
lib/base/rules.py:    battle.timeline.addplayer(player, tick - battle.timeline.tick)
lib/base/rules.py:def speed(battle, player):
lib/base/rules.py:    speed = player.stats["speed"]
lib/base/rules.py:    if player.last_act is not None:
lib/base/rules.py:        speed += player.last_act.metadata["speed"]
lib/base/rules.py:        print("{}'s {} has {} speed".format(player.name, player.last_act.name, speed))
lib/base/rules.py:    battle.timeline.addplayer(player, int(speed))
lib/base/rules.py:def get_all(battle, player):
lib/base/rules.py:    player.actions = []
lib/base/rules.py:    player.act_dict = {}
lib/base/rules.py:    for actgiver in player.limbs + player.equiped:
lib/base/rules.py:            player.actions.append(action)
lib/base/rules.py:            player.act_dict[name] = action
lib/base/rules.py:def wipe_normal(battle, player):
lib/base/rules.py:    if "MAXHP" in player.stats:
lib/base/rules.py:       player.stats["HP"] = player.stats["MAXHP"]
lib/base/rules.py:    player.actions = []
lib/base/rules.py:    player.status_list = []
lib/base/rules.py:def wipe_limbs(battle, player):
lib/base/rules.py:    for limb in player.limbs:
lib/base/rules.py:    player.actions = []
lib/base/rules.py:    player.status_list = []
lib/base/statuses.py:    player = self.player
lib/base/statuses.py:    print(player.name, "took", player.data['poison'], "damadge from poison")
lib/base/statuses.py:    player.stats["HP"] -= player.data['poison']
lib/base/statuses.py:    player.data['poison'] -= 1
lib/base/statuses.py:    if player.data['poison'] < 1:
lib/base/statuses.py:        player.status_list.remove(self)
lib/base/thinkers.py:        target = gettarget(self.player, self.battle)
lib/base/thinkers.py:        action = getaction(self.player, self.battle)
lib/base/thinkers.py:        return action.instance(self.player, target, self.battle)
lib/base/thinkers.py:def mosttarget(player, battle, cmp = int.__lt__):
lib/base/thinkers.py:    for enemy in battle.player_list:
lib/base/thinkers.py:        if enemy is not player:
lib/base/thinkers.py:least = lambda player, battle: mosttarget(player, battle, int.__gt__)
lib/base/thinkers.py:firstact = lambda player, battle: player.actions[0]
lib/base/thinkers.py:ptarget = lambda player, battle: pchoice(battle.player_list, ("HP", "choice.stats['HP']"), "Target? ")
lib/base/thinkers.py:paction = lambda player, battle: pchoice(player.actions, ("MP", "choice.metadata['MPC']"), "Actions? ")
lib/fancy.py:    for player in self.targets:
lib/fancy.py:        dodge = player.stats['Dodge']
lib/fancy.py:            print(player.name, "dodged the bomb!")
lib/fancy.py:            player.stats["HP"] -= dmg
lib/fancy.py:            print(player.name, "lost ", dmg, "vital energy in the blast!")
lib/limb.py:        target = next(target for target in self.battle.player_list if target != self.player)
lib/limb.py:        act = actchoice(self.player.act_dict)
lib/limb.py:        return act.instance(self.player, targetlimb, self.battle)
lib/limb.py:    player = self.player
lib/limb.py:    print("{}'s {} took {} DMG from poison, it now has {}".format(player.name, self.limb.name, self.poison, self.limb.data["HP"]))
lib/limb.py:        player.status_list.remove(self)
lib/limb.py:    target = targetlimb.player
lib/limb.py:player = man.instance("Player")
lib/limb.py:    0:api.Node([1], ["Advance!"], [('say', "You must fight a weird taco! (Hint: choose a limb to attack, then an attack)"), ("battle", [player, mad]), ('say',"You must go on to fight wierder stuff!")]),
lib/limb.py:    1:api.Node([2], ["Procced!"], {'battle': [player, python]}),
lib/limb.py:    2:api.Node([3], ["Procced!"], {'battle': [player, monty]}),
lib/limb.py:    3:api.Node([4], ["Procced!"], {'battle': [player, flylord]}),
lib/simple.py:player = baseman.instance("Player", pthinker, statchanges={"HP":1})
lib/simple.py:                [man, player, man2, staffo, oddman],
