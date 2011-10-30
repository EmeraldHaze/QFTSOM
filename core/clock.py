from collections import deque
class Clock:
    """A timeline with a number of types of slot for each tick, and a pointer
    (E.g. each tick has a number of named list
    clock.add<listname>(item, time) sceduals item time ticks away from now
    clock.<listname>s() returns the list of items scedualed for this tick
    """

    def __init__(self, *args):
        self.tick = 0
        self.splits = {}
        for split in args:
            self.splits[split] = deque([[]])

    def __getattr__(self, attr):
        if attr[:3] == "add":
            return lambda item, tick: self.add(attr[3:], item, tick)
            #Return a wrapper for the correct split add

        elif attr[-1] == 's':
            return lambda : self.get(attr[:-1])

        else:
            return self.splits[attr]

    def add(self, split, item, tick):
        tick += self.tick
        s = split
        split = self.splits[split]
        l = len(split) - 1
        #This accounts for the current tick
        if l < tick + 1:
            #If the target tick is beyond our scope...
            for i in range(tick - l + 2):
                split.append([])
            #Extend just enough for it to be within our scope + 2
            #The incremnt is so that we don't crash when people stop scedualing
        split[tick].append(item)

    def get(self, split):
        return self.splits[split][self.tick]

    def next_tick(self):
        self.tick += 1

    def __repr__(self):
        return "<Clock instance tick {tick} splits {splits}".format(tick = self.tick, splits = list(self.splits.keys()))
