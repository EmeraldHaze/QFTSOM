from api.belong import Belong
from data import actions

heartstaff = Belong("Heart Staff", [actions.cure, actions.regen, actions.msheild, actions.sheild], {"POW":10, "CRIT":1, "SPR":1})
walkingstick = Belong("Walking Stick", [actions.immolate, actions.glaciate, actions.thunderstorm], {"POW":10, "SPR":1})
dagger = Belong("Dagger", [actions.attack, actions.viperfang, actions.eyegouge, actions.slumberstab], {"POW":16, "CRIT":10})

magerobe = Belong("Mage Robe", [], {"MDEF":2})
hemprobe = Belong("Hemp Robe", [], {"MDEF":4, "SPR":1, "MP":10})
leathers = Belong("Bandit leather", [], {"DEF":2, "MDEF":2, "AGL":2, "AirRes":25})

silverring = Belong("Silver Ring", [], {"DEF":2})
aglring = Belong("Ring of AGL", [], {"AGL":1})

waterpendant = Belong("Water Pendant", [], {"MDEF":2, "WaterRes":50, "EarthRes":-50})
firependant = Belong("Fire Pendant", [], {"MDEF":2, "FireRes":50, "WaterRes":-50})
airpendant = Belong("Air Pendant", [], {"MDEF":2, "AirRes":50, "FireRes":-50})