#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    a = {x for x in my_list}
    for x in a:
        res += x
    return res


