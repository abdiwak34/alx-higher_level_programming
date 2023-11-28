#!/usr/bin/python3
for i in range(100):
    if i < 10:
        print("{}".format(str(i).zfill(2)), end = ", ")
    elif i == int(str(i)[::-1]) or i > int(str(i)[::-1]):
        continue
    else:
        print("{}".format(str(i).zfill(2)), end = ", ")
