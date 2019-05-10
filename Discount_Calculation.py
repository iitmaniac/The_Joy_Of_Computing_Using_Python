# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:10:58 2019

@author: Shrikant Tambe
"""

#This code will calculate the discounted amount of the total given cost.

name = input("Please enter your name: ")
print()
print("Hi", name, ". I hope you are doing well!")
print()
sp = input("Please enter the Final price of the product: ")
multipleproducts = input("Please enter the total quantity of the product: ")
offer = input("Please enter the total discout, you have got for that product: ")


totalsp = float(sp) * float(multipleproducts)
totaldiscount = float(offer) / 100 * float(totalsp)
totalbilling = float(totalsp - totaldiscount)

print()
print()
print("********************************INVOICE**********************************")
print("Total Selling Price of the products : Rs.",totalsp)
print("Total Discount: Rs.",totaldiscount)
print("Total Billing: Rs.",totalbilling)
print()
print()
print("Congratulations! You have saved Rs.",totaldiscount," on your purchasing.")
print("Thanks for visiting the store. Hope to see you again!")
print("*************************************************************************")
