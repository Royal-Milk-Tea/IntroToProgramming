#!/usr/bin/env python

""" Python conditional statements and loops
find those numbers which are divisible by 7 and multiple of 5,
between 1500 and 2700 (both included)"""

i = 1500
total = []

while i < 2700:
    if i % 7 == 0 and i % 5 == 0:
        total.append(i)
        i = i + 1
    else:
        i = i + 1
print total
    
