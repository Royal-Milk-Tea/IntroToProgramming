#!/usr/bin/env python

def candy (sweets, children):
    sweets_per_child= children/sweets
    print "Give the children %d" %(sweets_per_child)
    if sweets_per_child <= 5:
        print "But don't give them a toothache"
    elif sweets_per_child >= 10:
        print "...and call the dentist =/"
    

candy (int(input("Enter how many children: ")), int(input("Enter how many sweets there are: ")))
