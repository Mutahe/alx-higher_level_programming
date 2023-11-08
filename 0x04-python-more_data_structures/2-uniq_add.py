#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_ints = set()
    total = 0

    for t in my_list:
        if t not in uniq_ints:
            uniq_ints.add(t)
            total += t
    return total
