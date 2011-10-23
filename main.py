#!/usr/bin/python3
"""
Starts the game.
"""
PRELOAD_IMPORTS = True

if PRELOAD_IMPORTS:
	import core, lib
import game, pdb

def run():
    print(game.nodemap.travel())

if __name__ == "__main__":
    print(game.nodemap.travel())
