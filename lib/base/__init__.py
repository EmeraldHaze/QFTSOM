from lib import _reg
from core import shared
shared.current_module = "base"
shared.modules["base"] = "This is a base collection of modules , providing resources for all the other modules"
modules = _reg.get_modules(["lib", "base"])
globals().update(modules)