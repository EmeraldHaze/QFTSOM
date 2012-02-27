#!/usr/bin/python3
"""
Starts the game.
"""

from pdb import pm
import sys, struct

import game
from core import shared, config

if config.DEBUG >= 3:
    pdb.set_trace()

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


if __name__ == "__main__":
    sys.setrecursionlimit(50)
    #prevents infinite recursive loops from wiping out original context
    sys.stdout = Wrap(sys.stdout)
    #ensures that output gets past wraping
    print(".")#Corrects a client bug
    print("This is QFTSOM 0.3. In lieu of a proper interface, use the numbers. "
          " Failure to do so can cause crashs.")

    if config.GET_NAME:
        shared.name = input()
        #Sets player name, which is the first input if run by Socket'd

    print(game.nodemap.travel())
