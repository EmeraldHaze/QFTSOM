from collections import defaultdict
def build_reg(modules):
    parts = defaultdict(lambda :{})
    groups = defaultdict(lambda :{})

    for module_name, module in modules.items():
        for comp_name in dir(module):
            if not comp_name.startswith("_"):
                comp = getattr(module, comp_name)
                groups[module_name][comp_name] = comp
                parts[comp_name + "s"][module_name] = comp
    return dict(parts), dict(groups)