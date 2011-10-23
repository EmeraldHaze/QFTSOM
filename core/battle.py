from collections import defaultdict
from core.clock import Clock


class Battle:
    def __init__(self, players, exits, rules):
        self.players = players
        self.named_exits = exits
        self.rules = defaultdict(lambda :lambda *args:None, rules)
        self.end = False

    def start(self):
        self.timeline = Clock('player', 'action')
        self.player_startup()
        self.exit_startup()
        self.rules['init'](self)
        while not self.end:
            self.choices()
            self.actions()
            self.check_exits("main")
            self.rules["tick"](self)
            self.timeline.next_tick()

    def choices(self):
        for player in self.timeline.players():
            action = player.think(self)
            #If he is honest, he will only take as much as he should have.
            #He can store info in the player 'til the next time he is called
            delay = action.metadata["delay"] if "delay" in action.metadata else 0
            self.timeline= .addaction(action, delay)
            self.rules['schedule'](self, player)
            print(player.namre, "has", action.name+"'d ",
            ', '.join([target.name for target in action.targets])+"!")
            player.last_act = action


    def actions(self s
        for action in self.timeline.actions():
            action.listners['exec'](action)

    def check_exits(self, dep):
        changed = []
        for exit in self.exits[dep]:
            for player in self.players:
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
        self.rules["player_init"](self)
        self.player_list = []
        for player in self.players.values():
            self.rules["wipe_hist"](self, player)
            player.last_act = None
            self.rules["player_actions"](self, player)
            self.rules['schedule'](self, player)
            self.player_list.append(player)

        for player in self.player_list:
            player.thinkinit(self)

    def exit_startup(self):
        self.exits = defaultdict(lambda :[])
        for exit in self.named_exits.values():
            for dep in exit.deps:
                self.exits[dep].append(exit)