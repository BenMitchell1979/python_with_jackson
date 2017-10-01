#!/usr/bin/env python3
import random

user = raw_input("Select one of the following: Wizard, Tiger, or Dragon:")

# Random Computer Choice
choice = ['Wizard', 'Tiger', 'Dragon']
computer = random.choice(choice)

def game(user,computer):

    # Output Vars
    you_win = "Winner, Winner! Chicken Dinner!"
    you_lose = "Loser, Loser! HAHAHA!"

    # Game Logic
    if computer == user:
        result = 'TIE!'
        return(result)
    elif user == 'Wizard' and computer == 'Dragon':
        result = you_win
        return(result)
    elif user == 'Tiger' and computer == 'Wizard':
        result = you_win
        return(result)
    elif user == 'Dragon' and computer == 'Tiger':
        result = you_win
        return(result)
    else:
        result = you_lose
        return(result)

output = game(user, computer)
print(output)
