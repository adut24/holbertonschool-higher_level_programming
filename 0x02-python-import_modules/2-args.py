#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nb = len(sys.argv)
    i = 1
    if nb == 1:
        print("0 arguments.")
    else:
        if nb == 2:
            print("{:d} argument:".format(nb - 1))
        else:
            print("{:d} arguments:".format(nb - 1))
        while i < nb:
            print("{:d}: {:s}".format(i, sys.argv[i]))
            i += 1
