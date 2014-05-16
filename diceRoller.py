'''
Die roll program

This program simulates the roll of a die.
It generates a random number from a range of 6,
with each number corresponding to a side on the die.
It then displays this side.
It could be used in simulated board games, adapted for dungeons and dragons
or used with an actual board game.
The added meny allows you to select one of the tasks set.'''


import random #To simulate the die
import time #To allow a better user appeal

#To hold the displays for the dies sides
#The 'O's were spaced for the font I use on idle
dieSides= ["- - - - -\n|         |\n|   O   |\n|         |\n- - - - -\n",
           "- - - - -\n|O      |\n|         |\n|      O|\n- - - - -\n",
           "- - - - -\n|O      |\n|   O   |\n|      O|\n- - - - -\n",
           "- - - - -\n|O   O|\n|        |\n|O   O|\n- - - - -\n",
           "- - - - -\n|O   O|\n|   O   |\n|O   O|\n- - - - -\n",
           "- - - - -\n|O   O|\n|O   O|\n|O   O|\n- - - - -\n"]

#Asks if you want to roll the die, and then considers yuor answer
def decideToRoll():

    while True:
        choice = input("Do you want to roll the die? \n")

        if choice.lower() == "yes" or choice.lower() == "y":
            dieValue = roll()
            return dieValue #So roll can be used in the main game
        
        elif choice.lower() == "no" or choice.lower() == "n":
            return
        
        else:
            print("That input is not understood!\n")
            
def roll():
    print("Rolling.....") #Tell the user

    #Creates a random number from 0 to 5, a range of 6 (lists start at 0)
    dieValue = random.randint(0,5)
    return dieValue #So dieValue can be used in the main game     

def showDie(roll):
    print(dieSides[roll]) #Selects the corect side from the list
    
def menu(): #To allow a set task to be selected
    while True:
        print("1: Roll\n2: Ask to roll\n3: Roll untill 6\n4: Roll untill double\n")
        choice = input("What would you like to do? ")

        if choice == "1": #Roll
            dieValue = roll()
            time.sleep(1) #Wait
            showDie(dieValue) #Show the side of the die
            return
        
        elif choice == "2": #Ask to roll
            dieValue = decideToRoll()
            time.sleep(1) #Wait
            if dieValue != None: #If the die was rolled
                showDie(dieValue) #Show the side of the die
            return
                
        elif choice == "3": #Roll untill 6
            while True:
                dieValue = roll()
                time.sleep(1) #Wait
                showDie(dieValue) #Show the side of the die
                if dieValue == 5: #It starts at 0, not 1, so 5 is 6
                    print("You've rolled a six!")
                    return

        elif choice == "4": #Roll utnill double
            newDieValue = roll() #Holds the newest roll
            time.sleep(1) #Wait
            showDie(newDieValue) #Show the side of the die
            
            while True:
                oldDieValue = newDieValue #Holds the second newest roll
                newDieValue = roll()
                time.sleep(1) #Wait
                showDie(newDieValue) #Show the side of the die
                if newDieValue == oldDieValue: #If both rolls match
                    print("You've rolled a double!")
                    return
        
        else:
            print("That input is not understood!\n")

menu()

'''
Errors

I found many syntax errors, such as missing parenthesis
and misscapitalised names. I also found that the value 'dieValue' ('roll' at the time)
from the function roll() wasn't returned and so it couldn't be used in showDie.
The if statement previously found in showDie had only if and elses, no elifs.
However, I removed the if statement and used a list as dieValue was an integer, so it was more efficient.
The random.randint function was only given one parameter, and that was 7, when we want a number to 6.'''
