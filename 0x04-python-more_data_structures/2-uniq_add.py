#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_ints = set()
    for t in my_list:
        if t == uniq_ints:
            total = uniq_ints.add(t)
    return total
