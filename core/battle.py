from collections import defaultdict
from core.clock import Clock


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
        self.timeline = Clock('being', 'action')
        self.being_startup()
        self.exit_startup()
        self.rules['init'](self)
        while not self.end:
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
        for being in self.timeline.beings():
            action = being.thinker()
            #Thinkers should return ActionInsts
            delay = action.data["delay"] if "delay" in action.metadata else 0
            self.timeline.addaction(action, delay)
            print(being.name, "has", action.name + "'d",
            ', '.join([target.name for target in action.targets]) + "!")

            being.last_act = action
            self.rules['schedule'](self, being)

    def actions(self):
        """
        Executes every action
        """
        for action in self.timeline.actions():
            action.listners['exec'](action)

    def statuses(self):
        """
        Executes every status
        """
        for being in self.being_list:
            for status in being.status_list:
                status()

    def check_exits(self, dep):
        """
        Checks if any of the exits dependant on dep trigger, and cleans up
        after him (remove, recursivly call deps)
        """
        for exit in self.exits[dep]:
            #Loops through all the exits dependant on this change
            for being in self.being_list:
                if exit.condition(being, self):
                    exit.effect(being, self)
                    for change in exit.changes:
                        self.check_exits(change)
                    self.remove_being(being)
                    print(being.name, "exited. beings:", len(self.beings))
                    if self.beings is []:
                        self.end = True

    def remove_being(self, being):
        for index, tick in enumerate(self.timeline.being[self.timeline.tick:]):
            #Loops over all turns in the future
            split[i] = [item for item in split[i] if item != being]
            #Removes the departed being from this tick
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
