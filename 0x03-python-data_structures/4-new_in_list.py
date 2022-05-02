#!/usr/bin/python3
from hashlib import new


def new_in_list(my_list, idx, element):
    new_list = my_list.copy()

    if idx < 0 or idx > len(my_list):
        return new_list

    for i in range(len(my_list)):
        if i == idx:
            new_list[i] = element
            return new_list
