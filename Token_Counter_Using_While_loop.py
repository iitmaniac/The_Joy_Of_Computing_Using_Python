#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 20:31:21 2019

@author: sunbeam
"""
# This program simply increments the counter value but by using while loop.

print("Greetings to all! We are starting now...")
print()
print()
n = 1
c = "Yes"
while(c == "Yes" or c=="YES" or c== "yes" or c== "Y" or c=="y" or c=="Ya" or c=="YA" or c=="ya" or c=="Yep" or c=="YEP" or c=="yep" or c== "Yeah" or c=="YEAH" or c=="yeah"):
    print()
    print("Token number "+str(n)+", may come please!")
    c = input("Is there next token present?(Yes or No) \n")
    n = n+1
print()
print("We are closed now...Thank you for the day!")