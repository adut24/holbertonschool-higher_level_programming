#!/usr/bin/python3
"""
3-say_my_name.py module
This module is used to print the first name and last name of someone
Different tests will be performed
"""


def say_my_name(first_name, last_name=""):
    """
    print the name of someone
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
