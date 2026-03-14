"""
Snake Water Gun Game

s = Snake
w = Water
g = Gun

Rules:
Snake drinks Water  -> Snake wins
Water douses Gun    -> Water wins
Gun kills Snake     -> Gun wins
"""

import random

# Computer choice
computer = random.choice([-1, 0, 1])

# User input
youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()

# Dictionaries
youdict = {"s": 1, "w": -1, "g": 0}
reversedict = {1: "Snake", -1: "Water", 0: "Gun"}

# Convert user input to number
you = youdict.get(youstr)

if you is None:
    print("Invalid input! Please enter s, w, or g.")
else:
    print(f"\nYou chose: {reversedict[you]}")
    print(f"Computer chose: {reversedict[computer]}")

    if computer == you:
        print("Result: It's a draw!")

    elif (computer == -1 and you == 1):
        print("Result: You win!")

    elif (computer == -1 and you == 0):
        print("Result: You lose!")

    elif (computer == 1 and you == -1):
        print("Result: You lose!")

    elif (computer == 1 and you == 0):
        print("Result: You win!")

    elif (computer == 0 and you == 1):
        print("Result: You lose!")

    elif (computer == 0 and you == -1):
        print("Result: You win!")

    else:
        print("Something went wrong!")