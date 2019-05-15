# -*- coding: utf-8 -*-
"""
Created on Wed May 15 11:51:04 2019

@author: Shrikant Tambe
"""
"""
Here we are developing a game to find the answer of the jumbled word. 
Here we are taking an input from user, and checks with the solution of the jumbled word. 
If it is correct then a point is added to the player's score. Same goes with another player.
This keeps on happening until they wish to play the game.

"""

import random

def choose():
    dictionary = ['Literally','Irregardless','Whom', 'Colonel', 'Nonplussed', 'Disinterested', 'Enormity', 'Lieutenant', 'Unabashed']
    selected = random.choice(dictionary)
    return selected

def jumble(correctword):
    jumbledword="".join(random.sample(correctword,len(correctword)))
    return jumbledword

def thanks(a1,a2,b1,b2):
    print(a1 + " your total score is: " + str(b1) +" and " + a2 + " your total score is: " + str(b2))
    print()
    print()
    if(b1 > b2):
        print("Congratulations! " + a1 + " is the winner.")
        print("Thank you for playing. Hope to see you soon!")
    elif (b1 == b2):
        print("This is a tie! Match is Draw.")
        print("Thank you for playing. Hope to see you soon!")
    else:
        print("Congratulations! " + a2 + " is the winner.")
        print("Thank you for playing. Hope to see you soon!")
        
def play():
    p1 = input("Player 1, Please enter your name.\n")
    print()
    p2 = input("Player 2, Please enter your name.\n")
    print()
    print()
    print()
    print("*" * 20)
    point1 = 0
    point2 = 0
    turn = 0
    chance = 1
    while(chance == 1):
        if(turn % 2 == 0):
            print()
            print("Your chance,",p1)
            print()
            word = choose()
            jumbled = jumble(word)
            print(jumbled)
            guess = input("Hey! Guess the original word: \n")
            if(guess == word):
                point1 = point1 + 1
                print()
                print("Congratulations! Correct answer. Your total score is:", point1)
                print()
                print("*" * 20)
            else:
                print()
                print("Incorrect Answer! The correct answer was " + word)
                print()
                print("*" * 20)
                
        else:
            print()
            print("Your chance,",p2)
            print()
            word = choose()
            jumbled = jumble(word)
            print(jumbled)
            guess = input("Hey! Guess the original word: \n")
            if(guess == word):
                point2 = point2 + 1
                print("Congratulations! Correct answer. Your total score is:", point1)
                print()
                print("*" * 20)
                
            else:
                print("Incorrect Answer! The correct answer was " + word)
                print()
                print("*" * 20)      
        
        turn = turn + 1
#        print()
#        print()         
        
        
        chance = int(input("Do you want to Continue the game? Press '0' to exit and Press '1' to continue. \n"))
        print()
        print("$" * 20)
        
        if(chance == 0):
            print()
            print()
            chance = 0
            thanks(p1,p2,point1,point2)
            print()
            print("#" * 20)
            break
       

play()       
       
       
       