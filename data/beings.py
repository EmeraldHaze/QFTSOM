from api.being import Being
from data import thinkers, belongs
player = Being('Player', thinkers.player,
    {'hp': 6, 'win': 0}, {'stick': belongs.stick})
man = Being('Man', thinkers.man,
    {'hp': 5, 'win': 0}, {'stick': belongs.stick})
#man2 = Being('OtherMan', thinkers.other_man,
#    {'hp': 4, 'win': 0}, {'stick':belongs.stick})
#staffo = Being('Staffo', thinkers.man,
#{'hp': 5, 'win': 0}, {'staff':belongs.staff})
