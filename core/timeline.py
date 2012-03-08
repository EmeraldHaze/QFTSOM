from collections import deque
from core.config import info, at, debug


class Timeline:
    """A timeline with a number of types of slot (lines) for each tick, and a
    pointer (E.g. each tick has a number of named list
    clock.add<listname>(item, time) sceduals item time ticks away from now
    clock.<listname>s() returns the list of items scedualed for this tick
    """

    def __init__(self, *args):
        self.tick = 0
        self.lines = {}
        for line in args:
            self.lines[line] = deque([[]])

    def __getattr__(self, attr):
        if attr.startswith("add"):
            return lambda item, tick: self._add(attr[3:], item, tick)
            #Return a wrapper for the correct line add
        elif attr.endswith("s"):
            return lambda: self._get(attr[:-1])
        else:
            return self.lines[attr]

    def _add(self, linename, item, offset):
        target_tick = self.tick + offset
        line = self.lines[linename]
        self.pad(line, target_tick)
        line[target_tick].append(item)
        debug("_add:", linename, target_tick, item)

    def _get(self, line):
        return self.lines[line][self.tick]

    def pad(self, line, newlength):
        for i in range(newlength - self.tick + 1):
            line.append([])

    def next_tick(self):
        """
        Moves the tick counter forward by one and pads all lines
        """
        self.tick += 1
        for line in self.lines.values():
            self.pad(line, self.tick)

    def __repr__(self):
        return "<Clock instance tick {tick} lines {lines}".format(
            tick=self.tick,
            lines=list(self.lines.keys())
            )
