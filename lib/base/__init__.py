from lib import _reg
modules = _reg.get_modules(["lib", "base"])
globals().update(modules)