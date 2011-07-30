def start(people, exits, mods):
    setup()
    #Sets up the clock, sceduals eavrybody, and generates ability lists. Also makes players list
    while 1:
        ###Get actions of all players of this tick
        actions = []
        for player in clock.players(): actions.append(player.think(players))
