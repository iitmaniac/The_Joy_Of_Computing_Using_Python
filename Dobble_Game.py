# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 16:05:37 2019

@author: Shrikant Tambe
"""
import string
import random

symbols = []
symbols = list(string.ascii_letters)

card1 = [0] * 5
card2 = [0] * 5

pos1 = random.randint(0,4)
pos2 = random.randint(0,4)

samesymbol = random.choice(symbols)

if (pos1 == pos2):
    card1[pos1] = samesymbol
    card2[pos1] = samesymbol
    symbols.remove(samesymbol)

else:
    card1[pos1] = samesymbol
    card2[pos2] = samesymbol
    symbols.remove(samesymbol)
    
    card1[pos2] = random.choice(symbols)
    symbols.remove(card1[pos2])
    
    card2[pos1] = random.choice(symbols)
    symbols.remove(card2[pos1])

i = 0
while(i < 5):
    
    if(i != pos1 and i != pos2):
        ch = random.choice(symbols)
        card1[i] = ch
        symbols.remove(ch)
        
        ch = random.choice(symbols)
        card2[i] = ch
        symbols.remove(ch)
    
    i += 1


print("Find the common letter in the below given lists: ")
print(card1)
print(card2)

ans = input("")

if (ans == samesymbol):
    print("")
    print("Yes you are correct, the character '" + samesymbol + "' is common in both the lists!")
else:
    print("Oops! you are wrong, the character '" + samesymbol + "' is common in both the lists!")

