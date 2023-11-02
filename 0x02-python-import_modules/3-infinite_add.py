#!/usr/bin/python3
def add_arg(argv):
    t = len(argv) - 1
    if t == 0:
        print("{}".format(t))
        return

    else:
        i = 1
        add = 0
        while i <= t:
            add += int(argv[i])
            i += 1
        print("{}".format(add))


if __name__ == "__main__":
    import sys
    add_arg(sys.argv)
