#!/usr/bin/python3
def common_elements(set_1, set_2):
    set_common = set()
    for t in set_1:
        if t in set_2:
            set_common.add(t)
    return set_common
