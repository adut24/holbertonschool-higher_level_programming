#!/usr/bin/python3
"""My_list module"""


class MyList(list):
    """MyList class"""
    def print_sorted(self):
        """print a list in sorted order"""
        print(sorted(self))
