#!/usr/bin/python3
"""
Starts the game, and defines highlevel noderunning

Imports
Node actions
Main
"""
###Imports###
from core import battle, haggle
import lib, game

import pdb

###Node actions###
def do_say(string):
    """do_ node executer print function"""
    print(string)


def do_battle(arg):
    """Start a battle- arg should be formatted like this:
    player1, player2, etc|exit1, exit2, etc|rule1, rule2, etc"""
    #Make lists of the actual objects named in the arg
    args = map(parsearg, arg.split("|"), game.defaults.battle)

    b = battle.Battle(*arg)
    b.start()

def parsearg(arg, default = {}):
    parsed = {}
    for part in arg.split(", "):
        if ":" in part:
            name, part = part.split(":")
            part = eval(part)
        else:
            part = eval(part)
            name = part.name
        parsed[name] = parsed
    default.update = parsed
    return default

###Main###
def travel(nodemap):
    """Travles the nodemap. Is recursive and calls itself on any submaps"""
    nodename = nodemap.start
    node = nodemap[nodename]
    #Starting node in a network.

    while 1:
        for do in node.does:
            cmd, args = do.split(" ", 1)
            globals()["do_" + cmd](args)


        if node.net:
            nodename = travel(node)
            #If the node is actually a subnetwork, travel it.
            #It will return where the user exits

        else:
            #If this node is an exit, return where it wants to exit too.
            #Unless this is the root network,
            #in which case exit_ will be printed
            if node.exit_:
                return node.exit_

            for i in range(len(node.links)):
                print("(" + str(i) + ")", node.links[i])

            #Get valid option
            op = eval(input(node.q + "\n"))
            while not 0 <= op < len(node.links):
                print("invalid answer")
                op = eval(input(node.q + "\n"))

            nodename = node.names[op]

        node = nodemap[nodename]
        #Set the node

if __name__ == "__main__":
    print(travel(game.nodemap))
    #Travel the root network
