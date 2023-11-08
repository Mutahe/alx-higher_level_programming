#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for t in my_list:
        if t == search:
            new_list.append(replace)
        else:
            new_list.append(t)
        return new_list
