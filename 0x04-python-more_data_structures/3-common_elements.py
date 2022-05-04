#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_set = set({})
    it1 = iter(set_1)

    for i in set_1:
        item1 = next(it1)
        it2 = iter(set_2)
        for j in set_2:
            item2 = next(it2)
            if item1 == item2:
                new_set.add(item1)
    return new_set
