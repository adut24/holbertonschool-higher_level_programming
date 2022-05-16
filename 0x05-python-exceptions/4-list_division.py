#!/usr/bin/python3
from decimal import DivisionByZero
from hashlib import new


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):
        res = 0
        try:
            res = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            new_list.append(res)
    return new_list
