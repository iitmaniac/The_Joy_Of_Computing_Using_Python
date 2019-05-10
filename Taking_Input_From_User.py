# -*- coding: utf-8 -*-
"""
Created on Fri May 10 14:19:49 2019

@author: Shrikant Tambe
"""

print("Please fill the below given details before proceeding:")
name = input("What is your name? : ")
age = input("Please enter your age: ")
city = input("Please enter your city: ")
print()
print()
print()
print("Hello", name,". I hope life is treating you well!" )
print()
print()
print()
print("Please crossverify the details you have entered above!")
print("Your Name:", name)
print("Your Age:", age)
print("Your City:", city)
print()
response = input("Are above listed details correct?: ")
if response == "Yes" or response == "yes" or response =="YES" or response =="Yeah" or response =="YEAH" or response =="yeah" or response =="YA" or response =="ya" or response =="Ya":
    print("Thanks for your response! Have a nice day ahead. :)")
else:
    print("Please re-run the code again to register yourself. Sorry for the inconveniences!")
