import random

while(True):
    options = ["Rock", "Paper", "Scissors"]
    comp_ch = random.choice(options)
    user_ch = input("Select From Following :\n Rock, Paper ,Scissors: \n")
    print("Your Choice: ", user_ch)
    print("Computers Choice: ", comp_ch)

    if user_ch == comp_ch:
        print("Same Choice Hence It's A Tie!")
        rd=input("if want another round then type Yes otherwise No ")
        if rd =="No":
            break
        else:
            continue

    elif user_ch == "Rock" and comp_ch == "Scissors":
        print("You won!")
        rd=input("if want another round then type Yes otherwise No ")
        if rd=="No":
            break
        else:
            continue

    elif user_ch == "Paper" and comp_ch == "Rock":
        print("You won!")
        rd=input("if want another round then type Yes otherwise No ")
        if rd=="No":
            break
        else:
            continue

    elif user_ch == "Scissors" and comp_ch == "Paper":
        print("You Won!")
        rd=input("if want another round then type Yes otherwise No ")
        if rd=="No":
            break
        else:
            continue

    else:
        print("Computer Wins!")
        rd=input("if want another round then type Yes otherwise No")
        if rd=="No":
            break
        else:
            continue 

print("THANK YOU FOR GOOD GAME")