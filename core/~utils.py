import types


def copy(target, source, *tocopy):
    """
    Copies attributes listed in tocopy from source to target, making new
    instances of str, dict, list objects
    """
    for attr in tocopy:
        value = getattr(source, attr)
        if type(value) in [str, dict, list]:
            value = type(value)(value)
            #This makes a new object with the same content
        setattr(target, attr, value)
