from collections import defaultdict
__all__ = ['simple']#"statuses", "mardek", "basic", "misc"]

#class Lib:
#    def __init__(self, items = None):
#        if items == None:
#            items = {}
#        self.items = items
#    def __getattr__(self, item):
#        return self.items[item]

def get_componants(modules):
    comps = []
    for module in modules:
        n = "lib."+module
        print(n)
        m = __import__(n)
        for comp_name in dir(m):
            if comp_name[0] != "_":
                comp = getattr(m, comp_name)
                print(comp)
                comp.func = comp_name.split("_")[0] #Ex thinker, rule
                comp.group = module #Ex mana, limbs
    return comps

def _build_libs(comps):
    func = defaultdict(lambda :{})
    group = defaultdict(lambda :{})
    for comp in comps:
        group[comp.group].items[comp.func] = comp
        group[comp.func].items[comp.group] = func
    return func, group

func, group = _build_libs(get_componants(__all__))