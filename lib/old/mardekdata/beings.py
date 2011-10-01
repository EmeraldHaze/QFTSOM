from api.being import Being
from data import thinkers, belongs

class SBeing(Being):
    @property
    def actions(self):
        return list(self.actionset)
    @property
    def act_dict(self):
        return {action.name:action for action in self.actions}

Being = SBeing

aalia = Being("Aalia", thinkers.healer, {"STR":9, "VIT":10, "SPR":20, "AGL":16 ,
        "LVL":6, "basehp":25, "hplvl":10},
        {"HeartStaff": belongs.heartstaff, "MageRobe": belongs.magerobe,
        "SilverRing": belongs.silverring, "WaterPendant": belongs.waterpendant}, {"team":"sav"})

bernard = Being("Bernard", thinkers.attacker, {"STR":12, "VIT":8, "SPR":27, "AGL":13,
    "EVA":0, "LVL":11, "basehp":20, "hplvl":8},
    {"Walking Stick":belongs.walkingstick, "Hempen Robe":belongs.hemprobe,
    "Silver Ring":belongs.silverring, "FirePendant": belongs.firependant}, {"team":"sav"})

vennie = Being("Vennie", thinkers.player, {"STR":12, "VIT":14, "SPR":10, "AGL": 22,
    "EVA":0, "LVL":7, "basehp":35, "hplvl":14},
    {"Dagger":belongs.dagger, "Bandit Leather":belongs.leathers,
    "Ring of AGL":belongs.aglring, "AirPendant":belongs.airpendant}, {"team":"mar"})

bartholio = Being("Bartholio", thinkers.bart, {"STR":22, "VIT":19, "SPR":8, "AGL":11,
    "EVA":0, "basehp":45, "hplvl":18, "LVL":7},
    {"Mythril Greatblade":belongs.mythrilblade, "Bronze Armor":belongs.bronzearmor,
    "Gauntlet":belongs.gauntlet, "Green Beads":belongs.greenbeads}, {"team":"mar"})

#mardek = Being("Mardek", thinkers.player, {"STR":17, "VIT":15, "SPR":12, "AGL":9, ""})