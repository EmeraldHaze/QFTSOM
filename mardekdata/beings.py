from api.being import Being
from data import thinkers, belongs

aalia = Being("Aalia", thinkers.healer, {"STR":9, "VIT":10, "SPR":20, "AGL":16 ,
        "LVL":6, "basehp":25, "hplvl":10},
        {"HeartStaff": belongs.heartstaff, "MageRobe": belongs.magerobe,
        "SilverRing": belongs.silverring, "WaterPendant": belongs.waterpendant}, {"team":"sav"})

bernard = Being("Bernard", thinkers.attacker, {"STR":12, "VIT":8, "SPR":27, "AGL":13,
    "EVA":0, "LVL":11, "basehp":20, "hplvl":8},
    {"Walking Stick":belongs.walkingstick, "Hempen Robe":belongs.hemprobe,
    "Silver Ring":belongs.silverring, "FirePendant": belongs.firependant}, {"team":"sav"})

vennie = Being("Vennie", thinkers.attacker, {"STR":12, "VIT":14, "SPR":10, "AGL": 22,
    "EVA":0, "LVL":7, "basehp":35, "hplvl":14},
    {"Dagger":belongs.dagger, "Bandit Leather":belongs.leathers,
    "Ring of AGL":belongs.algring, "AirPendant":belongs.airpendant}, {"team":"sav"})