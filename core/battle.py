from collections import deque


def start(people, exits, mods):
    players, trigs = ({},)*2
    #trigs is the trigger stack. It will be used by do_action.
    for person in people: players[person.name] = person
    #Fill up players dict with name:person
    
    battletime = clock('player', 'effect', 'actions')(
    
    while 1:
        ###Make players of this tick go
        for player in battletime.players():
            #For each player
            action = player.think(players)
            #Get his action
            #Calls the thinker of a player and supply him with info about the players.
            #If he is honest, he will only take as much as he should have.
            #He can store info in the player untill the next time he is caleld
            #Actions are ussally lists of tuples of this form:
            #Trigger(s)*, None, Time, Target, Effect
            #If there is a non-recurisve trigger present, then it will be
            #Trigger, None, Time, Target, Effect
            do_action(action)
            ####Rescedule- Must be worked out. Important
            
        ###Apply effects of this tick
        for effect in battletime.effects():
            target, stat, change = effect
            players[target].stats[stat]+=change

        ###Apply actions of this tick
        for action in battletime.actions(): do_action(action)

        ##Check for exit conditions
        for player in players.keys():
            for exit in exits:
                if exit.condition(players[player]):
                    exit.effect(players[player])
                    del players[player]
        ###next tick
        battletime.tick()

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
            global battletime
            battletime.addeffect(effect)
            #Add the event. addevent puts it event[0] ticks away from now.
    
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
        if not tick: tick, item = item[0], item[1:]
        #If we don't have the tick, extract the tick
        split = self.splits[split]
        l = len(split)
        if l>tick:
            #If the target tick is beyond our scope...
            split.extend([[]]*tick-l)
            #Extend just enough for it to be within our scope (extend with blank lists)
        split[tick].append(item)

    def get(self, split):
        return self.splits[split][0]

    def tick(self):
        for split in self.splits.items():
            #For each dequeue
            split.popleft()
            #Pop the first item, hence ticking

