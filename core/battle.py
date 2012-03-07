from collections import defaultdict
from core.timeline import Timeline
from core.config import info, at, debug

class Battle:
    """
    Represents a battle. Call start() to start it.
    """
    def __init__(self, beings, exits, rules):
        """
        These fallowing arguments should be dicts of {name: appropriate object}
        beings: who is in the battle.
        exits: ways to exit the battle
        rules: ways to do things such as scheduling
        """
        self.end = False
        self.beings = beings
        self.named_exits = exits
        self.rules = defaultdict(lambda : lambda *args: None, rules)
        #That's a lambda which takes no arguments and returns a lambda which
        #take any arguments and retunrs None

    def start(self):
        at("start")
        self.timeline = Timeline('being', 'action')
        self.being_startup()
        self.exit_startup()
        self.rules['init'](self)
        while not self.end:
            at("tick " + str(self.timeline.tick))
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
        at("choises")
        for being in self.timeline.beings():
            action = being.thinker()
            #Thinkers should return ActionInsts
            try:
                delay = action.data["delay"]
            except KeyError:
                delay = 0
            self.timeline.addaction(action, delay)
            action.listeners["choosen"](action)
            being.last_act = action
            self.rules['schedule'](self, being)

    def actions(self):
        """
        Executes every action
        """
        at("actions")
        for action in self.timeline.actions():
            info(action)
            action.listeners['exec'](action)

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
                    #refered to by self.timeline.being[tick], this changes the timeline
                except ValueError:
                    pass
                    #the being is not scheduled for this tick
        del self.beings[being.name]
        self.being_list.remove(being)

    def being_startup(self):
        self.rules["being_init"](self)
        self.being_list = []
        for being in self.beings.values():
            self.rules["wipe_hist"](self, being)
            being.last_act = None
            self.rules["get_actions"](self, being)
            self.rules['schedule'](self, being)
            self.being_list.append(being)
            being.thinker.init(self)

    def exit_startup(self):
        """
        Builds a dict, {dep: [exits]}
        """
        self.exits = defaultdict(lambda : [])
        for exit in self.named_exits.values():
            for dep in exit.deps:
                self.exits[dep].append(exit)
