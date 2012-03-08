"""
This module contains those functions for those does that can be used in
node commands. To add a command, simply add a function with the command's name.
"""

from core.config import debug, at, info


def say(arg):
    print(arg)


def battle(arg):
    """
    Starts a battle. Arg should be of the form [[beings], [exits], [rules]].
    Any element except the former can be ommited. If both are ommited, the
    second pair of braces is unncerry
    """
    import game
    import core
    at("does.battle")
    if type(arg[0]) is not list:
        #If it's not a nested list
        arg = [arg]
    while len(arg) < 3:
        arg.append([])
        #Pads the arg too 3 elements
    debug(arg)
    #import pdb;pdb.set_trace()
    args = map(_parsearg, arg, game.defaults.battle.args)
    b = core.Battle(*args)
    b.start()


def _parsearg(args, default):
    """
    Makes a complete sect from args and default. About:
    args: [obj1, obj2], objects to be in this sect
    default: {name:obj}, to there if not overriden
    returns: {name:obj} with all of objects from args and those of defaults
    which aren't overridden by args objects that have the same .name
    """
    base = default.copy()
    arg_dict = {}
    for arg in args:
        arg_dict[arg.type_ if "type_" in dir(arg) else arg.name] = arg
    base.update(arg_dict)
    return base


def send(arg):
    return arg
    #If something is returned, it is set as the new node
