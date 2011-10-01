import lib
players = {}
exits = {"win":lib.base.exits.win, "die":lib.base.exits.die}
rules = {"schedule":lib.base.rules.next, "player_actions":lib.base.rules.actions}
battle = [players, exits, rules]

statrules = [("MAXHP", "self.stats['HP']")]