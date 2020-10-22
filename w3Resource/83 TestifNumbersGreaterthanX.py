#!/usr/bin/env python

#Write a Python program to test whether all numbers of a list is greater than a certain number.

num = [1, 4, 5] #list of numbers
print str("This many items:"),(len(num))

print "Roll Call!"
if 4 in num:
    print str("yes 4 is here")

print "Height Check!!"
print str("Anyone taller than 10? "),(all(x > 10 for x in num))
print str("Okay anyone shorter than 10?"),(all(x < 10 for x in num))

#I don't really get why x calls the numbers from num but...
