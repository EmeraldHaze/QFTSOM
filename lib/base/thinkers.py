from api import Thinker

def think_maker(gettarget, getaction):
    @Thinker
    def thinker(self):
        action = getaction(self.player, self.battle)
        target = gettarget(self.player, self.battle)
        return action.instance(self.player, target, self.battle)
    return thinker

def mosttarget(player, battle, cmp = int.__lt__):
    target = [None, float("inf")]
    for enemy in battle.player_list:
        if enemy is not player:
            hp = enemy.stats["HP"]
            if cmp(hp, target[1]):
                target = [enemy, hp]
    return target[0]

least = lambda player, battle: mosttarget(player, battle, int.__gt__)
firstact = lambda player, battle: player.actions[0]

def pchoice(choices, extra=None, query="Choice? "):
    """
    This function gets a choice from the user.
    choices should be {name:value}, where value is returned if name is choosen
    It can also be a iterable of values with name attributes
    extra, if set, prints out some extra information. It should be (name: expr),
    and name: eval(expr) is printed as part of the name
    """
    if type(choices) == dict:
        namelist = list(choices.keys())
    else:
        try:
            namelist, choices, choicelist = [], {}, choices
            for choice in choicelist:
                namelist.append(choice.name)
                choices[choice.name] = choice

        except AttributeError:
            namelist = choicelist
            choices = dict(zip(namelist, choicelist))

    for num, name in enumerate(namelist):
        if not extra:
            print("{}: {}".format(num, name))
        else:
            extraname, code = extra
            choice = choices[name]
            print("{}: {}, {}: {}".format(num, name, extraname, eval(code)))
    choicename = None
    while not choicename:
        try:
            q = input(query)
            choicename = namelist[int(q)]
        except (ValueError, IndexError):
            if q == "break":
                raise Exception
            else:
                print("Bad choice! Bad!")
    return choices[choicename]

ptarget = lambda player, battle: pchoice(battle.player_list, ("HP", "choice.stats['HP']"), "Target? ")
paction = lambda player, battle: pchoice(player.battle_list, ("MP", "choice.metadata['MPC']"), "Actions? ")