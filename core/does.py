def say(string):
    """do_ node executer print function"""
    print(string)

def battle(arg):
    """Start a battle- arg should be formatted like this:
    player1, player2, etc|exit1, exit2, etc|rule1, rule2, etc"""
    import game, core
    #Make lists of the actual objects named in the arg
    if type(arg[0]) is not list:
        arg = [arg]
    for i in range(3-len(arg)):
        arg.append([])#Pads the arg too 3 elements
    args = map(parsearg, arg, game.defaults.battle)
    args = list(args)
    b = core.Battle(*args)
    b.start()

def parsearg(args, default):
    base = dict(default)
    arg_dict = {}
    for arg in args:
        arg_dict[arg.name] = arg
    base.update(arg_dict)
    return base

def tofile(arg):
    from core.shared import name as username
    if type(arg) == str:
        arg = "a", username + (arg,)
    elif len(arg) == 2:
        arg = ("a",) + arg
    name, mode, s = arg
    open(name, mode).write(s)