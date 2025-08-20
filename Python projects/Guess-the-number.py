import random

target = random.randint(1,100)

while True:
    userchoice = input("Guess the Number or Quit(Q): ")
    if (userchoice == "Q"):
        print("User Quitted")
        break

    userchoice = int(userchoice)
    if (userchoice == target):
        print("You won the Game.")
        break
    elif (userchoice > target):
        print("Your Number is Big.Take a smaller number....")
    else:
        print("Your Number is Small.Take a bigger number....")

print("....Game Over....")
