from core import battle, haggle

from content import battle_mods, glob_acts, people, meta
from content.nodemap import nodemap


###Start node actions
def do_say(s): print s


###Main function
def travel(nodemap):
    nodename = nodemap.start
    node = nodemap[nodename]
    while 1:
        for do in node.does:
            cmd, args = do.split(" ", 1)
            globals()["do_"+cmd](args)

        
        if node.net:
            nodename = travel(node)
            
        else:
            #Check for exit
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
            
print travel(nodemap)
   
