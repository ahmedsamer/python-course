#!/usr/bin/env python

digits = []
upper = []
lower = []
special = []

password = raw_input("\nPlease enter your password: ")

for x in password :
    if x.isdigit():
        digits.append(x)
    elif x.isupper():
        upper.append(x)
    elif x.islower():
        lower.append(x)
    elif x in '$' '#' '@':
        special.append(x)
    else:
        print "Error: This script accespt only [Upper], [Lower] and ['$', '#', '@'']\n"
        exit(0)


if len(password) < 6 :
    print "Error: Password requires at least 6 character\n"
elif len(password) > 16 :
    print "Error: Password maximum required 16 character\n"
elif len(digits) == 0 or len(upper) == 0 or len(lower) == 0 or len(special) == 0:
    print "Error: Password must contain 1 upper 1 lower 1 special character ['$' '#' '@]\n"
else:
    print "\'%s\' Is a valid password\n" % password
