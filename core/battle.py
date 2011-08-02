from collections import deque


def start(people, exits, mods):
    players, trigs = ({},)*2
    #trigs is the trigger stack. It will be used by do_action.
    for person in people: players[person.name] = person
    #Fill up players dict with name:person
    battletime = clock('player', 'effect')
    
    ###Generate player action lists
    for player in players.values():
        for belong in player.belongs.values(): player.actions.extend(belong.actions)
    
    ##Scedual players
    t = 0
    for player in players.values():
        battletime.addplayer(player, t)
        t+=1
        
        
    while 1:
        ###Make players of this tick go
        for player in battletime.players():
            #For each player
            action = player.think(player, players)
            #Get his action
            #Calls the thinker of a player and supply him with info about the players.
            #If he is honest, he will only take as much as he should have.
            #He can store info in the player untill the next time he is caleld
            print player.name, "has done ", action.name+"!"
            do_action(action)
            ####Rescedule- Must be worked out. Important
            battletime.addplayer(player, 2)
            
        ###Apply effects of this tick
        for effect in battletime.effects():
            target, changes = effect
            for change in changes.items():
                players[target].stats[change[0]]+=change[1]
                print target, "'s ", change[0], 'has changed by ', change[1]
            
            #For each change, apply the change to the target

        ##Check for exit conditions
        for player in players.keys():
            for exit in exits:
                if exit.condition(players[player]):
                    exit.effect(players[player], players)
                    del players[player]
        ###next tick
        battletime.tick()

def do_action(action):
    global battletime
    for effect in action.effects: battletime.addeffect((effect, action.targettarget), tick)

    
class clock:
    """A scrolling timeline with a nuber of types of slot for each tick.
    (E.g. each tick has a number of named list
    clock.add<listname>(item) assumes that item[0] is how many ticks away to secedual that item
    clock.add<listname>(item, time) sceduals item time ticks away from now
    clock.<listname>s() returns the list of items scedualed for this tick
    """

    def __init__(self, *args):
        self.splits = {}
        for split in args: self.splits[split] = deque()

    def __getattr__(self, attr):
        if attr[:3] == "add":
            return lambda item, tick = None: self.add(attr[3:], item, tick)
            #Return a wrapper for the correct split add
            
        elif attr[-1] == 's':
            return lambda :self.get(attr[:-1])
        else:
            return self.splits[attr]              
            

    def add(self, split, item, tick = None):
        if tick is None: tick, item = item[0], item[1:]
        #If we don't have the tick, extract the tick
        split = self.splits[split]
        l = len(split)-1
        #This accounts for the current tick
        if l<tick:
            #If the target tick is beyond our scope...
            split.extend([[]]*(tick-l))
            #Extend just enough for it to be within our scope (extend with blank lists)
        split[tick].append(item)

    def get(self, split):
        return self.splits[split][0]

    def tick(self):
        for split in self.splits.items():
            #For each dequeue
            split.popleft()
            #Pop the first item, hence ticking

