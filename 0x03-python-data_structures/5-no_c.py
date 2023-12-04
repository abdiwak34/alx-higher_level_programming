#!/usr/bin/env python3
def no_c_list(my_string):
    new_list = [char for char in my_string if char.lower() not in {'c', 'C'}]
    return new_list
