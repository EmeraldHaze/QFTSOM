from api import PlaceNet, Place
from core import Game
import lib
from lib import new
from lib.base import rules, exits

placenet = PlaceNet([
    Place("Groove", ["Clearing"], "You're in the groove!", new.drunkard),
    Place("Clearing", ["Groove"], "A rather plain clearing", new.player, new.knife)
])

rules = {
    "schedule": rules.speed,
    "get_actions": rules.get_all,
    "wipe_hist": rules.wipe_normal
}


game = Game(placenet, rules, [exits.die])

choosen_game = game
