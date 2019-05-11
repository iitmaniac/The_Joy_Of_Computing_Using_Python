#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 18:06:59 2019

@author: sunbeam
"""
#This program asks user to enter the number for which user likes to see the multiplication table.

name = input("Please enter your name! \n")
print()
print()
print("Hello, "+name+". Hope you are doing well!")
print()
table = float(input("Please enter the number for which you would like to see the multiplication table.\n"))
multiples = int(input("Please enter the total number of non-zero, 'positive whole multiples' you want to see in the table.\n"))
print()
if multiples > 0:
    print("Please find your desired multiplication table for",table,"as: ")
    for i in range(1, multiples+1):
        print(table,"X",i,"=",i*(table))
    print()
    print()
    print("Thanks for using this service!")
else:
    print("Please enter the non-zero, positive whole number for multiples.")
    print("Kindly re-run the program for using the service. Sorry for inconvinences!")
