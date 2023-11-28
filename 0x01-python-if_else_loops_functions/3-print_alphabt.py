#!/usr/bin/python3
a = ""
for i in range(ord('a'), ord('z') + 1):
    if chr(i) == 'q' or chr(i) == 'e':
        continue
    else:
        a += chr(i)
print(f"{a}", end = "")
