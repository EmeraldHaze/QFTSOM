from api.being import being
from data import thinkers, belongs
player = being('player', thinkers.player, {'hp':5}, {'stick':belongs.stick})
man = being('man', thinkers.man, {'hp':5}, {'stick':belongs.stick})
