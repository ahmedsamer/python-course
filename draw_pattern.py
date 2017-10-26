#!/usr/bin/env python
"""
Ex1: Write a Python program to construct the following pattern, using a nested loop number.
Expected Output:

1
22
333
4444
55555
666666
7777777
88888888
999999999
"""
#n = raw_input("enter the number of pattern: ")
#for i in range(0, int(n)):
#    print(str(i) * i)

n = 0
num_to_count_to = raw_input("Please enter the number to count to: ")

if num_to_count_to.isdigit():
    print ""
else:
    print "Please enter a valid number."
    exit(1)

for x in range(0, int(num_to_count_to)):
    print str(x) * n
    n = n + 1