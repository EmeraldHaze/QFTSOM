#!/usr/bin/python3
"""
Starts the game.
"""

import sys
import struct
from pdb import pm
from core import shared, config


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
    print("This is QFTSOM 0.3. In lieu of a proper interface, use the numbers."
          " Failure to do so can cause crashs.")

    if config.GET_NAME:
        shared.name = input()
        #Sets player name, which is the first input if run by Socket'd
    else:
        shared.name = "Glycan"
    import api
    from game.nodemap import nodemap
    #if it was imported before, lib and compony would of loaded without the
    #changes we just made
    print(nodemap.travel())
