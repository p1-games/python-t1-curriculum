# Problem 1
# Ask the user to enter a number.
# Print "Even" if the number is divisible by 2, otherwise print "Odd".
banana = int(input("pick number because yes and do it right now: "))
if banana % 2 != 1:
    print("Even")
else:
    print("odd")



# Problem 2
# Ask the user for the day of the week (all lowercase).
# Print "Weekend" if the day is "saturday" or "sunday",
# else print "Weekday".
banana = (input("enter day of the week (all lowercase): "))
if banana in ["saturday","sunday"]:
    print("weekend")
else:
    print("weekday")



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


# Problem 4
# Ask the user for a positive integer.
# If the number is divisible by 2 and greater than 10, print "Big even number".
# Otherwise print "Number does not meet criteria".
banana = int(input("enter a positive integer because yes and do it right now: "))
if banana % 2 != 1 and banana > 10:
    print("Big Even Number")
else:
    print("Number does not meet criteria")



# Problem 5
# Ask the user for two numbers.
# Print which number is larger.
# If the numbers are equal, print "Numbers are equal".
banana = int(input("pick number because yes and do it right now: "))
apple = int(input("pick number because yes and do it right now: "))
if banana == apple:
    print("Numbers are equal")
elif banana > apple: 
    print(banana)
else:
    print(apple)