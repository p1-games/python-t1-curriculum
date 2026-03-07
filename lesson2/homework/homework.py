# Homework Problem 1
# Ask the user for two numbers.
# Print their quotient and remainder on separate lines.
inutp1 = int(input("give number now!"))
input2 = int(input("give another one now!"))
quotient = int(input1 / input2)
remainder = input1 % input2
print(quotient)
print(str(remainder) + "R")

# Homework Problem 2
# Ask the user for their favorite animal and favorite color.
# Print a sentence combining them like: "A blue tiger would be awesome!"
color = input("give coler of favorit stuff: ")
animal = input("and favorit animal: ")

print("A",color,animal,"would be awesome")

# Homework Problem 3
# Use a for loop to print all the even numbers from 0 to 10 (including 10).
for banana in range(11):
    if banana % 2 != 1:
        print(banana)


# Homework Problem 4
# Ask the user how many push-ups they can do.
# Multiply it by 7 and print how many they could do in a week.
push = int(input("how push-ups can do: "))
push_up = push * 7
print(push_up)


# Homework Problem 5
# Use a for loop to print the square of each number from 1 to 6.
# (Example: 1*1=1, 2*2=4, etc.)
for food in range(1,7):
     print(food * food)