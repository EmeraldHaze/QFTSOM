"""
Starts the game, and defines highlevel noderunning

Imports
Node actions
Main
"""
###Imports###
from core import battle, haggle

from data import battle_mods, glob_acts, beings, exits
from data.nodemap import nodemap

###Node actions###
def do_say(string):
    """do_ node executer print function"""
    print string


def do_battle(arg):
    """Start a battle- arg should be formatted like this:
    player1, player2, etc|exit1, exit2, etc|battlemod1, battlemod2, etc"""
    #Make lists of the actual objects named in the arg
    player_names, exit_names, mod_names = arg.split("|")
    player_list = [getattr(beings, player) for player in player_names.split(", ")]
    exit_list = [getattr(exits, exit) for exit in exit_names.split(", ")]
    mod_list = [getattr(battle_mods, mod) for mod in mod_names.split(", ")]
    b = battle.Battle(player_list, exit_list, mod_list)
    b.start()


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
                print "(" + str(i) + ")", node.links[i]

            #Get valid option
            op = input(node.q + "\n")
            while not 0 <= op < len(node.links):
                print "invalid answer"
                op = input(node.q + "\n")

            nodename = node.names[op]

        node = nodemap[nodename]
        #Set the node


print travel(nodemap)
#Travel the root network
