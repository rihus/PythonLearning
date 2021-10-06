#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 6 11:39:44 2021

@author: riaz
"""
## For and if loops 
cities = ['Torino', 'Milano', 'Venezia', 'Bolzano', 'Trieste', 
          'Aosta', 'Genova', 'Roma', 'Firenze', 'Cinque_Terre']
##if conditional with == (equal to)
for city in cities:
    if city == 'Cinque_Terre':
        print("I still need to visit " + city.upper())
    else:
        print("I have been to: "+city.title())

countries = ['Italy', 'Usa', 'japan', 'New zealand', 'Mexico', 'South africa']
##if conditional with != (not equal to)
for country in countries:
    if country != 'Italy':
        print('I want to visit ' + country.upper())
    else:
        print("Its been nice but now is time to leave: "+country)

##Multiple conditionals with == (equal), less than (<), greater than (>)


ages = ['27', '35', '66', '2']

for age in ages:
    if ages[0] < ages[1] and ages[2] < ages[1]:
        print('ages make sense')
    elif age == '2':
        print(str(age) + " This could be their son")
    else:
        print("I don't know")

## Using both for and if loops together

available_toppings = ['mushrooms', 'green peppers', 'extra cheese', 'fries',
                      'chicken', 'olives']

requested_toppings = ['mushrooms', 'pineapple', 'extra cheese', 'fries', 'olives']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else: 
        print("Sorry, this is Italy, we don't put: "+ requested_topping +" on pizza.")

print("Finished making your pizza")