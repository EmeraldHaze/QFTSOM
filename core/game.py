from collections import defaultdict
from core.timeline import Timeline
from core.utils import info, at, debug


class Game:
    def __init__(self, placenet, rules, exits):
        """Initilizes the game"""
        at("game initilization")
        self.end = False
        self.placenet = placenet
        self.exit_list = exits
        self.rules = defaultdict(lambda *a: lambda *args: None, rules)
        self.timeline = Timeline('being', 'action')
        self.being_startup()
        self.exit_startup()
        self.rules['init'](self)

    def play(self):
        at("game play")
        while not self.end:
            print("Turn", self.timeline.tick)
            self.choices()
            self.actions()
            self.statuses()
            self.check_exits("main")
            self.rules["tick"](self)
            self.timeline.next_tick()

    def choices(self):
        """
        Queries every being for an action, and schedules it, with some cleanup
        """
        at("choices")
        for being in self.timeline.beings():
            action = being.thinker()
            #Thinkers should return ActionInsts
            if "delay" in action.data:
                delay = action.data["delay"]
            elif "speed" in action.data:
                delay = action.data["speed"]
            else:
                delay = 0
            self.timeline.addaction(action, delay)
            action.listeners["choosen"]()
            being.last_act = action
            self.rules['schedule'](self, being)
            action.listeners["init"]()

    def actions(self):
        """
        Executes every action
        """
        at("actions")
        for action in self.timeline.actions():
            info(action, "is execing")
            action.listeners['exec']()

    def statuses(self):
        """
        Executes every status
        """
        at("statuses")
        for being in self.being_list:
            for status in being.status_list:
                status()

    def check_exits(self, dep):
        """
        Checks if any of the exits dependant on dep trigger, and cleans up
        after him (remove, recursivly call deps)
        """
        at("check_exits")
        for exit in self.exits[dep]:
            #Loops through all the exits dependant on this change
            for being in self.being_list:
                if exit.condition(being, self):
                    info(exit.name, "triggered, changes:", exit.changes)
                    exit.effect(being, self)
                    self.remove_being(being)
                    for change in exit.changes:
                        info("checking", change)
                        self.check_exits(change)
                    if not len(self.beings):
                        #If the length has a False value (e.g, 0)
                        self.end = True
                    else:
                        print(len(self.beings), "beings left")

    def remove_being(self, being):
        at("remove_being")
        line = self.timeline.being
        for tick, beings in enumerate(line):
            #loops over all turns
            if tick > self.timeline.tick:
                #if it's in the future
                try:
                    beings.remove(being)
                    #since the identifier "beings" refers to the object also
                    #refered to by self.timeline.being[tick], this changes the
                    #timeline
                except ValueError:
                    pass
                    #the being is not scheduled for this tick
        del self.beings[being.name]
        self.being_list.remove(being)

    def being_startup(self):
        at("being startup")
        self.rules["being_init"](self)
        self.being_list = []
        self.beings = {}
        self.findbeings(self.placenet)

    def findbeings(self, net):
        at("find beings")
        for name, place in net.nodes.items():
            if name is not "parent":
                if place.net:
                    self.findbeings(place)
                else:
                    for being in place.beings:
                        self.rules["wipe_hist"](self, being)
                        being.last_act = None
                        being.location = place
                        self.rules["get_actions"](self, being)
                        self.rules['schedule'](self, being)
                        self.being_list.append(being)
                        self.beings[being.name] = being
                        being.thinker.init(self)

    def exit_startup(self):
        at("exit startup")
        """
        Builds a dict, {dep: [exits]}
        """
        self.exits = defaultdict(lambda *a: [])
        for exit in self.exit_list:
            for dep in exit.deps:
                self.exits[dep].append(exit)
