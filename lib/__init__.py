from collections import defaultdict as dd
__all__ = ['simple']#"statuses", "mardek", "basic", "misc"]

class Lib:
    def __getattr__(self, item):
        return self.items[item]
    def __init__(self, items = {}):
        self.items = items

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
                comp.sys = module #Ex mana, limbs
    return comps

def _build_libs(comps):
    func = dd(lambda :Lib())
    sys = dd(lambda :Lib())
    for comp in comps:
        sys[comp.sys].items[comp.func] = comp
        func[comp.func].items[comp.sys] = func
    return dict(sys.items() + sys.items())

locals().update(_build_libs(get_componants(__all__)))