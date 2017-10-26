#!/usr/bin/env python

"""
Ex2:
Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.

lucky_sum(1, 2, 3) = 6
lucky_sum(1, 2, 13) = 3
lucky_sum(1, 13, 3) = 1
"""

a = int(raw_input("Please enter the first number: "))
b = int(raw_input("Please enter the second number: "))
c = int(raw_input("Please enter the third number: "))

if a == 13:
    a, b, c = 0, 0, 0
elif b == 13:
    b, c = 0, 0
elif c == 13:
    c = 0

print a + b + c