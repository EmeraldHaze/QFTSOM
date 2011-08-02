from api import being
from data import thinkers, belongs
player = being('player', thinkers.player, {'hp':5}, [belongs.stick])
stickman = being('man', thinkers.man, {'hp':5}, [belongs.stick])
