from collections import defaultdict
from api.clock import Clock
import pdb
class Battle:
    def __init__(self, player_list, exit_list, mod_list):
        self.player_list = player_list
        self.exit_list = exit_list
        self.mod_list = mod_list

    def start(self):
        self.trigs = {}
        #trigs is the trigger stack. It will be used by do_action.
        self.timeline = Clock('player', 'effect')
        self.player_startup()
        self.exit_startup()
        self.end = False
        while not self.end:
            self.choices()
            self.effects()
            self.check_exits("main")
            self.timeline.next_tick()

    def choices(self):
        print "Making choices"
        for player in self.timeline.players():
            action = player.think(self)
            #If he is honest, he will only take as much as he should have.
            #He can store info in the player 'til the next time he is called
            print player.name, "has", action.name, "'d ", ', '.join(action.targets), "!"
            self.do_action(action)
            ####Rescedule- Must be worked out. Important
            self.timeline.addplayer(player, 1)

    def effects(self):
        print 'Applying effects'
        for effect in self.timeline.effects():
            for target in effect.targets:
                for change in effect.changes.items():
                    self.players[target].stats[change[0]] += change[1]
                    print target, "'s ", change[0], 'has changed by ', change[1]
            #For each change of each effect, apply the change to the target

    def do_action(self, action):
        for effect in action.effects:
            self.timeline.addeffect(effect, effect.tick)

    def check_exits(self, dep):
        changed = []
        for exit in self.exits[dep]:
            for player in self.players.keys():
                    if exit.condition(self.players[player], self.players):
                        exit.effect(self.players[player], self.players)
                        changed.extend(exit.changes)
                        del self.players[player]
                        print player," exited. Players:", len(self.players)
                        if not len(self.players):
                            self.end = True
        for change in changed:
            self.check_exits(change)

    def player_startup(self):
        self.players = {}
        for player in self.player_list:
            for belong in player.belongs.values():
                for action in belong.actions:
                    player.actions.append(action.copy('action list generation'))
                    #Copy so that the original doesn't change

            #Make this into a data function, shouldn't be part of core
            self.timeline.addplayer(player, 0)

            self.players[player.name] = player
        print self.players
    def exit_startup(self):
        self.exits = defaultdict(lambda :[])
        for exit in self.exit_list:
            for dep in exit.deps:
                self.exits[dep].append(exit)