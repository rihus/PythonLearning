#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 16:09:09 2021

@author: riaz
"""

def favorite_book(title):
    """Display the favorite book after input"""
    print("One of my favorite book is:", title)

favorite_book('Jack Reacher')

def describe_pet(animal_type, pet_name):
    """Display info about a pet"""
    print("I would like to have a " + animal_type + " as a pet.")
    print("And I will name it " + pet_name + ".")

describe_pet("dog", "lotu")

describe_pet(animal_type="huskey dog", pet_name="motu")

def describe_city(city='Milan',country='Italy'):
    """
    Print the sentence with city name and country.
    Default: Milan, Italy
    """
    print(city + " is a city in " + country)

describe_city('Bologna', 'Italy')
describe_city()
describe_city('Islamabad', 'Pakistan')


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease write your name:")
    print("(enter 'q' at any time to quit!)")
    
    f_name = input("First name: ")
    if f_name == 'q':
        break
    
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")




