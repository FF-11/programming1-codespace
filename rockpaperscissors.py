import random
choices=["rock","paper","scissors"]
while True:
    player = input("Enter rock/paper/scissors: ")
    if player in choices: break
computer = random.choice(choices)

print(f"You chose {player}, computer chose {computer}")

match (choices.index(computer)-choices.index(player))%3:
    case 0:
        print("It's a tie.")
    case 1:
        print("The computer won.")
    case 2:
        print("You won.")
