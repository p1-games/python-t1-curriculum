import random

num = random.randint(1,10)

while(True):
    Unum = int(input("guess a number betwen 1 and 10: "))

    if num == Unum:
        print("corect")
        break
    else:
        print("try again")