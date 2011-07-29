from core import battle, haggle

from content import battle_mods, glob_acts, people, meta
from nodemap import nodemap


###Start node actions
def do_say(s): print s


###Main function
def travel(nodemap):
    nodename = nodemap.start
    node = nodemap[nodename]
    while 1:
        for do in node.does:
            cmd, args = do.split(" ", 1)
            globals()[cmd](args)

        if node.exit_: return node.exit_
        
        if node.net:
            nodename = traval(node)
            
        else:
            ops = len(node.links)
            #Print all options
            for i in range(ops):print "(",i,")",node.links[i]
            
            #Get valid option
            op = input(node.q)
            while ops>op=>0:
                print "invalid answer"
                op = input(node.q)

            #Get node name
            nodename = node.names[op]

        node = nodemap[nodename]
            
travel(nodemap)
    
