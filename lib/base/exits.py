from api.exit import Exit

die = Exit('die', (lambda p, b: p.stats['HP'] <= 0),  (lambda p, b: print(p.name, 'is woefully unlifelike!')), ["main", "HP"], ["players"])
win = Exit('win', (lambda p, b: b.player_list == [p]),(lambda p, b: print(p.name, "has vanquished his foes!")), ['players'], ["players"])