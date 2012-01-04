from api import Net, Node
from lib import base, simple, limb#, fancy
from game.nodeutils import change, custombattle, ideas
from game import defaults
2
game1 = Net(0, {\
    0:Node([1], ["Advance!"], [('say', "You must fight a weird taco! (Hint: choose a limb to attack, then an attack)"), ("battle", [limb.mad]), ('say',"You must go on to fight wierder stuff!")]),
    1:Node([2], ["Procced!"], {'battle': [limb.python]}),
    2:Node([3], ["Procced!"], {'battle': [limb.monty]}),
    3:Node([4], ["Procced!"], {'battle': [limb.flylord]}),
    4:Node([], [], {"say": "That's all the battles to be had"}, exit_='hub')
    })

game2 = Net(0, {\
    0:Node([], [], {"say":"The folks you're to fight are simple: they attack he who has the least HP. The town fool, Oddball, does the reverse, while the puissant Staffo hits twice as hard as you stick-possesing fools.","send":1}),
    1:Node([], [], {'battle': [[simple.man, simple.player, simple.man2, simple.staffo, simple.oddman], [base.exits.die], [base.rules.next, base.rules.reset]]}, exit_="hub")
    })

nodemap = Net("hub", {\
    "hub":Node(["game1", "game2", "change", "custom", "ideas"], ["Game #1", "Game #2", "Change Defaults", "Custom Game", "Ideas"], {'say': "Here are some game presets. You can change the defaults (rules and exit conditions) which will apply to presets, and/or make your own game. It may not work, note. Being a good person, you'll also give feedback and ideas."}),
    "game1":  game1,
    "game2":  game2,
    "change": Node([], [], [("say", "You are now chaning the defaults. They can be overriden, but ussually rules and exits are not touched, so they apply to everything"), (change, defaults.battle), ("send", "hub")]),
    "custom": Node([], [], [(custombattle, None), ("send", "hub")]),
    "ideas":  Node([], [], [(ideas, None), ("send", "hub")])
})
