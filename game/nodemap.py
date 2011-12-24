from api import Net, Node
from lib import simple, limb#, fancy

def write(arg):
    name, query = arg
    open(name, "a").write(input(query))

game1 = Net(0, {\
    0:Node([1], ["Advance!"], [('say',"You must fight a weird taco! (Hint: choose a limb to attack, then an attack)"), ("battle", [limb.mad]), ('say',"You must go on to fight wierder stuff!")]),
    1:Node([2], ["Procced!"], [('battle', [limb.python])]),
    2:Node([3], ["Procced!"], [('battle', [limb.monty])]),
    3:Node([4], ["Procced!"], [('battle', [limb.flylord])]),
    4:Node([], [], [("say", "That's all the battles to be had")], exit_='hub')
    })

nodemap = Net("hub", {\
    "hub":Node(["game1"], ["Game #1"], {'say': "These are the avalible games. Being a good person, you'll give feedback at the end of each, right? An even better action might be to suggest general ideas, which is also an option! You'd be amazed at all the things good people do!"}),
    "game1":game1,
    "ideas":Node(["hub"], ["Return to hub"], [()])
})
