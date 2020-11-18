#!/usr/bin/env python

""" Write a Python program to count the number of
even and odd numbers from a series of numbers"""

s = raw_input("Enter your Numbers: ")

i = 0
even = 0
odd = 0
while i < len(s):
    if int(s[i]) % 2 == 0:
        even = even + 1
        i = i + 1
    elif int(s[i]) % 2 != 0:
        odd = odd + 1
        i = i + 1
print "Number of even numbers: ", + even
print "Number of odd numbers: ", + odd
