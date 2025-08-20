import random

print("< welcome to the Rock , Paper , Scissor Game >")
print("Let's Start the Game.Or Quit(Q)")

while True:
    values = "Rock","Paper","Scissor"
    bot_choice = random.choice(values)

    user_choice = input("Enter Your choice From [Rock,Paper,Scissor] : ").lower()
    if(user_choice == "Q"):
        print("User Quitted.")
        break
    if (user_choice=="Rock" and bot_choice=="Paper"):
        print("bot choose Paper . You lose!")
    elif (user_choice=="Paper" and bot_choice=="Scissor"):
        print("bot choose Scissor . You lose!")
    elif (user_choice=="Scissor" and bot_choice=="Rock"):
        print("bot choose Rock . You lose!")
    elif(user_choice == bot_choice):
        print("It's a tie! Let's Try Again")
    else:
        print("bot choose",bot_choice,". You Won!")
        break





