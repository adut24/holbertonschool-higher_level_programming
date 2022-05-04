#!/usr/bin/python3
def common_elements(set_1, set_2):
    len1 = len(set_1)
    len2 = len(set_2)
    new_set = set({})
    item1 = next(iter(set_1))
    item2 = next(iter(set_2))

    if len1 < len2:
        for i in range(len2):
            if item1 == item2:
                new_set.add(item1)
            item1 = next(iter(set_1))
            item2 = next(iter(set_2))
    else:
        for i in range(len1):
            if item1 == item2:
                new_set.add(item1)
            item1 = next(iter(set_1))
            item2 = next(iter(set_2))
    return new_set
