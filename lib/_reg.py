from collections import defaultdict
import os
import importlib

def build_reg(modules):
    parts = defaultdict(lambda :{})
    groups = defaultdict(lambda :{})

    for module_name, module in modules.items():
        for comp_name in dir(module):
            if comp_name.startswith("reg_"):
                comp = getattr(module, comp_name)
                groups[module_name][comp_name] = comp
                parts[comp_name + "s"][module_name] = comp
    return dict(parts), dict(groups)

def get_modules(d):
    files = os.listdir("./" + "/".join(d))
    names = [fi[:-3] for fi in files if not fi.startswith("_") and fi.endswith(".py")]

    modules = {}
    for fi in names:
        modules[fi] = importlib.import_module(".".join(d + [fi]))

