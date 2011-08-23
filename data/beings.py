from api.being import Being
from data import thinkers, belongs
player = Being('Player', thinkers.player, {'hp':5, 'win':0}, {'stick':belongs.stick})
man = Being('Man', thinkers.man, {'hp':5, 'win':0}, {'stick':belongs.stick})
