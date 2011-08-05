from api.being import being
from data import thinkers, belongs
player = being('Player', thinkers.player, {'hp':5, 'win':0}, {'stick':belongs.stick})
man = being('Man', thinkers.man, {'hp':5, 'win':0}, {'stick':belongs.stick})
