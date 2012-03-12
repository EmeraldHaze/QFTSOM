"This file contains the root nodemap"
from api import Net, Node
from game.nodeutils import change, custombattle, ideas
from game import defaults
from lib.simple import game as game1
from lib.limb import game as game2


nodemap = Net("hub", {
    "hub": Node(
                ["game1", "game2", "change", "custom", "ideas"],
                ["Simple", "Limbs", "Ideas"],#""Change Defaults", "Custom Game", "Ideas"],
             {'say': "Here are some game presets. You can change the defaults "
             "(rules and exit conditions) which will apply to presets, and/or "
             "make your own game. It may not work, note. Being a good person, "
             "you'll also give feedback and ideas."}
             ),
    "game1": game1,
    "game2": game2,
    "change": Node([], [], [("say", "You are now chaning the defaults. They "
    "can be overriden, but ussually rules and exits are not touched, so they "
    "apply to everything"), (change, defaults.battle), ("send", "hub")]),
    "custom": Node([], [], [(custombattle, None), ("send", "hub")]),
    "ideas":  Node([], [], [(ideas, None), ("send", "hub")])
})
