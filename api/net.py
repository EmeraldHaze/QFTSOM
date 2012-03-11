from api import Abstract

class Node(Abstract):
    """
    args: names, links, does, q, exit_
    links: names of nodes the user can go to from here.
    names: Display names of said links. links[0]'s name should be names[0].
    does:  commands to be done on this node; see does.py for more info.
    q: Query when asking for choice
    exit_: If set, exits the player to a higher network as named.
    """
    def __init__(self, names, links,
            does={}, q="Where do you want to go?", exit_=False):
        self.names = names
        self.links = links
        self.does = does
        self.exit_ = exit_
        self.q = q
        self.net = False


class Net(Abstract):
    def __init__(self, start, nodes, does=[]):
        """
        Start is the starting possision upon arival.
        Nodes are a dict of all nodes in this network.
        Do is node commands
        """
        self.nodes = nodes
        self.start = start
        self.does = does
        self.net = True

    def __getitem__(self, item):
        return self.nodes[item]

    def travel(self):
        "Travles the nodemap. Is recursive and calls itself on any submaps"
        from core import does
        name = startname = self.start
        node = startnode = self[startname]
        while 1:
            ###Does###
            if type(node.does) is dict:
                node.does = node.does.items()
            sendto = None
            for do, args in node.does:
                if type(do) is str:
                    do = getattr(does, do)
                result = do(args)
                if result:
                    sendto = result
            ###nodename selection###
            if node.net:
                #If it is a net
                nodename = node.travel()
            elif sendto:
                nodename = sendto
            else:
                #If this node is an exit, return where it wants to exit too.
                if node.exit_:
                    return node.exit_
                for i, v in enumerate(node.links):
                    print("{}: {}".format(i + 1, v))
                while 1:
                    try:
                        nodename = node.names[int(input(node.q + "  ")) - 1]
                        break
                    except (ValueError, IndexError):
                        print("Bad answer! User a number in range")
            node = self[nodename]
            #Set the node
