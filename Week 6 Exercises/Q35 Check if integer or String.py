#!/usr/bin/env python

""" Write a Python program that accepts
a string and calculate the number of digits and letters """

s = raw_input("Type Something: ")
s = s.replace(" ","") #removes whitespace
i = 0
digit = 0
stringy = 0
while i < len(s):
    if len(s) < 1:
        print "input a valid text"
    else:
        if s[i].isdigit():
            digit = digit + 1
            i = i + 1
        elif s[i].isalpha():
            stringy = stringy + 1
            i = i + 1
print "Number of Digits: ", + digit
print "Number of Letters: ", + stringy
