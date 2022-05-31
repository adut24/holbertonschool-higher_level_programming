#!/usr/bin/python3
"""stats module"""
import sys


count = 0
size = 0
stats = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0,
         '405': 0, '500': 0}

try:
    for line in sys.stdin:
        count += 1
        line = line.split()[-2:]
        if line[0] in stats:
            stats[line[0]] += 1
        size += int(line[1])
        if count % 10 == 0:
            print(f"File size: {size}")
            for k, v in sorted(stats.items()):
                if v:
                    print(f"{k}: {v}")
except KeyboardInterrupt:
    print(f"File size: {size}")
    for k, v in sorted(stats.items()):
        if v:
            print(f"{k}: {v}")
