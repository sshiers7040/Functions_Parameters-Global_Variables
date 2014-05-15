#Die roll program
#This program simulkates teh roll of a die.
#It generates a random number from a range of 6,
#with each number corresponding to a side on the die.
#It then displays this side.
#It could be used in simulated board games, adapted for dungeons and dragons or used with an actual board game.

import random #To simulate the die
import time #To allow a better user appeal

#To hold the displays for the dies sides
dieSides= ["- - - - -\n|         |\n|   O   |\n|         |\n- - - - -\n",
           "- - - - -\n|O      |\n|         |\n|      O|\n- - - - -\n",
           "- - - - -\n|O      |\n|   O   |\n|      O|\n- - - - -\n",
           "- - - - -\n|O   O|\n|        |\n|O   O|\n- - - - -\n",
           "- - - - -\n|O   O|\n|   O   |\n|O   O|\n- - - - -\n",
           "- - - - -\n|O   O|\n|O   O|\n|O   O|\n- - - - -\n"]

def roll():
    print("Rolling.....") #Tell the user
    roll = random.randint(0,5) #Creates arandom number from 0 to 5, a range of 6 (lists start at 0)
    return roll #So roll can be used in the main game


def showDie(roll):
    print(dieSides[roll]) #Selects the corect side from the list

roll = roll() #Roll, the die
time.sleep(1) #Wait
showDie(roll) #Show the side of the die

