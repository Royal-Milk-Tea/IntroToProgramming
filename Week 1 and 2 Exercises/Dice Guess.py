#!/usr/bin/env python
# -*- coding: cp1252 -*-

""" The program should do the following:

    Roll a pair of dice.
    Add the values of the roll.
    Ask the user to guess a number.
    Compare the user’s guess to the total value.
    Determine the winner (user or computer).
"""
from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input("Take a Guess: "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  guess = get_user_guess()

def max_val = number_of_sides*2
  print "The Maximum value is %d" %(max_val)
