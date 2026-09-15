import random
choices=["rock","paper","scissor"]
comp=random.choices(choices)
times=int(input("How many times do you want to play this game:"))
flag=False
points=0
c_points=0

for i in range(times):
    user=str(input("Please make your choice from(rock,paper,scissor) : ").lower())

    if user==comp:
        print("Its a tie , you both chose the same",)
    elif user=="rock" and comp==["scissor"]:
        print("Computer chose scissor",)
        print("You chose ",user)
        print("You won ")
        points +=1
    elif user=="paper" and comp==["scissor"]:
        print("Computer chose scissor",)
        print("You chose ",user)
        print("You lose ")
        c_points +=1
    elif user=="scissor" and comp==["paper"]:
        print("Computer chose paper",)
        print("You chose ",user)
        print("You won ")
        points +=1
    elif user == "rock" and comp == ["paper"]:
        print("Computer chose paper", )
        print("You chose ", user)
        print("You lose ")
        c_points += 1
    elif user=="scissor" and comp==["rock"]:
        print("Computer chose rock",)
        print("You chose ",user)
        print("You lose ")
        c_points +=1
    elif user=="paper" and comp==["rock"]:
        print("Computer chose rock",)
        print("You chose ",user)
        print("You won ")
        points +=1

print("Your total score is ",points)
print("Computer's total score is ",c_points)
if points>c_points:
            print("You won this set of laps")
elif points<c_points:
            print("You lost this set of laps")
elif points==c_points:
            print("This set of laps ended in draw ")
print("Thanks for playing ")