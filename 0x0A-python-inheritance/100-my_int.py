#!/usr/bin/python3
"""my_int module"""


class MyInt(int):
    """MyInt class"""
    def __init__(self, value):
        """constructor method"""
        self.__value = value

    def __eq__(self, value):
        """verify if equal"""
        return self.__value != value

    def __ne__(self, value):
        """verify if not equal"""
        return self.__value == value
