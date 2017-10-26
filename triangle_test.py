#!/usr/bin/env python
"""
Write a Python program to check a triangle is valid or not.
Expected Output:
Input the length of side1: 5                                            
Input the length of side2: 4                                            
Input the length of side3: 6                                            
The triangle is valid
"""

side1 = int(raw_input("Input the length of side1: "))
side2 = int(raw_input("Input the length of side2: "))
side3 = int(raw_input("Input the length of side3: "))

if ( side1 + side2 > side3 ) and ( side2 + side3 > side1 ) and ( side3 + side1 > side2 ):
    print "Your triangle is valid"
else:
    print "your triangle is invalid"
