import random
comp_win=0
user_win=0
print("Welcome to the tournament of ROCK, PAPER, SCISSORS.")
print("Please enter the rounds of tournament you want to play.")
n=int(input("Enter rounds: "))
for i in range(0,n):
    user_action=input("Choose your action(Rock,Paper,Scissors):  ")
    b=["Rock","Paper","Scissors"]
    computer_action=random.choice(b)
    print(f"\n You chose: {user_action},  Computer chose: {computer_action}\n")
    if user_action==computer_action:
        print("It is a tie..! ")
    elif user_action=="Rock":
        if computer_action=="Scissors":
            print("Rock smashes Scissors..\nCongratulations..! You Won.\n")
            user_win+=1
        else:
            print("Scissors cuts Paper..\nComputer Won..!\n")
            comp_win+=1
    elif user_action=="Paper":
        if computer_action=="Rock":
            print("Paper covers Rock..\nCongratulations..! You Won.\n")
            user_win+=1
        else:
            print("Scissors cuts Paper..\nComputer Won..!\n")
            comp_win+=1
    elif user_action=="Scissors":
        if computer_action=="Paper":
            print("Scissors cuts Paper..\nCongratulations..! You Won.\n")
            user_win+=1
        else:
            print("Rock smashes Scissors..\nComputer Won..!\n")
            comp_win+=1
print(f"You won {user_win} times, Computer won {comp_win} times")
if (comp_win>user_win):
  print("Computer won the tournament.")
elif (user_win>comp_win):
  print("Congratulations..! You won the tournament.")
else:
  print("It's a tie.")