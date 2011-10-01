import lib
players = {}
exits = {"win":lib.base.exits.win, "die":lib.base.exits.die}
rules = {"schedule":lib.base.rules.next}
battle = [players, exits, rules]

statrules = []