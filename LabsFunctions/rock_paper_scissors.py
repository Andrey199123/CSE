from random import choice

def generate_choice():
    options = ["rock", "paper", "scissors"]
    return choice(options)


def decide_winner(player, opponent):
    if player == opponent:
        return "tie"
    elif (player == "rock" and opponent == "scissors") or (player == "scissors" and opponent == "paper") or (
            player == "paper" and opponent == "rock"):
        return "player"
    else:
        return "opponent"


while True:
    user_input = input("Make your move: rock, paper, or scissors? ").lower()
    while user_input not in ["rock", "paper", "scissors"]:
        print("Please enter rock, paper, or scissors.")
        user_input = input("Make your move: ").lower()

    computer_choice = generate_choice()
    print("Computer chose:", computer_choice)

    game_result = decide_winner(user_input, computer_choice)

    if game_result == "player":
        print("You win.")
    elif game_result == "opponent":
        print("Computer wins.")
    else:
        print("It's a tie.")
        continue

    play_again = input("Do you want to play again? Enter 'yes' or 'no': ").lower()
    if play_again != "yes":
        break
