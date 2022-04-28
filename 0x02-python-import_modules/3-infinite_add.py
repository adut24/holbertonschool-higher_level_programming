#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nb = len(sys.argv)
    i = 1
    res = 0
    while i < nb:
        res += int(sys.argv[i])
        i += 1
    print("{:d}".format(res))
