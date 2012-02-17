from api.exit import Exit

die = Exit('die',
    (lambda being, battle: being.stats['HP'] <= 0),
    (lambda being, battle: print(being.name, 'is woefully unlifelike!')),
    ["main", "HP"], ["beings"])

win = Exit('win',
    (lambda being, battle: battle.being_list == [being]),
    (lambda being, battle: print(being.name, "has vanquished his foes!")), ["beings"], ["beings"])
