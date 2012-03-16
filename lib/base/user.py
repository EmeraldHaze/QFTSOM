from api import Thinker
from api import AbstractNode as Node, AbstractNet as Net
from lib.base.thinkers import pchoice

def upfold(l, maker=None):
    if maker is None:
        maker = lambda i: Node(i, exit_=True)
    def unfolder(net):
        for i in l:
            node = maker(i)
            net.nodes[node.name] = node
    return unfolder


@Thinker
def tree_user(self):
    option_tree = Net('Choices', [
        Node("Move", exit_=True),
    ], [unfold_act_types
    ])
    choice = option_tree.walk(pchoice)
    print(choice)

pthinker = tree_user

@api.Thinker
def smart_user(self):
    act_type = thinkers.pchoice(list(self.typed_acts.keys()))
    action = thinkers.pchoice(self.typed_acts[act_type])
    args = {}
    arg_queries = {}
    if "arg_queries" in action.data:
        arg_queries = action.data["arg_queries"]
    for arg, info in action.argsinfo:
        try:
            query = arg_queries[arg]
        except KeyError:
            query = "Choice? "
        if arg is "targets":
            value = thinkers.pchoice(
                eval(info),
                ("HP", "choice.stats['HP']"),
                query=query
            )
        else:
            value = thinkers.pchoice(eval(info), query=query)
        args[arg] = value
    return action.instance(**args)
