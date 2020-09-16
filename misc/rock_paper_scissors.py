##########################################################
# vMake a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock


def to_numb(choice):
    if choice == "rock":
        choice_num = 1
    elif choice == "paper":
        choice_num = 2
    elif choice == "scissors":
        choice_num = 3
    else:
        choice_num = "not a valid choice"
    return choice_num


def game(p1, p2):
    if (p1 == "not a valid choice") or (p2 == "not a valid choice"):
        print("Both players must enter a valid choice")
        winner = "Incorrect information entered"
    elif p1 - p2 == -1:
        winner = "Player2"
    elif p1 - p2 == 2:
        winner = "Player2"
    elif p1 - p2 == 1:
        winner = "Player1"
    elif p1 - p2 == -2:
        winner = "Player1"
    else:
        winner = "Tie"
    return winner


player_1_choice = input("Player 1 make your choice: ")
p1 = to_numb(player_1_choice)

player_2_choice = input("Player 2 make your choice: ")
p2 = to_numb(player_2_choice)

print("The winner is", game(p1, p2))
