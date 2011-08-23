"""Starts the game, and defines highlevel noderunning"""
from core import battle, haggle

from data import battle_mods, glob_acts, beings, exits
from data.nodemap import nodemap


###Start node actions
def do_say(string):
    """do_ node executer print function"""
    print string

def do_battle(arg):
    """Start a battle- arg should be player1, player2|exit1, exit2|mod1, mod2"""
    players, game_exits, mods = arg.split("|")
    players = [getattr(beings, player) for player in players.split(", ")]
    game_exits = [getattr(exits, exit) for exit in game_exits.split(", ")]
    mods = [getattr(battle_mods, mod) for mod in mods.split(", ")]
    battle.start(players, game_exits, mods)
    
###Main function
def travel(nodemap):
    """Travles the nodemap. This is recursive and calls itself on any submaps"""
    nodename = nodemap.start
    node = nodemap[nodename]
    #Starting node in a network.
    
    while 1:
        for do in node.does:
            cmd, args = do.split(" ", 1)
            globals()["do_"+cmd](args)
        #Do all of the things the node wants done
        
        if node.net:
            nodename = travel(node)
            #If the node is actually a subnetwork, travel it.
            #It will return where the user exits, which will be the current node
            
        else:
            #If this node is an exit, return where it wants to exit too.
            #Unless this is the root network,
            #in which case exit_ will be a printed messege
            if node.exit_:
                return node.exit_
            
            ops = len(node.links)
            #Print all options
            for i in range(ops):
                print "("+str(i)+")", node.links[i]
            
            #Get valid option#############################################IO
            op = input(node.q+"\n")
            while not 0 <= op < ops:
                print "invalid answer"
                op = input(node.q+"\n")
                ##########################################################IO

            #Get node name
            nodename = node.names[op]
            
        node = nodemap[nodename]
        #Set the node




print travel(nodemap)
#Travel the root network
