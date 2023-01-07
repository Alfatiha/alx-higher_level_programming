#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lst = int(repr(number) [-1])
cond1 = "and is greater than 5"
cond2 = "and is 0"
cond3 = "and is less than 6 and not 0"
print ("Last digit of", number, end='')
if lst > 5:
    print(" is", lst, cond1)
elif lst == 0:
    print(" is", lst, cond2)
elif lst < 6 and not 0:
    print(" is", lst, cond3)
