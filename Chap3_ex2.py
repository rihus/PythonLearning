# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 12:21:13 2021

@author: riazh
"""

Guests=['Naeem','Feynman','Teresa','Amber']

print("Guest list is:" + "\n \t" + Guests[0] + "\n \t" + Guests[1] + "\n \t" + Guests[2] + "\n \t" + Guests[-1])

print("Please have dinner with me " + Guests[0] + " and " + Guests[1])

print("\nUnfortunately " + Guests[1] + " can't make it cos he's dead lol")
#Guests.remove("Feynman")
Guests.insert(1, "Saleem")
Guests.append("Abrar")
print("New guests are:\n")
print(Guests)

Guests.pop(-1)

print(Guests)

del Guests[2]

print(Guests)

