"""
Thinkers files
Thinkers are functions that are given a player, players, and timeline.
Honest thinkers should not abuse this, and only use what info their player has
Returns an action with complete() called on it
"""
from random import randint, choice

def player(self, battle):
    people = list(battle.players.values())
    print("Targets:")
    for i in range(len(people)):
        print("{i}: {name}, HP:{hp}".format(i = i, name = people[i].name, hp = people[i].stats["HP"]))

    possib_acts = [action for action in self.actions]
    print("Actions:")
    for i in range(len(possib_acts)):
        print("{i}: {name} MP cost: {mp}".format(i = i, name = possib_acts[i].name, mp = possib_acts[i].metadata["MPcost"]))

    target = int(input('Target? '))
    action = int(input('Action? '))
    action = possib_acts[action].copy(battle)
    action.complete(self, people[target])
    return action

def healer(self, battle):
    wounded = [ally for ally in self.battle.player_list if ally.data["team"] == self.data["team"] and ally.stats["HP"]/ally.stats["MAXHP"] < 0.7]
    if len(wounded):
        action = self.act_dict["cure"]
        action.complete(self, wounded[0])
    else:
        action = choice("sheild", "m. shield", "regen")
        targets = [ally for ally in self.battle.player_list if ally.data["team"] == self.datga["team"] and action not in ally.status]
        while not targets:
            print("Remaking choice")
            action = choice("sheild", "m. shield", "regen")
            targets = [ally for ally in self.battle.player_list if ally.data["team"] == self.datga["team"] and action not in ally.status]
        acttion.complete(self, target)
    return action

def attacker(self, battle):
    action = choice(self.actions)
    if action.metadata["target"] == "norm":
        action.complete(self, choice(battle.player_list))
    else:
        action.complete(self, battle.teams["mar"])
    return action

def bart(self, battle):
    if len(battle.teams[self.data["team"]]) == 1 and "berseck" not in self.status:
        action = self.actions["avengance"]
        action.complete(self, self)
    else:
        return attacker(self, battle)




