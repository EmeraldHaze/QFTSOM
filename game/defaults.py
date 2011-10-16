import lib
players = {}
exits = {"win":lib.base.exits.win, "die":lib.base.exits.die}
rules = {"schedule":lib.base.rules.next, "get_actions":lib.base.rules.get_actions}
battle = [players, exits, rules]