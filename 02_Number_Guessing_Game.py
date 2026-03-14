"""
Number Guessing Game

The computer selects a random number between 1 and 100.
The user tries to guess the number.
The program gives hints: higher or lower.
"""

from random import randint

# Generate random number
number = randint(1, 100)

guess = -1
attempts = 0

while guess != number:
    guess = int(input("Enter your guess (1-100): "))
    attempts += 1

    if guess > number:
        print("Lower number please.")
    elif guess < number:
        print("Higher number please.")

print(f"\nYou guessed the number {number} correctly in {attempts} attempts!")