import lib
from api import BeingInst, Exit, Rule


def getchoice(*valid, query="Choice? ", change=True):
    "A convience wrapper for thinkers.pchoice"
    if len(valid) == 1:
        valid = valid[0]
        #So that calls with an iter don't have to do getchoice(*valids, ..,)
    #print(valid)
    return lib.base.thinkers.pchoice(valid, query=query)


def change(battleargs):
    """
    This allows the user to change battle args by adding and removing reg items
    battleargs should be a list, of the form [{name:player}, {ruletype:rule},
     {exitname:exit}]
    """
    from core.shared import battle_order, reg_list as reg, modules

    for arg in battleargs:
        for item in arg.values():
            item.selected = True
            #These same items are in reg, so we'll acess them from here
            #and know which ones are in or out in the reg

    print("You must use non-numerical choices here. Try help first.")
    while 1:
        act = input("Action? ")
        try:
            act, arg = act.split()
        except ValueError:
            act, arg = act, ''

        if act == "help":
            print('help gives you this. "list" by itself lists all componants'
             'and takes these arguments: in (all selected componants), out '
             '(all unselected), b (all beings, which can be in the battle), r '
             '(rules, which determine how to do a given thing, like player '
             'order), e (all exits, which are exit conditions and effects, '
             'like die and win), modules (all modules), <module name> (all '
             "componants of that module). Naming a componant's number flips "
             ' it\'s selection status (selected --> unselected and vice versa '
             '? <componant number> gives more information about that componant'
             ". ? <module name> gives you more information about that module"
             '"end" ends the session.')

        elif act == "end":
            break

        elif act == "list":
            if arg == "modules":
                for module in modules.keys():
                    print(module)
            else:
                selectors = {\
                    "b":   lambda item: isinstance(item, BeingInst),
                    "r":   lambda item: isinstance(item, Rule),
                    "e":   lambda item: isinstance(item, Exit),
                    "in":  lambda item: item.selected,
                    "out": lambda item: not item.selected,
                    "":    lambda item: True}

                mselect = {module: (lambda item, module=module:
                    item.module == module) for module in list(modules.keys())}
                selectors.update(mselect)
                #Adds filters for specific modules.
                try:
                    condition = selectors[arg]
                    for n, componant in enumerate(reg):
                        if condition(componant):
                            print((str(n) + ":").ljust(3), str(componant))
                except KeyError:
                    #If there is no selector with that name
                    print(arg, "is not a valid list argument!")

        elif act == "?":
            try:
                index = int(arg)
                try:
                    print(reg[index].info, "Module:", reg[index].module)
                except IndexError:
                    print("No such componant")
            except ValueError:
                #If it's not an int, it should be a module name
                try:
                    print(modules[arg])
                except KeyError:
                    print("No such module")

        elif act == "break":
            raise Exception("err'd by request")

        else:
            #Flip selection status
            try:
                item = reg[int(act)]
                item.selected ^= True
                #X XOR True flips X
                print(str(item) + "'s inclusion flipped")
            except (ValueError, IndexError):
                print("Invalid action, or choice is out of range")

    D = [{}, {}, {}]
    for item in reg:
        if item.selected:
            item.selected = False
            D[battle_order.index(item.plural)][item.name] = item
    #Goes through the reg, inserting selected componants into the right place
    return D


def custombattle(dummy_arg):
    "Starts a custom battle by change()ing a blank arg list and running it"
    print("You're making your own battle now. It follows defaults, so you "
    "don't need to have rules and exits- just people (enemies, normally)")
    args = change([{}, {}, {}])
    if getchoice("Yes", "No", query="Start battle? ") == "Yes":
        from core.does import battle
        battle([list(arg.values()) for arg in args])


def ideas(dummy_arg):
    "Writes an idea with a name to a file"
    s = input("What is your idea/suggestion/feedback? (One submit per idea)\n")
    from core.shared import name
    open("ideas", "a").write(name + ": " + s + "\n")
    print("Idea/feedback/suggestion submitted.")
