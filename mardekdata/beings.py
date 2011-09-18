from api.being import Being
from data import thinkers, belongs
aalia = Being("Aalia", thinkers.healer, {"STR":9, "VIT":10, "SPR":20, "AGL":16 ,
        "ATK":10, "DEF":2, "MDEF":2, "LVL":6, "basehp":25, "hplvl":10},
        {"HeartStaff": belongs.heartstaff, "MageRobe": belongs.magerobe,
        "SilverRing": belongs.silverring, "WaterPendant": belongs.waterpendant}, {"team":0})