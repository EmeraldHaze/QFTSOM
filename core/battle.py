from collections import defaultdict, OrderedDict


from core.clock import Clock

import pdb

class Battle:
    def __init__(self, player_list, exit_list, rule_dict):
        self.player_list = player_list
        self.exit_list = exit_list
        self.rules = defaultdict(lambda :lambda *args:None, rule_dict)

    def start(self):
        self.timeline = Clock('player', 'action')
        self.player_startup()
        self.exit_startup()
        self.rules['init'](self)
        self.end = False
        while not self.end:
            self.choices()
            self.actions()
            self.check_exits("main")
            self.timeline.next_tick()

    def choices(self):
        for player in self.timeline.players():
            action = player.think(self)
            #If he is honest, he will only take as much as he should have.
            #He can store info in the player 'til the next time he is called
            print(player.name, "has", action.name+"'d ",
             ', '.join([target.name for target in action.targets])+"!")
            player.last_act = action
            self.timeline.addaction(action, action.metadata["delay"])
            self.rules['schedule'](self, player)

    def actions(self):
        for action in self.timeline.actions():
            action.listners['exec'](action)

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
        for i in range(self.timeline.tick, l):
            split[i] = [item for item in split[i] if item != player]

        del self.players[player_name]
        self.player_list.remove(player)
        del player

    def player_startup(self):
        self.players = OrderedDict()
        for player in self.player_list:
            for belong in list(player.belongs.values()):
                for action in belong.actions:
                    player.actions.append(action.copy(battle = self))
                    #Copy so that the original doesn't change

            player.last_act = None

            self.rules['schedule'](self, player)

            self.players[player.name] = player
        for player in self.player_list:
            player.thinkinit(self)

    def exit_startup(self):
        self.exits = defaultdict(lambda :[])
        for exit in self.exit_list:
            for dep in exit.deps:
                self.exits[dep].append(exit)