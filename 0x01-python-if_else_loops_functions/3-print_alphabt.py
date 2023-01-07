#!/usr/bin/python3
for ch in range(97, 123):
    if ch == 101:
        continue
    elif ch == 113:
        continue
    print("{0:s}".format(chr(ch)), end='')
