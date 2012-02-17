import os, sys

find = sys.argv[1]
replace = sys.argv[2]

for folder in os.walk("."):
    for fname in folder[-1]:
        fname = folder[0] + "/" + fname
        if not input("Search in %s? " % fname):
            print("Searching", fname)
            with open(fname) as f:
                newtext = ""
                for n, line in enumerate(f):
                    if find in line:
                        if not input(str(n) + " " + line):
                            line.replace(find, replace)
                    newtext += line
                with open("~" + fname, "w") as copy:
                    copy.write(open(fname).read())
                with open(fname, "w") as newf:
                    newf.write(newtext)
