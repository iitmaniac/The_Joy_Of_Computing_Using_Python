# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 15:58:04 2019

@author: Shrikant Tambe
"""

def magic_square(n):
    
    magicsquare = []
    
    for i in range(n):
        l = []
        for j in range(n):
            l.append(0)
        magicsquare.append(l)
        
    i = n//2
    j = n-1
    
    num = n*n
    count = 1
    
    while(count <= num):
        if(i == -1 and j == n):
            i = 0
            j = n-2
        
        else: 
            if(i == -1):
                i = n-1
            if(j == n):
                j = 0
        
        if(magicsquare[i][j] != 0):
            i = i+1
            j = j-2
            continue
        else:
            magicsquare[i][j] = count
            count += 1
        
        i = i-1
        j = j+1
        
    print("The Magic Square for Number " + str(n) + " is given as below: ")
    for i in range(n):
        for j in range(n):
            print(magicsquare[i][j], end = ' ')
        print("")
    
    print("The sum of Diagonal / Row / Column in a Magic Square is: " + str(n*(n**2 + 1)/2))
    
magic_square(3)