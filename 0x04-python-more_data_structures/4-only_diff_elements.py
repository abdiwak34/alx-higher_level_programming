#!/usr/bin/python3
def common_elements(set_1, set_2):
    a = [x for x in set_1 if x not in set_2]
    a += [y for y in set_2 if y not in set_1]
    return a
