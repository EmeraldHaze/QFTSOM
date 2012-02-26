#!/usr/bin/python3
"""
Starts the game.
"""

NAME = False
DEBUG = 2
{
    0: "no debug",
    1: "show parts",
    2: "heavy debug",
    3: "pdb"
}

import sys, struct, pdb
import game

from core import shared

if DEBUG == 3:
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

    sys.stdout = Wrap(sys.stdout)

    print("This is QFTSOM 0.3. In lieu of a proper interface, use the numbers. "
          " Failure to do so can cause crashs.")

    if NAME:
        shared.name = input()
        #Sets player name, which is the first input if run by Socket'd

    print(game.nodemap.travel())
