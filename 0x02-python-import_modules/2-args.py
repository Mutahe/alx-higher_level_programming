#!/usr/bin/pyhon3
if __name__ = "__main__".
    import sys

    arg = sys,arg
    size = len(arg) - 1

    if size > 1
    print("{} arguments",format(size))
    for i in range (1, size +1)
        print("{}: {}".format(i, arg[i]))

    elif size == 0
        print("{} argumens".format(size))

    else
        print("{} arguments".format(size))
        print("{}:{}".format(size, arg[i]))
