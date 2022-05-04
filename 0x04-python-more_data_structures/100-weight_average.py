#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    av = 0
    div = 0
    for i in range(len(my_list)):
        av += my_list[i][0] * my_list[i][1]
        div += my_list[i][1]
    av /= div
    return av
