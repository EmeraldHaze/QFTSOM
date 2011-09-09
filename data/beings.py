from api.being import Being
from data import thinkers, belongs
player = Being('Player', thinkers.player,
    {'HP': 6}, {'stick': belongs.stick})
man = Being('Man', thinkers.man,
    {'HP': 5}, {'stick': belongs.stick})
man2 = Being('OtherMan', thinkers.other_man,
    {'HP': 4}, {'stick':belongs.stick})
staffo = Being('Staffo', thinkers.man,
{'HP': 5}, {'staff':belongs.staff})

#dwarf = {'Dwarf', thinkers.dwarf,
#    {'str':13,'int':7}, {'Axe':belongs.axe, "Helm":belongs.helm