from collections import defaultdict as _defaultdict
__all__ = ['simple', 'mana']#"statuses", "mardek", "basic", "misc"]

class Lib:
    def __init__(self, items = None):
        if items == None:
            items = {}
        self.items = items
    def __getattr__(self, item):
        return self.items[item]
    def __repr__(self):
        return self.items

def _get_componants(modules):
    comps = []
    for module in modules:
        exec("from lib import "+module+" as m", globals())
        for comp_name in dir(m):
            if comp_name[0] != "_":
                comp = getattr(m, comp_name)
                comp.func = comp_name.split("_")[0] #Ex thinker, rule
                comp.group = module #Ex mana, limbs
                comps.append(comp)
    return comps

def _build_libs(comps):
    func = _defaultdict(lambda :Lib())
    group = _defaultdict(lambda :Lib())
    for comp in comps:
        group[comp.group].items[comp.func] = comp
        func[comp.func].items[comp.group] = comp
    return dict(func), dict(group)

_comps = _get_componants(__all__)

for item in  _build_libs(_comps):
    globals().update(item)
