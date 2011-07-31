def start(people, exits, mods):
    setup()
    #Sets up the clock, sceduals eavrybody, generates ability lists, and makes a dict of players, with there names as the keys. Also makes a trigger stack, trigs
    while 1:
        ###Make players of this tick go
        for player in clock.players():
            #For each player
            action = player.think(players)
            #Get his action
            #Calls the thinker of a player and supply him with info about the players.
            #If he is honest, he will only take as much as he should have.
            #He can store info in the player untill the next time he is caleld
            #Actions are ussally lists of tuples of this form:
            #Trigger, Time, Target, Effect
            #If there is a non-recurisve trigger present, then it will be
            #Trigger, None, Time, Target, Effect
            do_action(action)
            ####Rescedule- Must be worked out. Important
            
        ###Apply effects of this tick
        for effect in clock.effect():
            target, stat, change = effect
            players[target].stats[stat]+=effect

        ###Apply actions of this tick
        for action in clock.actions(): do_action(action)

        ##Check for exit conditions
        for player in players.keys():
            for exit in exits:
                if exit.condition(players[player]):
                    exit.effect(players[player])
                    del players[player]
        ###next tick
        clock.tick()

def do_action(action):
    for act in action:
        #For each part of his action
        trigger, effect = act[0], act[1:]
        if act[0]:
            global trigs
            #If this part has a trigger 
            trigs[trigger] = effect
            #Add it to the trigger stack
            #Notes:  This can means that triggers can be stacked.
            #Triggers are not finnished 
            #The triggering action must be hooked
        else:
            #If it has no trigger
            global clock
            clock.addeffect(effect)
            #Add the event. addevent puts it event[0] ticks away from now.
    
                    
