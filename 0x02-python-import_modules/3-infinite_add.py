#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arglen = len(sys.argv) - 1
    sum = 0
    if arglen == 0:
        print(0)
    else:
        for i in range(1, len(sys.argv)):
            sum += int(sys.argv[i])
        print("{}".format(sum))
