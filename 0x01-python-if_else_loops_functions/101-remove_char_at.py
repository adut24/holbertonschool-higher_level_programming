#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    ch = ''

    if n < 0:
        return str

    while len(str) > i:
        if i == n:
            i += 1
        ch += chr(ord(str[i]))
        i += 1
    return ch
