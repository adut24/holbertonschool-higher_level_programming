#!/usr/bin/python3
def no_c(my_string):
    i = 0
    new_string = ''
    while len(my_string) > i:
        if my_string[i] != 'c' and my_string[i] != 'C':
            new_string += chr(ord(my_string[i]))
        i += 1
    return new_string
