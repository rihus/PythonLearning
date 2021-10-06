#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 13:40:20 2021

@author: riaz
"""

## Lists in Python
fruits = ['apple', 'banana', 'pineapple', 'mangoes', 'grapes']
for fruit in fruits:
    print("Here are fruits from list: " + fruit)

##range() function
for value in range(1,10,1):
    print(value)

##range() to make a list

numbers_list = list(range(0,20,2))
print(numbers_list)

## Cubes of a list with for loop and range()
cubes = []
for value in range(1,20):
    cube = value**3
    cubes.append(cube)

print("Here are the cubes of list: " + str(cubes))

##Same code written more concisely
cubes = []
for value in range(1,20):
    cubes.append(value**3)

print("Here are the cubes of list (concise code): " + str(cubes))

##Simple statistics with a list of number
digits_list = [0, 1, 3, 6, 8, 7, 12, 0, 16, 11, 12, 3, 13]
##minimum value in the list
min(digits_list)
##maximum value in the list
max(digits_list)
##sum of the all numbers in list
sum(digits_list)

##Tuple is a list of items that you can't modify using code i.e. they're immutable
tuple_example = ('apple', 'banana', 'car', 'dog')
print(tuple_example)
# ##Trying to change generates an error 
# tuple_example[0] = 'carrot'
# print(tuple_example)
# TypeError: 'tuple' object does not support item assignment
##but one can change list
list_example = ['apple', 'banana', 'car', 'dog']
print(list_example)
list_example[0] = 'carrot'
print(list_example)





