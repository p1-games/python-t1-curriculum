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