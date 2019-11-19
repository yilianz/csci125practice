import random

def rps():
    user=input("rock paper scissors, Shoot!")    
    computer=random.choice(["rock","paper","scissors"])

    if user == computer:
        print(f"You chose {user}, Computer chose {computer}, DRAW!!!")
    elif user == "rock" and computer == "scissors":
        print(f"You chose {user}, Computer chose {computer}, You Win!!!")
    elif user == "paper" and computer == "rock":
        print(f"You chose {user}, Computer chose {computer}, You Win!!!")
    elif user == "scissors" and computer == "paper":
        print(f"You chose {user}, Computer chose {computer}, You Win!!!")
    elif user == "rock" and computer == "paper":
        print(f"You chose {user}, Computer chose {computer}, Computer Wins!!!")   
    elif user == "paper" and computer == "scissors":
        print(f"You chose {user}, Computer chose {computer}, Computer Wins!!!")
    elif user == "scissors" and computer == "rock":
        print(f"You chose {user}, Computer chose {computer}, Computer Wins!!!")
    else:
        print("Wut") 

#  test
rps()

 
           

