DEBUG = 0
GET_NAME = True
PREFIX = "###"


def info(*msg):
    if DEBUG >= 1:
        print(PREFIX, end="")
        print(*msg)


def at(loc):
    if DEBUG >= 1:
        print(PREFIX + "At %s" % loc)


def debug(*msg):
    if DEBUG >= 2:
        print(PREFIX, end="")
        print(*msg)
