#!/usr/bin/python3
"""stats module"""
import fileinput
import signal
import sys


def print_info(stats, size):
    print(f"File size: {size}")
    for k, v in stats.items():
        if v != 0:
            print(f"{k}: {v}")

def signal_handler(sig, frame):
    print_info(stats, size)
    sys.exit(0)

count = 0
size = 0
stats = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, \
    '405': 0, '500': 0}
for line in fileinput.input():
    count += 1
    line = line.split()[-2:]
    size += int(line[1])
    value = stats.get(line[0])
    value += 1
    stats.update({line[0]: value})
    if count % 10 == 0:
        print_info(stats, size)
    signal.signal(signal.SIGINT, signal_handler)
