#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 22:47:35 2019

@author: sunbeam
"""

# We are performing some common operations on List in this program.

l1 = []     #Creating an empty list
print("This is list l1:",l1)
print()

#Creating a list.
l2 = ["Chetan", "Amit", "Komal", "Abhilash", "Rashmi", "Abhilash", "Shri", "Shrikant","Ajay","Emma"]
print("This is list l2:",l2)
print()

#Appending the list.
l2.append("Roshan")
l2.append("Shreya")
l2.append("Shubham")
l2.append("Rupam")


l3 = l2.copy()
l3.append("Sugandha")

print("This is the list l2 after appending and without sorting:",l2)
print()
print("This is the list l3 after appending and without sorting:",l3)
print()

#Sorting the list
l2.sort() #Sorting in ascending order.
print("This is list l2 after sorting:",l2)
print()
l3.sort(reverse=True) #sorting in desending order.
print("This is the list l3 after sorting in reverse/ desending order:")
print(l3)
print()

#Remove elements:
l2.pop()
print(l2)
print()
l2.remove("Shri")
print(l2)
print()
l2.remove("Abhilash")
print(l2)
print()
l2.remove("Abhilash")
print("This is list l2 after removing some values:",l2)
print()

#Inserting elements:
l1.append("Krunal")
l1.append("Kalyani")
l1.insert(1,"Kritika") #Inserting an element in the list at index 1
print("This is list l1 after appending some values:",l1)
print()

#Counting elements and length:
print(l3.count("Abhilash"))
print()
print("This is lenght of list l1:",len(l1))
print("This is lenght of list l2:",len(l2))
print("This is lenght of list l3:",len(l3))
print()

#Deletion of list l2:
del(l2)

#Slicing of list:
a = l3[2:8] #From index 2 to 7
b = l3[2:] #From index 2 to default end index
c = l3[:9]#From default start index to 8
d = l3[-11:-3] #from index -11 to -4
e = l3[-11:] #from index -11 to default end index
f = l3[:-3] #from default start index to -4
print("This is list l3:",l3)
print()
print("This is 'a', part of list l3 after slicing:",a)
print()
print("This is 'b', part of list l3 after slicing:",b)
print()
print("This is 'c', part of list l3 after slicing:",c)
print()
print("This is 'd', part of list l3 after slicing:",d)
print()
print("This is 'e', part of list l3 after slicing:",e)
print()
print("This is 'f', part of list l3 after slicing:",f)
print()

