from core import shared
shared.current_module = "base"
shared.modules["base"] = """This is a base collection of modules,
    providing resources for all the other modules"""

from lib.base import actions, exits, rules, statuses, thinkers
