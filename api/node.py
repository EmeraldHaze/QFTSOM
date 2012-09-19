from collections import OrderedDict

from api import Abstract


class Node(Abstract):
    net = False


class AbstractNode(Node):
    """An abstract node used for conversations and other logical networks"""
    def __init__(self, name, links=[], does=[], exit_=False, data=None):
        self.name = name
        self.links = links
        self.does = does
        self.exit_ = exit_
        self.net = False


class Place(Node):
    """A node that represents a place"""
    def __init__(self, name, links, info, beings=None, items=None,
                 named_links=False):
        if items is None:
            items = []
        if type(items) is not list:
            items = [items]
        if beings is None:
            beings = []
        if type(beings) is not list:
            beings = [beings]
        self.name = name
        if named_links is False:
            named_links = links
        self.links = OrderedDict(zip(named_links, links))
        self.info = info
        self.items = items
        self.beings = beings
        self.parent = None


    def __repr__(self):
        return "<{} with {} in it>".format(
            self.name,
            ", ".join(map(repr, self.beings + self.items))
        )

    def alone(self):
        """
        Returns True if there's nobody in this place, the Being if
        their's one, and False if there's more than one
        """
        if len(self.beings) is 0:
            return True
        elif len(self.beings) is 1:
            return self.beings[0]
        else:
            return False

class Net(Abstract):
    net = True
    def __init__(self, name, nodes, does=[], start=None):
        """
        Start is the starting possision upon arival.
        Nodes are a dict of all nodes in this network.
        Do is node commands
        """
        self.name = name
        if type(nodes) is list:
            node_dict = OrderedDict()
            for node in nodes:
                node_dict[node.name] = node
            nodes = node_dict
        self.nodes = nodes
        for node in nodes.values():
            self.addnode(node)
        self.does = does
        self.start = start

    def addnode(self, node):
        if node.net:
            newnodes = OrderedDict(back=self)
            #this causes the 'back' to be the 'first' node in that net
            newnodes.update(node.nodes)
            node.nodes = newnodes
        else:
            links = OrderedDict()
            for name, link in node.links.items():
                links[name] = self.nodes[link]
            node.links = links
        self.nodes[node.name] = node


class PlaceNet(Net):
    """A network of Places"""


class AbstractNet(Net):
    """A network of AbstractNodes"""
    def walk(self, chooser):
        """
        Walk the network until you reach a node/state marked as end, which
        is returned
        """
        state = self.start
        if not state:
            state = chooser(self.nodes)
        while state:
            for do in state.does:
                do(state)
            if state.net:
                return state.walk(chooser)
            else:
                if state.exit_:
                    return state
                else:
                    try:
                        state = chooser(state.links, query=state.name)
                    except TypeError:
                        #no query argument
                        state = chooser(state.links)
