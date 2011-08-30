from collections import deque

def start(player_list, exits, mods):
    """Starts battle"""
    def do_action(action):
        for effect in action.effects:
            battletime.addeffect(effect, effect.tick)
            
    players, trigs = {}, {}
    #trigs is the trigger stack. It will be used by do_action.
    for player in player_list:
        players[player.name] = player
    #Fill up players dict with name:person
    battletime = Clock('player', 'effect')
    ###Generate player action lists
    for player in players.values():
        #For each player
        for belong in player.belongs.values():
            #For each of his belongings
            for action in belong.actions:
                #For each of it's actions
                player.actions.append(action.copy('action list generation'))
                #Append a copy [So that the original doesn't change]
    
    ##Scedual players
    #t = 0
    for player in players.values():
        battletime.addplayer(player, 0)
        #t+=1
    
    exitlist = []
    player_num = len(players)
    #This is to make end-of-battle cleaner
    run = True
    while run:
        ###Make players of this tick go
        print "Making choices"
        for player in battletime.players():
            #For each player
            if player.name not in exitlist:
                #If the player isn't killed (this is for end-of-battle errors)
                action = player.think(player, players)
                #Get his action
                #Call the player's thinker and give him info about the players.
                #If he is honest, he will only take as much as he should have.
                #He can store info in the player 'til the next time he is called
                print player.name, "has", action.name, "'d ", ', '.join(action.targets), "!"
                do_action(action)
                ####Rescedule- Must be worked out. Important
                battletime.addplayer(player, 1)
                
        ###Apply effects of this tick
        print 'Applying effects'
        for effect in battletime.effects():
            for target in effect.targets:
                for change in effect.changes.items():
                    players[target].stats[change[0]]+=change[1]
                    print target, "'s ", change[0], 'has changed by ', change[1]
            
            #For each change, apply the change to the target

        ##Check for exit conditions
        for player in players.keys():
            for exit in exits:
                if exit.condition(players[player]):
                    exit.effect(players[player], players)
                    del players[player]
                    exitlist.append(player)
                    player_num-=1
                    print "Someone exited. Players:", player_num
                    if player_num == 0:
                        run = False
                    #Handle player exit stuff and break if eavryone is dead.
                    
        ###next tick
        battletime.next_tick()

        
class Clock:
    """A timeline with a number of types of slot for each tick, and a pointer
    (E.g. each tick has a number of named list
    clock.add<listname>(item, time) sceduals item time ticks away from now
    clock.<listname>s() returns the list of items scedualed for this tick
    """

    def __init__(self, *args):
        self.tick = 0
        self.splits = {}
        for split in args: self.splits[split] = deque()

    def __getattr__(self, attr):
        if attr[:3] == "add":
            return lambda item, tick: self.add(attr[3:], item, tick)
            #Return a wrapper for the correct split add
            
        elif attr[-1] == 's':
            return lambda :self.get(attr[:-1])
            
        else:
            return self.splits[attr]
     
            

    def add(self, split, item, tick):
        tick+=self.tick
        s = split
        split = self.splits[split]
        l = len(split)-1
        #This accounts for the current tick
        if l<tick+1:
            #If the target tick is beyond our scope...
            for i in range(tick-l+1):
                split.extend([[]])
            #Extend just enough for it to be within our scope + 1
            #The incremnt is so that we don't crash when people stop scedualing
        split[tick].append(item)

    def get(self, split):
        return self.splits[split][self.tick]
        

    def next_tick(self):
        self.tick+=1
    
    
