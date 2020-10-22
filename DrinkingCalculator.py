#!/usr/bin/env python

def yikes(year):
    print year % 400 == 0 or year % 4 == 0 and year % 100 != 0

year = (int(input("")))
yikes(year)
