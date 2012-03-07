DEBUG = 0
GET_NAME = True


prefix = "###"

def info(*msg):
    if DEBUG >= 1:
        print(prefix, end="")
        print(*msg)

def at(loc):
    if DEBUG >= 1:
        print(prefix + "At %s" % loc)

def debug(*msg):
    if DEBUG >= 2:
        print(prefix, end="")
        print(*msg)
