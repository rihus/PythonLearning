# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 06:40:49 2021

@author: riazh
"""
##Practicing the user input examples and exercises

##Taking the simple user input
message_in=input("What is your name? ")
print("Hi " + message_in)

##Taking multi-line user input
prompt = "You should start with your name."
prompt += "\nWrite your first name: "
name_print=input(prompt)

print("\nHello " + name_print.title())

##Excercise
rent_car=input("Name of the car you want to rent: ")
print("Let us see if we can find " + rent_car + " car for you.")


dinner_guests = "How many people are you?"
dinner_guests += "\nPlease write the number: "
ding_num = input(dinner_guests)
ding_num = int(ding_num)

if ding_num >= 4:
    print("You'll have to wait a bit, I'm afraid!")
else:
    print("Very well, we'll get you a table immediately.")
    
###Telling if a user input is multiple of a digit
num_in = input("Write a number and I'll tell you if it's a multiple of ten: ")
num_in = int(num_in)

if num_in % 10 == 0:
    print("\nThe number is a multiple of 10.")
else:
    print("The number is not a multiple of 10.")