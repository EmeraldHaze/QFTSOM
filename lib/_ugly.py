class Lib:
    def __init__(self, items = None):
        if items == None:
            items = {}
        self.items = dict(items)

    def __getattr__(self, item):
        return self.items[item]

    def __repr__(self):
        return repr(self.items)

def make(parts, groups):
    parts.update(groups)
    root = parts
    root = Lib(root)
    for name, sub in root.items.items():
        #Things like mana, rules, simple, thinkers
        for item in sub.values():
            #Things like mana.rule(s), simple.thinker(s)
            if item == dict:
                item = Lib(item)
        root.items[name] = Lib(sub)
    #Root becomes made of Libs
    return root