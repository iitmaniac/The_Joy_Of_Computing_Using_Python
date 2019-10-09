# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 12:26:51 2019

@author: Shrikant Tambe
"""

import random

birthdays = []

i = 0
while(i <50):
    year = random.randint(1800, 2019)
    if (year%4 == 0 and year%100 != 0 or year%400 == 0):
        leap = 1
    else:
        leap = 0
    
    month = random.randint(1,12)
    if(month == 2 and leap == 0):
        days = 28
        dt = random.randint(1,28)
    elif(month == 2 and leap == 1):
        days = 29
        dt = random.randint(1,29)
    elif(month == 9 or month == 4 or month == 6 or month == 11):
        days = 30
        dt = random.randint(1,30)
    else:
        days = 31
        dt = random.randint(1,31)
    i += 1

    dob = str(dt) + "-" + str(month)
    birthdays.append(dob)

birthdays.sort
print(birthdays)
print("")

flag = 0
print("These dates share the birthdays of more than 1 person :")

dup = birthdays.copy()

for i in birthdays:
    dup.remove(i)
    
    for j in dup:
        if (i == j):
            print(i)
            flag = 1
print("")

if(flag != 1):
    print("Sorry! No two persons have the same birthday date and month.")
