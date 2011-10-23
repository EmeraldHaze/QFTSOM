class Node:
    def __init__(self, names, links, does=[], q="Where do you want to go?", exit_=False):
        self.links = links
        self.names = names
        self.does = does
        self.exit_ = exit_
        self.q = q
        self.net = False


class Net:
    def __init__(self, start, nodes, does=[]):
        """Nodes are a dict of all nodes in this network.
           Start is the starting possision upon arival.
           Do is node commands"""
        self.nodes = nodes
        self.start = start
        self.does = does
        self.net = True

    def __getitem__(self, item):
        return self.nodes[item]

    def travel(self):
        """Travles the nodemap. Is recursive and calls itself on any submaps"""
        from core import does
        name = startname = self.start
        node = startnode = self[startname]
        while 1:
            for do in node.does:
                cmd, args = do.split(" ", 1) #That's one split
                getattr(does, cmd)(args)
                #Get the do function from the does module
            if node.net:
                #If it is a net
                nodename = node.travel()
            else:
                #If this node is an exit, return where it wants to exit too.
                if node.exit_:
                    return node.exit_
                for i, v in enumerate(node.links):
                    print("{}: {}").format(i, v)
                op = int(input(node.q1 + "\n"))
                while not 0 <= op < len(node.links):
                    print("invalid answer")
                    op = int(input(node.q + "\n"))                    
                nodename = node.names[op] 
            node = nodemap[nodename]
            #Set the node
