"""12/10/2020 Python Test -Birth year checker """
from astrosigns import zodiac

def birth_year (age, current_year):
    year = current_year - age
    print "You were born in %d" % (year)

birth_year (int(input("Enter your age: ")), int(input("Enter the current year: ")))



"""adj1 = raw_input("Enter an Adjective: ")
#age=int(input("What is your age?"))"""
""" Can I add something to tell you which zodiac animal you are? """

