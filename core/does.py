def say(string):
    """do_ node executer print function"""
    print(string)

def battle(arg):
    """
    Starts a battle. Full form: [[]]"""
    import game, core
    #Make lists of the actual objects named in the arg
    if type(arg[0]) is not list:
        arg = [arg]
    for i in range(3-len(arg)):
        arg.append([])#Pads the arg too 3 elements
    args = map(parsearg, arg, game.defaults.battle)
    b = core.Battle(*args)
    b.start()

def parsearg(args, default):
    """
    Makes a complete sect from
    args: [obj1, obj2], objects to be in this sect
    default: {name:obj}, to there if not overriden
    returns: {name:obj} with all of objects from args and those of defaults
    which aren't overridden by args objects that have the same .name
    """
    base = default.copy()
    arg_dict = {}
    for arg in args:
        arg_dict[arg.name] = arg
    base.update(arg_dict)
    return base

def send(arg):
    return arg
    #If something is returned, it is set as the new node