#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    if my_list == []:
        return None
    max = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] > max:
            max = my_list[i]
    return max
