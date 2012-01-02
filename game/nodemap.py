from itertools import chain
from api import Net, Node
from lib import simple, limb#, fancy
import lib

def getchoice(*valid, query="Choice? ", change=True):
    if len(valid) == 1:
        valid = valid[0]
        #So that calls with an iterable don't have to do getchoice(*valids, ..,)
    #print(valid)
    return lib.base.thinkers.pchoice(valid, query=query)

def change(battleargs):
    """
    This allows the user to change battle-arguments
    battleargs should be a list, of the form [{name:player}, {ruletype:rule},
     {exitname:exit}]
    """
    from core.shared import battle_order, registry as reg
    D = dict(zip(battle_order, battleargs))
    #covert to named-arg form
    while 1:
        choice = getchoice("help", "list", "players", "rules", "exits", "remove", "list possibles" "quit")
        if choice == "help":
            print('"players" is who is in the battle, who\'s fighting. "rules"'
             ' determine how to do a given thing, like determining player order.'
             ' "exits" are exit conditions and effects, like die and win.'
             ' "remove" removes objects, of course. Note that adding something'
             ' with the same name (such as rules of the same type) overwrites'
             ' the old item.')

        elif choice == "quit":
            break

        elif choice == "remove":
            name = getchoice(list(chain.from_iterable(D.values())), query="What do you want remove? ")
            for sect in D.values():
                sect.pop(name, None)
                #This pops the name if it exsists and nothing if not. It removes name from any sections in which it is

        elif choice == "list":
            print("Rules:")
            for rule in D["rules"].values():
                print("    %s: %s" % (rule.name, rule.func.__name__))
            for sect in ("players", "exits"):
                print(sect.title() + ":")
                for item in D[sect].values():
                    print("    " + item.name)

        #elif choice == "list possibles":
            #print("Rules:")
            #for rule in D["rules"].values():
                #print("    %s: %s" % (rule.name, rule.func.__name__))
            #for sect in ("players", "exits"):
                #print(sect.title() + ":")
                #for item in D[sect].values():
                    #print("    " + item.name)


        elif choice == "rules":
            ruletype = getchoice(*reg["rules"].keys(), query="What rule type do you want to set? ")
            rule = getchoice(reg["rules"][ruletype], query="What rule do you want to set? ", change=False)
            D["rules"][ruletype] = rule

        else:
            obj = getchoice(reg[choice], query="What %s do you want to add? " % choice[:-1], change=False)
            D[choice][obj.name] = obj
            #D[type of object][name of object] = object
    return [D[arg] for arg in battle_order]
    #Convert to indiced args form

def custombattle(dummy_arg):
    print("You're making your own battle now. It follows defaults, so you don't"
    " necessarily have to have rules and exits- just people (enemies, normally)")
    args = change([{}, {}, {}])
    if getchoice("Yes", "No", query="Start battle? ") == "Yes":
        from core.does import battle
        battle([list(arg.values()) for arg in args])

def ideas(dummy_arg):
    s = input("What is your idea, suggestion, or feedback? (Please, one idea per line)")
    from core.shared import name
    open("ideas", "a").write(name + ": " + s + "\n")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ")
    print("Idea/feedback/suggestion submitted.")

from game import defaults

game1 = Net(0, {\
    0:Node([1], ["Advance!"], [('say', "You must fight a weird taco! (Hint: choose a limb to attack, then an attack)"), ("battle", [limb.mad]), ('say',"You must go on to fight wierder stuff!")]),
    1:Node([2], ["Procced!"], {'battle': [limb.python]}),
    2:Node([3], ["Procced!"], {'battle': [limb.monty]}),
    3:Node([4], ["Procced!"], {'battle': [limb.flylord]}),
    4:Node([], [], {"say": "That's all the battles to be had"}, exit_='hub')
    })

nodemap = Net("hub", {\
    "hub":Node(["game1", "change", "custom", "ideas"], ["Game #1", "Change Defaults", "Custom Game", "Ideas"], {'say': "Here are some game presets. You can change the defaults (rules and exit conditions) which will apply to presets, and/or make your own game. It may not work, note. Being a good person, you'll also give feedback and ideas."}),
    "game1":game1,
    "change":Node([], [], [("say", "You are now chaning the defaults. They can be overriden, but ussually rules and exits are not touched, so they apply to everything"), (change, defaults.battle), ("send", "hub")]),
    "custom":Node([], [], [(custombattle, None), ("send", "hub")]),
    "ideas": Node([], [], [(ideas, None), ("send", "hub")])
})
