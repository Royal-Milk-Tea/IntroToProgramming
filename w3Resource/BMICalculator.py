#!/usr/bin/env python
# 66.  Calculate body mass index
#BMI = kg/m2
#Added print options to practice classifications again

w = (float(input("Input Weight in kg: "))) #weight
h = (float(input("Input Height in meters: "))) #height

n = round(w / (h * h), 2)

print "underweight: ", n <= 18.5
print "normal weight", 18.6 <= n <= 24.9
print "overweight", 25.0 <= n <= 29.9
print "obesity class I", 30.0 <= n <= 34.9
print "obesity class II", 35.0 <= n <= 39.9
print "obesity class III",  40.0 <= n
print "don't worry bmi doesn't handle exceptional people very well"
