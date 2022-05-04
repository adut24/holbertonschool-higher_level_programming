#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max = 0
    best = ''
    for i in a_dictionary:
        if a_dictionary[i] > max:
            best = i
            max = a_dictionary[i]
    return best
