class Node:
    def __init__(self, names, links, does = [], q = "Where do you want to go?", exit_ = False):
        self.links = links
        self.names = names
        self.does = does
        self.exit_ = exit_
        self.q = q
        self.net = False

class Net:
    
    def __init__(self, start, nodes, does = []):
        """Nodes are a dict of all nodes in this network.
           Start is the starting possision upon arival.
           Do is node commands"""
        self.nodes = nodes
        self.start = start
        self.does = does
        self.net = True
        
    def __getitem__(self, item):
        return self.nodes[item]

