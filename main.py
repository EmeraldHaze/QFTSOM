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
import pdb
if PRELOAD_IMPORTS:
    import core, lib
import game
print("This is QFTSOM 0.2")
def run():
    print(game.nodemap.travel())
if __name__ == "__main__":
    print(game.nodemap.travel())
