from collections import defaultdict#, OrderedDict
#from types import MethodType

from core.clock import Clock

import pdb

class Battle:
    def __init__(self, player_list, exit_list, rule_dict):
        self.player_list = player_list
        self.exit_list = exit_list
        self.rules = defaultdict(lambda :lambda *args:None, rule_dict)

    def start(self):
        self.timeline = Clock('player', 'effect')
        self.player_startup()
        self.exit_startup()
        self.rules['init'](self)
        self.end = False
        while not self.end:
            self.choices()
            self.effects()
            self.check_exits("main")
            self.timeline.next_tick()

    def choices(self):
        print("Making choices")
        for player in self.timeline.players():
            action = player.think(self)
            #If he is honest, he will only take as much as he should have.
            #He can store info in the player 'til the next time he is called
            print(player.name, "has", action.name+"'d ", ', '.join(action.targets)+"!")
            player.last_act = action
            self.do_action(action)
            ####Rescedule- Must be worked out. Important
            self.rules['schedule'](self, player)

    def do_action(self, action):
        for effect in action.effects:
            self.timeline.addeffect(effect, effect.tick)

    def effects(self):
        print('Applying effects')
        for effect in self.timeline.effects():
            for target in effect.targets:
                for change in list(effect.changes.items()):
                    self.players[target].stats[change[0]] += change[1]
                    print(target, "'s ", change[0], 'has changed by ', change[1])
            #For each change of each effect, apply the change to the target

    def check_exits(self, dep):
        changed = []
        for exit in self.exits[dep]:
            for player in list(self.players.keys()):
                    if exit.condition(self.players[player], self):
                        exit.effect(self.players[player], self)
                        changed.extend(exit.changes)
                        self.remove_player(player)
                        print(player," exited. Players:", len(self.players))
                        if not len(self.players):
                            self.end = True
        for change in changed:
            self.check_exits(change)

    def remove_player(self, player_name):
        player = self.players[player_name]
        split = self.timeline.player
        l = len(split)
        try:
            for i in range(self.timeline.tick, l):
                split[i] = [item for item in split[i] if item != player]
        except:
            pdb.set_trace()
        del self.players[player_name]

    def player_startup(self):
        self.players = {}#OrderedDict()
        for player in self.player_list:
            for belong in list(player.belongs.values()):
                for action in belong.actions:
                    player.actions.append(action.copy('action list generation'))
                    #Copy so that the original doesn't change

            self.rules['schedule'](self, player)

            self.players[player.name] = player

    def exit_startup(self):
        self.exits = defaultdict(lambda :[])
        for exit in self.exit_list:
            for dep in exit.deps:
                self.exits[dep].append(exit)