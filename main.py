#!/usr/bin/python3
"""
Starts the game.
"""
class Wrap:
    def __init__(self, f):
        self.f = f

    def write(self, data):
        #data = struct.pack('!H', len(data)).decode() + '\x00' + data
        self.f.write(data)
        self.f.flush()

    def __getattr__(self, item):
        return getattr(self.f, item)


import sys, struct
sys.stdout = Wrap(sys.stdout)

PRELOAD_IMPORTS = False

print("This is QFTSOM 0.2. In lieu of a proper interface, use the numbers. Failure to do so can cause crashs.")

import pdb
if PRELOAD_IMPORTS:
    import core, lib

from core import shared
#shared.name = input()

import game


def run():
    print(game.nodemap.travel())
if __name__ == "__main__":
    print(game.nodemap.travel())
