from collections import OrderedDict

from api import Abstract
from core import does


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
    def __init__(self, name, links, info, beings=None, items=None):
        if items is None:
            items = []
        if type(items) is not list:
            items = [items]
        if beings is None:
            beings = []
        if type(beings) is not list:
            beings = [beings]
        self.name = name
        self.links = links
        self.info = info
        self.items = items
        self.beings = beings
        self.parent = None

    def __repr__(self):
        return "<{} with {} in it>".format(
            self.name,
            ", ".join(map(repr, self.beings + self.items))
        )


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
            node.parent = self
            if node.net:
                newnodes = OrderedDict(back=self)
                newnodes.update(node.nodes)
                #This causes the back to be the 'first' node in that net
                node.nodes = newnodes
            else:
                links = []
                for link in node.links:
                    links.append(self.nodes[link])
                node.links = links
        self.does = does
        self.start = start


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
                    state = chooser(state.links)
