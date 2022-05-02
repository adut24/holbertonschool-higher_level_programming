#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    res_list = [False, ]
    if my_list is None:
        return
    if my_list == []:
        return
    if my_list[0] % 2 == 0:
        res_list[0] = True
    for i in range(1, len(my_list)):
        if my_list[i] % 2 != 0:
            res_list.append(False)
        else:
            res_list.append(True)
    return res_list
