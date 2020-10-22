#!/usr/bin/env python
"""21/10/2020
My very funny prefix script. Turns out Sarah and Steve got removed from youtube so now I look mad but sure whatever"""

print "Ive always been fascinated by the tallaght prefix: CH chnow what I mean?"

tallaght = 'ch'

story = raw_input('Story Lad? ')
                  
if len(story) >0 and story.isalpha():
    word = story.lower()
    start = word[1:len(story)]
    tallaghTastic = tallaght + start
    print tallaghTastic
else:
    print 'Whats the craic lad?' 
                  
