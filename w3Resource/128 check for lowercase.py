#!/usr/bin/env python#

#128. Write a Python program to check whether lowercase letters exist in a string.
#w3resource 22/10/2020

s = (raw_input(""))

print (any(s.islower() for x in s)) 
