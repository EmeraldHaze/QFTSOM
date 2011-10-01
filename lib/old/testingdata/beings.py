from api.being import Being
from data import thinkers, belongs
#simpleplayer = Being('Player', thinkers.player,
    #{'HP': 6}, {'Sword': belongs.stick})
#man = Being('Man', thinkers.man,
    #{'HP': 5}, {'stick': belongs.stick})
#man2 = Being('OtherMan', thinkers.other_man,
    #{'HP': 4}, {'stick':belongs.stick})
#staffo = Being('Staffo', thinkers.man,
#{'HP': 5}, {'staff':belongs.simplestaff})

dwarf = Being('Dwarf', thinkers.simple,
    {'STR':13,'INT':7}, {'Axe':belongs.axe, "Helm":belongs.helm}, thinkinit = thinkers.stdinit)

player = Being('Player', thinkers.player,
    {'STR': 10, 'INT':10}, {'Staff': belongs.staff})

dwarf2 = Being('Dwarf2', thinkers.simple,
    {'STR':13,'INT':7}, {'Axe':belongs.axe, "Helm":belongs.helm}, thinkinit = thinkers.stdinit)

rouge = Being("Rouge", thinkers.player,
    {"STR":10, "INT":12}, {"Dagger":belongs.dagger, "Bomb":belongs.bomb, "Quick Shoes":belongs.shoes})