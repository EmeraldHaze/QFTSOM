from api import PlaceNet, Place
from core import Game
import lib
from lib import simple
from lib.base import rules, exits

placenet = PlaceNet([
    Place("Groove", ["Clearing"], "You're in the groove!", simple.drunkard),
    Place("Clearing", ["Groove"], "A rather plain clearing", simple.player)
])

rules = {
    "schedule": rules.next,
    "get_actions": rules.get_all,
    "wipe_hist": rules.wipe_normal
}


game = Game(placenet, rules, [exits.die])

choosen_game = game
