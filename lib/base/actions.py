from api import Action, ActionFactory
from random import randint


@ActionFactory
def simplemaker(name, dmg):
    def sexec(self):
        target = self.targets[0]
        print(target.name, "has lost", dmg, "health!")
        target.stats["HP"] -= dmg
    return Action(name, {"exec": sexec, "delay": 0})


def complete_exec(self):
    rules = self.dmgrules
    if "status" in self.data:
        status = self.data["status"].instance(
            self.targets[0],
            self.battle,
            **self.data["status_data"]
        )
        self.targets[0].status_list.append(status)
    for target in self.targets:
        dmg = eval(rules[self.data["type"]])
        target.stats["HP"] -= dmg
        print(target.name, "lost", dmg, "health!")


def manainit(self):
    self.actor.stats['MP'] -= self.data["MPC"]


def basic_choosen(action):
    print("{} has {}'d {}!".format(
                        action.actor.name,
                        action.name,
                        ', '.join([target.name for target in action.targets])
                    )
                )


def move_exec(self):
    being = self.actor
    dest = self.args["dest"]
    loc = being.location
    if dest in loc.linked:
        loc.beings.remove(being)
        dest.beings.append(being)
        being.loc = dest
        print(being.name, "has moved too", dest.name)
        print(dest.info)

move = Action(
    "move",
    {"exec": move_exec, "choosen": lambda a: None},
    {"speed": 1},
    min_targets=0,
    max_targets=0
)

null = Action(
    "pass",
    {
        "exec": (lambda self: print("%s does nothing." % self.actor.name)),
        "choosen": (lambda self: print("%s passes." % self.actor.name))
    },
    {"speed": 0},
    min_targets=0,
    max_targets=0
)
