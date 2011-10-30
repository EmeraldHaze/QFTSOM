from random import randint, choice, shuffle
from collections import defaultdict
from lib import base
import api

def basicattack(self, battle, targets):
    act = (action for action in self.actions if action.name == "attack").next()
    target = choice(targets)
    return act.format(battle, self, target)

def teams(battle, you = None):
    t = defaultdict(lambda :[])
    [t[player.data["team"]].append(player) for player in battle.players]
    if you:
        return (team for name, team in t.items() if name != you).next() , t[you]
    else:
        return t

def healer(self, battle):
    targets, allies = teams(battle, self.data["team"])
    wounded = [ally for ally in allies if ally.stats["HP"]/ally.stats["MAXHP"] < 0.9]
    if len(wounded):
        action = self.act_dict["cure"]
        target = wounded[0]
    else:
        buffs = ["shield", "m. shield", "regen"]
        shuffle(buffs)
        shuffle(allies)
        action = None
        for buff in buffs:
            for ally in allies:
                if buff not in ally.status_list:
                    action =  self.act_dict[buff]
                    target = ally
                    break
    if not action:
        return basicattack(battle, targets)
    else:
        return action.format(self, target)

#heartstaff = Belong("Heart Staff", {"POW":10, "CRIT":1, "SPR":1}, [actions.cure, actions.regen, actions.mshield, actions.shield])
#walkingstick = Belong("Walking Stick", {"POW":10, "SPR":1}, [actions.immolate, actions.glaciate, actions.thunderstorm])
#dagger = Belong("Dagger", {"POW":16, "CRIT":10}, [actions.attack, actions.viperfang, actions.eyegouge, actions.slumberstab])
#mythrilblade = Belong("Mythril Greatblade", {"POW":22, "CRIT":4}, [actions.attack, actions.powerattack, actions.avengance])

#magerobe = Belong("Mage Robe", {"MDEF":2})
#hemprobe = Belong("Hemp Robe", {"MDEF":4, "SPR":1, "MP":10})
#leathers = Belong("Bandit leather",{"DEF":2, "MDEF":2, "AGL":2, "AirRes":25})
#bronzearmor = Belong("Bronze Armor", {"DEF":6})

#silverring = Belong("Silver Ring", {"DEF":2})
#aglring = Belong("Ring of AGL", {"AGL":1})
#gauntlet = Belong("Gauntlet", {"DEF":1, "STR":2})

#waterpendant = Belong("Water Pendant", {"MDEF":2, "WaterRes":50, "EarthRes":-50})
#firependant = Belong("Fire Pendant", {"MDEF":2, "FireRes":50, "WaterRes":-50})
#airpendant = Belong("Air Pendant", {"MDEF":2, "AirRes":50, "FireRes":-50})
#greenbeads = Belong("Green Beads", {"MDEF":4, "VIT":1, "EarthRes":20})

#aalia = api.Being("Aalia", healer, {"STR":9, "VIT":10, "SPR":20, "AGL":16, "LVL":6,
        #"basehp":25, "hplvl":10}, [heartstaff, magerobe, silverring, waterpendant], {"team":"sav"})

#bernard = Being("Bernard", thinkers.attacker, {"STR":12, "VIT":8, "SPR":27, "AGL":13,
    #"EVA":0, "LVL":11, "basehp":20, "hplvl":8},
    #{"Walking Stick":belongs.walkingstick, "Hempen Robe":belongs.hemprobe,
    #"Silver Ring":belongs.silverring, "FirePendant": belongs.firependant}, {"team":"sav"})

#vennie = Being("Vennie", thinkers.player, {"STR":12, "VIT":14, "SPR":10, "AGL": 22,
    #"EVA":0, "LVL":7, "basehp":35, "hplvl":14},
    #{"Dagger":belongs.dagger, "Bandit Leather":belongs.leathers,
    #"Ring of AGL":belongs.aglring, "AirPendant":belongs.airpendant}, {"team":"mar"})

#bartholio = Being("Bartholio", thinkers.bart, {"STR":22, "VIT":19, "SPR":8, "AGL":11,
    #"EVA":0, "basehp":45, "hplvl":18, "LVL":7},
    #{"Mythril Greatblade":belongs.mythrilblade, "Bronze Armor":belongs.bronzearmor,
    #"Gauntlet":belongs.gauntlet, "Green Beads":belongs.greenbeads}, {"team":"mar"})