class action:
    def __init__(self, (effect, delay = 0, trigs = None)):
        self.effect = effect
        self.tick = delay
        if trigs is not None: trigs.reverse()
        #Reverse it si that pop works fast, unless it's none
        
        self.trigs = trigs
        
    def poptrig(self):
        return self.trigs.pop()
