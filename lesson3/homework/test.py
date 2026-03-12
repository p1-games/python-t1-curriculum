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