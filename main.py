#!/usr/bin/python3
"""
Starts the game.
"""
from sys import stdout, stdin, stderr

class Wrap:
    def __init__(self, f):
        self.f = f
    def write(self, data):
        self.f.write(data)
        self.f.flush()
    def __getattr__(self, item):
        return getattr(self.f, item)

stdout = Wrap(stdout)
stdin = Wrap(stdin)
stderr = open("/home/glycan/LOG", 'w', 2)

PRELOAD_IMPORTS = False
import pdb
if PRELOAD_IMPORTS:
    import core, lib
import game

def run():
    print(game.nodemap.travel())
if __name__ == "__main__":
    print(game.nodemap.travel())
