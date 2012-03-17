import api
from api import Thinker
from lib.base.thinkers import pchoice


@api.Thinker
def smart_user(self):
    choices = 2
    choice = 0
    if len(self.being.location.beings) is 1:
        #if we are alone
        choice = 2
        act = self.being.act_dict["move"]
        choices = 3
    else:
        #we have company
        choice = 1
        acts = self.typed_acts["attack"]
    args = {}
    while choice < choices:
        if choice is 0:
            acts = pchoice(self.typed_acts, query="Type? ")
            choice += 1
        elif choice is 1:
            act = pchoice(acts, query="Action? ", back=True)
            if act is "back":
                choice -= 1
            else:
                choices += len(act.argsinfo)
                choice += 1
        elif choice > 1:
            arg, info = act.argsinfo[choice - 2]
            value = pchoice(eval(info), query=arg, back=True)
            if value is "back":
                choice -= 1
            else:
                args[arg] = value
                choice += 1
    return act.instance(**args)


user = smart_user
