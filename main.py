#!/usr/bin/python3
"""
Starts the game.
"""
PRELOAD_IMPORTS = False
import pdb
if PRELOAD_IMPORTS:
    import core, lib
import game

def run():
    print(game.nodemap.travel())
if __name__ == "__main__":
    print(game.nodemap.travel())
