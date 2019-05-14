# -*- coding: utf-8 -*-
"""
Created on Tue May 14 10:13:11 2019

@author: Shrikant Tambe
"""

#Here we are writing the function for famous Fizz-Buzz puzzle for the given set of numbers and displaying the output for the given input values by the end users.

def fizzbuzz(ran):                      # Writing a function and accepting the input range in the function from the user.
    for i in range(1,ran+1):
        if (i % 3 == 0) and (i % 5 == 0): #Checking conditions for Fizz, Buzz or Fizz-Buzz inside a for loop.
            print(i,"is a Fizz-Buzz!")
        elif (i % 3 == 0):
            print(i, "is a Fizz.")
        elif (i % 5 == 0):
            print(i, "is a Buzz.")
        else:
            print(i, "is neither a Fizz nor a Buzz and not even a Fizz-Buzz.")


name = input("Please enter your name. \n") #Taking inputs from the user.
print()
print("Hope you are doing good,",name,"!")
print()
num = int(input("Please enter the number upto which you want to find the Fizz Buzz puzzle. \n")) #Taking range inputs from the user for which we have to display the Fizz Buzz Puzzle.
print()
print("Your Fizz-Buzz Puzzle for",num,"numbers are as printed below: ")
print()
fizzbuzz(num)
print()
print("Thanks for using this service. Hope to see you again!")