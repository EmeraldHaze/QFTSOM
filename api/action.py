class Action:
    def __init__(self, name, *args):
        """Each arg is a tuple:
            (changes, delay = 0, trigs = [])"""
        self.name = name
        self.effects = []
        self.copy_status = 0
        for effect_data in args:
            self.effects.append(Effect(effect_data))
            #For each effect given, add it to our effects as an effect object.

    def copy(self, where):
        new = Action(self.name)
        new.effects = []
        for effect in self.effects:
            new.effects.append(effect.copy())
        new.copy_stats = self.copy_status + 1
        return new

    def complete(self, actor, targets):
        self.actor = actor
        if type(targets) == str:
            targets = [targets]
        self.targets = targets
        for effect in self.effects:
            effect.targets = targets
            effect.actor = actor


class Effect:
    def __init__(self, effect_data):
        l = len(effect_data)
        if type(effect_data) == dict:
            effect_data = [effect_data]
        #If it's one item, make it so you don't have to put []s youself.
        changes, tick, trigs = effect_data[0], 0, []
        #Set manditory and defaults
        if l > 1:
            tick = effect_data[1]
            if l > 2:
                trigs = effect_data[2]
                #Set optinal vars if they exist.
        self.changes = changes
        self.tick = tick
        self.trigs = trigs

    def __repr__(self):
        return  "<Effect instance target " + str(self.targets) + " changes " +\
         str(self.changes)+" from " + str(self.actor) + ">"

    def poptrig(self):
        return self.trigs.pop()

    def copy(self):
        new = Effect({})
        new.changes = self.changes
        new.tick = self.tick
        new.trigs = self.trigs
        return new
