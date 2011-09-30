from lib import _reg, _ugly

###API1
modules = _reg.get_modules(["lib"])
globals().update(modules)

###API2
parts, groups = _reg.build_reg(modules)

###API3
ugly = _ugly.make(parts, groups)

import base