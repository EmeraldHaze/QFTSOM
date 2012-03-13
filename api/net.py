from api import Abstract
from core import does


class Node(Abstract):
    """
    args: names, links, does, q, exit_
    links: names of nodes the user can go to from here.
    names: Display names of said links. links[0]'s name should be names[0].
    does:  commands to be done on this node; see does.py for more info.
    q: Query when asking for choice
    exit_: If set, exits the player to a higher network as named.
    """
    net = False
    def __init__(self, names, links,
            does={}, q="Where do you want to go?", exit_=False, name=None):
        self.names = names
        self.links = links
        self.does = does
        self.exit_ = exit_
        self.q = q
        self.net = False


class AbstractNode(Node):
    """An abstract node used for conversations and other logical networks"""


class Place(Node):
    """A node that represents a place"""
    def __init__(self, name, linked, info, beings=None, items=None):
        if items is None:
            items = []
        if type(items) is not list:
            items = [items]
        if beings is None:
            beings = []
        if type(beings) is not list:
            beings = [beings]
        self.name = name
        self.linked = linked
        self.info = info
        self.items = items
        self.beings = beings

    def __repr__(self):
        return "<{} with {} in it>".format(
            self.name,
            ", ".join(map(repr, self.beings + self.items))
        )


class Net(Abstract):
    net = True
    def __init__(self, nodes):
        """
        Start is the starting possision upon arival.
        Nodes are a dict of all nodes in this network.
        Do is node commands
        """
        if type(nodes) is list:
            nodes = {node.name: node for node in nodes}
        self.nodes = nodes
        for node in nodes.values():
            node.parent = self

    def __getitem__(self, item):
        return self.nodes[item]


class PlaceNet(Net):
    """A network of Places"""


class AbstractNet(Net):
    """A network of AbstractNodes"""
