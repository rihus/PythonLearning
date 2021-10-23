#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 16:20:14 2021

@author: riaz
"""
# ##My excercize with WHILE LOOP
# ## While loop runs as long as (or while) a certain condition is true.

import time

##This will print numbers from 1 to 15 
current_number = 1
while current_number <= 15:
    print(current_number)
    current_number += 1

##This loop will go on until you write 'quit'. Using break in while
message_in = "\nAsk me any question and no answer will be given"
message_in += "\n Write quit when tired. \n"
while True:
    message_loop = input(message_in)
    if message_loop == 'quit':
        print("\nOh... you killed me!")
        break
    else:
        print("I have no idea!")

##Using continue in while loop...
##it tells the loop to ignore the rest of the loop and return to beginning 
my_number = 0
while my_number < 20:
    my_number +=  1
    if my_number % 2 == 0:
        continue    
    print(my_number)

##Pizza toppings 
toppings = "What toppings you'd like on your pizza? \n"
toppings += "Enter exit, when finished.\n"
toppings_list = ""
while toppings_list != 'exit':
    toppings_list = input(toppings)
    if toppings_list != 'exit':
        print("Okay, " + toppings_list.upper() + " will be added.")

##Movie tickets
question_in = "Enter the age of person for cinema ticket one at a time.\n"
question_in += "Enter done when finished.\n"
q_store = ""
while q_store != 'done': 
      question_1 = input(question_in)
      if question_1.isdigit():
         print("\nOkay. Please wait!\n")
         time.sleep(2)
      elif question_1 == 'done':
         break
      else:
         print("\nPlease enter the number only!")
         continue
      if int(question_1) <= 3:
          print("\nCongrats! The ticket is free!") 
      elif int(question_1) > 3 and int(question_1) <= 12:
              print("\nTicket price is 10€") 
      else: 
           print("Ticket price is 15€")










