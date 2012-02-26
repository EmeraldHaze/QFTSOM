from api import rule, Rule

@rule('schedule')
def same(battle, being):
    "All the beings go at the same turn, with deaths being figured after everyone makes choices."
    battle.timeline.addbeing(being, 1)

@rule('schedule')
def next(battle, being):
    "Players go one after the other in a pre-determined order, with there actions having consequances immideatly."
    line = battle.timeline.being
    for tick in range(len(line)):
        try:
            go = (line[tick] == [] and line[tick+1] == [])
        except IndexError:
            go = (line[tick] == [])
        if go:
            break
            #This leaves tick at the first tick when there's a nobody
    battle.timeline.addbeing(being, tick - battle.timeline.tick)

@rule('schedule')
def speed(battle, being):
    "Players go their speed stat + last action's speed turns from now, these turns may overlap. Will error when speed is not defined."
    speed = being.stats["speed"]
    if being.last_act is not None:
        speed += being.last_act.data["speed"]
        print("{}'s {} has {} speed".format(being.name, being.last_act.name, speed))
    battle.timeline.addbeing(being, int(speed))

@rule('get_actions')
def get_all(battle, being):
    "Gets actions from both equipment and limbs. Should always work."
    being.actions = []
    being.act_dict = {}
    for actgiver in being.limbs + being.equiped:
        for action in actgiver.actions:
            try:
                name = actgiver.prefix + action.name
            except AttributeError:
                name = action.name
            being.actions.append(action)
            being.act_dict[name] = action

@rule('wipe_hist')
def wipe_normal(battle, being):
    "resets HP to MAXHP if such exists, and some internals. Should always work."
    if "MAXHP" in being.stats:
       being.stats["HP"] = being.stats["MAXHP"]
    being.actions = []
    being.status_list = []

@rule("wipe_hist")
def wipe_limbs(battle, being):
    "Resets HP to MAXHP per-limb. Only works when limb HP is defined."
    for limb in being.limbs:
        limb.data["HP"] = limb.data["MAXHP"]
    being.actions = []
    being.status_list = []
