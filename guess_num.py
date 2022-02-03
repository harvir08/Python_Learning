import random
cnumber=random.randrange(1,101)
userInput=int(input("Enter your number:--"))
if userInput>cnumber:
    print("Computer Number",cnumber)
    print("Your guess number is too high")
elif cnumber>userInput:
    print("Computer Number", cnumber)
    print("Your guess number is too low")
else:
    print("Computer Number", cnumber)
    print("Your guess number is equal")