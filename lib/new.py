import api
from core import shared

shared.blank()
shared.current_module = "new"
shared.modules["new"] = """This is a module for trying out the refactored
changes"""

pass
