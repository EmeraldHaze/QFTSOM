###API1 - imports###
import os
import importlib

files = os.listdir("./lib")
__all__ = [fi[:-3] for fi in files if not fi.startswith("_") and fi.endswith(".py")]

modules = {}
for fi in __all__:
    modules[fi] = importlib.import_module('lib.'+fi)

globals().update(modules)

###API2 - registry###
from lib import _reg
parts, groups = _reg.build_reg(modules)

###API3 - ugly hacks###
from lib import _ugly
ugly = _ugly.make(parts, groups)