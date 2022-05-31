#!/usr/bin/python3
"""add_item module"""
from sys import argv
from os.path import exists
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


file = 'add_item.json'
if not exists(file):
    save_to_json_file([], file)
if len != 1:
    a = load_from_json_file(file)
    for i in range(len(argv)):
        if i != 0:
            a.append(argv[i])
    save_to_json_file(a, file)
