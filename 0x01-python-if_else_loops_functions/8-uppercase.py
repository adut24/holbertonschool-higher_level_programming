#!/usr/bin/python3
def uppercase(str):
    i=0
    ch=''
    while len(str)>i:
        if str[i]>='a' and str[i]<='z' :
            ch+=chr(ord(str[i])-32)
        else:
            ch += chr(ord(str[i]))
        i+=1
    print("{:s}".format(ch))
