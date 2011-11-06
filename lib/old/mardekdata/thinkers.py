"""
Old thinkers files
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
        print("{i}: {name}".format(i = i, name = possib_acts[i].name))
    target = int(input('Target? '))
    action = int(input('Action? '))
    action = possib_acts[action].copy(battle)
    action.complete(self, people[target])
    return action

def healer(self, battle):
    wounded = [ally for ally in battle.player_list if ally.data["team"] == self.data["team"] and ally.stats["HP"]/ally.stats["MAXHP"] < 0.9]
    if len(wounded):
        action = self.act_dict["cure"]
        action.complete(self, wounded[0])
    else:
        action = choice(["shield", "m. shield", "regen"])
        targets = [ally for ally in battle.player_list if ally.data["team"] == self.data["team"] and action not in ally.statuses]
        while not targets:
            print("Remaking choice")
            action = choice(["shield", "m. shield", "regen"])
            targets = [ally for ally in battle.player_list if ally.data["team"] == self.data["team"] and action not in ally.statuses]
        action = self.act_dict[action]
        action.complete(self, choice(targets))
    return action

def attacker(self, battle):
    action = choice(self.actions)
    if action.metadata["target"] == "norm":
        action.complete(self, choice([enemy for enemy in battle.player_list if enemy.data["team"] != self.data["team"]]))
    else:
        action.complete(self, battle.teams["mar"])
    return action

def bart(self, battle):
    if len(battle.teams[self.data["team"]]) == 1 and "berseck" not in self.status:
        action = self.actions["avengance"]
        action.complete(self, self)
    else:
        return attacker(self, battle)