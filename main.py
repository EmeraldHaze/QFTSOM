from core import battle, haggle

from data import battle_mods, glob_acts, beings
from data.nodemap import nodemap


###Start node actions
def do_say(s): print s

def do_battle(arg):
    persons, exits, mods = arg.split(" | ")
    persons = [getattr(people, person) for person in persons.split(", ")]
    exits = [getattr(battle_mods, exit) for exit in exit.split(", ")]
    mods = [getattr(battle_mods, mod) for mod in mods.split(", ")]
    battle.start(persons, exits, mods)
    
###Main function
def travel(nodemap):
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
            #Unless this is the root network, in which case it's a message to be printed
            if node.exit_: return node.exit_
            
            ops = len(node.links)
            #Print all options
            for i in range(ops):print "("+str(i)+")",node.links[i]
            
            #Get valid option#############################################IO
            op = input(node.q+"\n")
            while not 0<=op<ops:
                print "invalid answer"
                op = input(node.q+"\n")
                ##########################################################IO

            #Get node name
            nodename = node.names[op]
            
        node = nodemap[nodename]
        #Set the node




print travel(nodemap)
#Travel the root network
