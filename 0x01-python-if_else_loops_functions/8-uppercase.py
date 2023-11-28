#!/usr/bin/python3
def uppercase(str):
    A = ""
    for i in str:
        if i >= 'a' and i <= 'z':
            A += chr(ord(i) - ord('a') + ord('A'))
        else:
            A += i
    print("{}".format(A))
