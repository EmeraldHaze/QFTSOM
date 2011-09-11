from collections import OrderedDict
default = {"MAXHP": "self.stats['HP']"}
old_qftsom = OrderedDict([("HP", "self.stats['STR']*5+50"),
    ("MP", "self.stats['INT']*5+50"),
    ("DEF", "self.stats['STR']"),
    ("MDEF", "self.stats['INT']"),
    ("MAXMP", "self.stats['MP']"),
    ("MAXHP",   "self.stats['HP']"),
    ("MAXWPNDMG", "0"),
    ("MINWPNDMG", "0")])