class Action:
    def __init__(self, name,  *args):
        """Each arg is a tuple of changes, delay = 0, trigs = []"""
        self.name = name
        self.effects = []
        for effect_data in args:
            self.effects.append(effect(effect_data))
            #For each effect given, add it to our effects as an effect object.
        
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
        
    def poptrig(self):
        return self.trigs.pop()
    
