#!/usr/bin/python3
"""stats module"""
import sys


def print_info(stats, size):
    """print the informations"""
    print("File size: {}".format(size))
    for k, v in sorted(stats.items()):
        if v:
            print("{}: {}".format(k, v))


def signal_handler(sig, frame):
    """called if Ctrl+C is pressed"""
    print_info(stats, size)


count = 0
size = 0
stats = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0,
         '405': 0, '500': 0}
try:
    for line in sys.stdin:
        count += 1
        line = line.split()[-2:]
        size += int(line[1])
        stats[line[0]] += 1
        if count % 10 == 0:
            print_info(stats, size)
    print_info(stats, size)
except KeyboardInterrupt:
    print_info(stats, size)
