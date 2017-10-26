#!/usr/bin/env python
"""
Write a Python program to find numbers between 100 and 400 (both included) 
where each digit of a number is an even number. 
The numbers obtained should be printed in a comma-separated sequence
"""

#y = []
y = ""

for x in range(100,401) :
    if x % 2 == 0 :
        for z in str(x):
            if int(z) % 2 != 0:
                break
        else:
            #y.append(x)
            y = y + str(x) + ','
print y

