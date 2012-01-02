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
        #import pdb;pdb.set_trace()
        while not self.end:
            self.choices()
            self.actions()
            self.statuses()
            self.check_exits("main")
            self.rules["tick"](self)
            self.timeline.next_tick()

    def choices(self):
        for player in self.timeline.players():
            action = player.thinker()
            #If he is honest, he will only take as much as he should have.
            #He can store info in the player 'til the next time he is called
            delay = action.metadata["delay"] if "delay" in action.metadata else 0
            self.timeline.addaction(action, delay)
            player.last_act = action
            print(player.name, "has", action.name+"'d",
            ', '.join([target.name for target in action.targets])+"!")
            self.rules['schedule'](self, player)

    def actions(self):
        for action in self.timeline.actions():
            action.listners['exec'](action)

    def statuses(self):
        for player in self.player_list:
            for status in player.status_list:
                status()

    def check_exits(self, dep):
        changed = []
        for exit in self.exits[dep]:
            #All the exits dependant on this change
            for player in self.player_list:
                if exit.condition(player, self):
                    exit.effect(player, self)
                    changed.extend(exit.changes)
                    self.remove_player(player)
                    print(player.name," exited. Players:", len(self.players))
                    if not len(self.players):
                        self.end = True
        for change in changed:
            self.check_exits(change)

    def remove_player(self, player):
        split = self.timeline.player
        l = len(split)
        for i in range(self.timeline.tick, l):
            split[i] = [item for item in split[i] if item != player]
        del self.players[player.name]
        self.player_list.remove(player)

    def player_startup(self):
        self.rules["player_init"](self)
        self.player_list = []
        for player in self.players.values():
            self.rules["wipe_hist"](self, player)
            player.last_act = None
            self.rules["get_actions"](self, player)
            self.rules['schedule'](self, player)
            self.player_list.append(player)

        for player in self.player_list:
            player.thinker.init(self)

    def exit_startup(self):
        self.exits = defaultdict(lambda :[])
        for exit in self.named_exits.values():
            for dep in exit.deps:
                self.exits[dep].append(exit)