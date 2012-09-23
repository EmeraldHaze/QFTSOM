import api
from lib.limbs import player, mad, python, monty, flylord
from lib.base import rules, exits


palcenet = api.Placeet(0, {
    0: api.Node([], [], [
        ('say', "You'll fight a taco! (Hint: choose a limb, then an attack)"),
        ("battle", [player, mad]),
        ('say',"You must go on to fight wierder stuff!"),
        ("send", 1)
        ]),
    1: api.Node([], [], {'battle': [player, python],  "send": 2}),
    2: api.Node([], [], {'battle': [player, monty],   "send": 3}),
    3: api.Node([], [], {'battle': [player, flylord], "send": 4}),
    4: api.Node(
            [],
            [],
            {"say": "That's all the battles to be had"},
            exit_='hub'
        )
})

rules = rules = {
    "schedule": rules.speed,
    "get_actions": rules.get_all,
    "wipe_hist": rules.wipe_normal
}
