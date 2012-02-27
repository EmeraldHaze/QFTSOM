from api import Thinker

def think_maker(gettarget, getaction):
    @Thinker
    def thinker(self):
        target = gettarget(self.being, self.battle)
        action = getaction(self.being, self.battle)
        act = action.instance(self.being, target, self.battle)
        return act
    return thinker

def mosttarget(being, battle, cmp = int.__lt__):
    target = [None, float("inf")]
    for enemy in battle.being_list:
        if enemy is not being:
            hp = enemy.stats["HP"]
            if cmp(hp, target[1]):
                target = [enemy, hp]
    return target[0]

least = lambda being, battle: mosttarget(being, battle, int.__gt__)
firstact = lambda being, battle: being.actions[0]

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
        printname = name[0].upper() + name[1:]
        #Because capitalize and title mess up things like "Dwarf II"
        if not extra:
            print("{}: {}".format(num, printname))
        else:
            extraname, code = extra
            choice = choices[name]
            print("{}: {}, {}: {}".format(num, printname, extraname, eval(code)))
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

ptarget = lambda being, battle: pchoice(battle.being_list, ("HP", "choice.stats['HP']"), "Target? ")
paction = lambda being, battle: pchoice(being.actions, ("MP", "choice.data['MPC']"), "Actions? ")
pthinker = think_maker(ptarget, paction)
