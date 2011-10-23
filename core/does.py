def say(string):
    """do_ node executer print function"""
    print(string)

def battle(arg):
    """Start a battle- arg should be formatted like this:
    player1, player2, etc|exit1, exit2, etc|rule1, rule2, etc"""
    import game, core
    #Make lists of the actual objects named in the arg
    args = map(parsearg, arg.split("|"), game.defaults.battle)
    args = list(args)
    b = core.Battle(*args)
    b.start()

def parsearg(arg, default = {}):
    global game, lib
    import game, lib
    parsed = {}
    for part in arg.split(", "):
        if part:
            if ":" in part:
                name, part = part.split(":")
                part = eval(part)
            else:
                part = eval(part)
                name = part.name
            parsed[name] = part
    default.update(parsed)
    return default

