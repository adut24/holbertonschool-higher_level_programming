#!/usr/bin/python3
if __name__ == "__main__":
    hidden = __import__('hidden_4')
    name = dir(hidden)
    i = 0
    while i < len(name):
        if name[i][0] != '_':
            print(name[i])
        i += 1
