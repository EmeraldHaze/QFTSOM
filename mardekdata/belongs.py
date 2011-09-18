from api.belong import Belong
from data import actions
heartstaff = Belong("Heart Staff", [actions.cure, actions.regen, actions.mshield, actions.shield], {"POW":10, "CRIT":1, "SPR":1})
magerobe = Belong("Mage Robe", [], {"MDEF":2})
silverring = Belong("Silver Ring", [], {"DEF":2})
waterpendant = Belong("Water Pendant", [], {"MDEF":2, "WaterRes":50, "EarthRes":-50})