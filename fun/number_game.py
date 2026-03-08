# Problem 3
# Generate a random number between 1 and 10 (inclusive).
# Ask the user to guess the number.
# Print "Correct!" if the guess matches the random number, else print "Try again!".
import random

num = random.randint(1,10)

while(True):
    Unum = int(input("guess a number betwen 1 and 10: "))

    if num == Unum:
        print("corect")
        break
    else:
        print("try again")