# Problem 1
# Ask user for two test scores.
# If BOTH scores are at least 50, print "You passed both!"
# Otherwise, print "You failed at least one."
test = input("give test score (0-100) :")
test2 = input ("give test score one more time :")
if int(test) >= 50 and int(test2) >= 50:
    print("You passed both!")
else:
    print("You failed at least one.")
# Problem 2
# Ask user if they brought lunch and water (yes/no).
# If they brought lunch OR water, print "You're somewhat ready."
# If they brought both, print "You're fully ready!"
# If they brought neither, print "You're not ready."
water = input("did you bring water (yes/no) :")
lunch = input("did you bring lunch (yes/no) :")
if water == "yes" and lunch == "yes":
    print("You're fully ready!")
elif water == "yes" or lunch == "yes":
    print("You're somewhat ready.")
else:
    print("You're not ready.")


# Problem 3
# Ask user to enter a number.
# If the number is NOT between 1 and 10 (inclusive), print "Out of range."
# Otherwise, print "In range."
num = int(input("give a number (1-10): "))
if num > 0 and num < 11:
    print("in range")
else:
    print("Out of range")


# Problem 4
# Generate a random number between 1 and 10.
# Ask the user to guess.
# If the guess is right AND the number is even, print "Even match!"
# Else if guess is right OR number is 5, print "Nice try!"
# Otherwise, print "Nope."
import random

num = random.randint(1,10)

while(True):
    Unum = int(input("guess a number betwen 1 and 10: "))

    if num == Unum and Unum % 2 == 0:
        print("Even match!")
        break
    elif num == Unum or Unum == 5:
        print("Nice try!")
        break
    else:
        print("Nope")


# Problem 5
# Ask the user for two numbers.
# If one is divisible by 5 AND the other is NOT divisible by 2, print "Interesting pair!"
# Otherwise, print "Plain pair."
num = int(input("give number: "))
num2 = int(input("again, give number: "))
if (num % 5 == 0 and num2 % 2 != 0) or (num2 % 5 == 0 and num % 2 != 0):
    print("Interesting pair!")
else:
    print("Plain pair")