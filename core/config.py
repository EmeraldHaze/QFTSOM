DEBUG = 0
ONLINE = False
PREFIX = "###"


def info(*msg):
    if DEBUG >= 1:
        print(PREFIX, end="")
        print(*msg)


def at(loc):
    if DEBUG >= 1:
        print(PREFIX + "at %s" % loc)


def debug(*msg):
    if DEBUG >= 2:
        print(PREFIX, end="")
        print(*msg)
