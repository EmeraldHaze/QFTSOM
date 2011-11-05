import types
def copy(target, source, *copys):
    for name in copys:
        value = getattr(source, name)
        if type(value) in [str, dict, list]:
            value = type(value)(value)
            #This makes a copy
        setattr(target, name, value)