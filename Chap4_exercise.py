# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 11:19:18 2021

@author: riazh
"""

message0="numbers list up to 20 with for loop"
print(message0)

num_count=[]
for number in range(1, 21):
    print(number)
    num_count.append(number*3)
print(num_count)

message1="numbers list up to 1 million"
print(message1)

million_nums=list(range(1, 1000001))
print(million_nums)

message2="Even and Odd numbers list up to 20"
print(message2)

odd_nums=list(range(1,21,2))
print(odd_nums)

even_nums=list(range(2,21,2))
print(even_nums)

message3="Threes list up to 30"
print(message3)
three_nums=[]
for nums in range(1, 31):
    if nums % 3 == 0:
        print(nums)