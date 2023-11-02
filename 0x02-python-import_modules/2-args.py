#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    size = len(args)

    if size > 1:
        print("{} arguments".format(size))
        for i in range(size):
            print("{}: {}".format(i, args[i]))
    elif size == 1:
        print("{} arguments".format(size))
        print("1: {}".format(args[0]))
    else:
        print("No arguments")
