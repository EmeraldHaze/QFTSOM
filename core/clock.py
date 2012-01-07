from collections import deque


class Clock:
    """A timeline with a number of types of slot (splits) for each tick, and a
    pointer (E.g. each tick has a number of named list
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
            return lambda item, tick: self._add(attr[3:], item, tick)
            #Return a wrapper for the correct split add

        elif attr[-1] == 's':
            return lambda: self._get(attr[:-1])

        else:
            return self.splits[attr]

    def _add(self, split, item, tick):
        tick += self.tick
        s = split
        split = self.splits[split]
        l = len(split) - 1
        #This accounts for the current tick
        if l < tick + 1:
            self.pad(split, tick)
        split[tick].append(item)

    def _get(self, split):
        return self.splits[split][self.tick]

    def pad(self, split, newlength):
        for i in range(newlength - self.tick + 1):
            split.append([])

    def next_tick(self):
        """
        Moves the tick counter forward by one and pads all splits
        """
        self.tick += 1
        for split in self.splits.values():
            self.pad(split, self.tick)

    def __repr__(self):
        return "<Clock instance tick {tick} splits {splits}".format(
            tick=self.tick,
            splits = list(self.splits.keys())
            )
