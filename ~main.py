#!/usr/bin/python3
"""
Starts the game.
"""
PRELOAD_IMPORTS = False

import sys, struct, pdb
import game
from core import shared

if PRELOAD_IMPORTS:
    import core, lib


class Wrap:
    """
    This class wraps a FD for buffer flushing and [eventually] prefixing
    messages with there lengths
    """
    def __init__(self, fd):
        self.fd = fd

    def write(self, data):
        #data = struct.pack('!H', len(data)).decode() + '\x00' + data
        self.fd.write(data)
        self.fd.flush()

    def __getattr__(self, item):
        return getattr(self.fd, item)


sys.stdout = Wrap(sys.stdout)

print("This is QFTSOM 0.2. In lieu of a proper interface, use the numbers. "
      " Failure to do so can cause crashs.")

#shared.name = input()
#Sets player name, which is the first input if run by Socket'd

if __name__ == "__main__":
    print(game.nodemap.travel())
