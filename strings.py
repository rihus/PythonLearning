#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 6 10:33:22 2021

@author: riaz

"""

## A string is a series of characters. Anything inside a single quote ''
## or double quote is a string "". Few ways to use this flexibility:

string_one = 'I told my friend: "Come on!"'
string_two = "\nThe language 'Python' is named after Monty Python, not the snake."
string_three = "\nIn Python, \none's use of apostrophe works too"

print(string_one, string_two, string_three)

## As we saw we need to used different quotes in a single string.
## We can print multiple strings in same print command
## \n for new line, \t for tab, works in strings

## Changing case in a string
name = "jack reacher"
print("this is lower case name: " + name)
print("this is title case name: " +name.title())
print("this is upper case name: " +name.upper())
print("\tthis is again lower case name with a tab at start: " +name.lower())
## Clearly, print can combine two strings (and string with variables)
## This is called "concatenation"
print(string_one + " " + string_two)
##also
print("Title case string one follows: " + string_one.title())

## string.rstrip() is used to strip white spaces from the right end of a string
## string.rstrip() is used to strip white spaces from the left end of a string
## string.strip() is used to strip white spaces from both ends of a string

## These things are useful when we are taking user input in some program

## When concatenating strings with non-string values(e.g. digits), you must declare them as str()
granny_age = 100
granny_message = "Happy " + str(granny_age) + "th Birthday Grandma!"


