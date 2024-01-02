import random

"""
1. Ask user for input
2. Generate computer choice
3. Compare who won
4. Update the score
"""
CHOICES = ['R', 'P', 'S']

def print_menu():
    print("ROCK PAPER SCISSORS GAME!!!!\n"
          "----------------\n"
          "1. Rock\n"
          "2. Paper\n"
          "3. Scissors")


print_menu()

player_score = 0
pc_score = 0

play_game = True

while play_game:
    player_choice = input("Select an attack (R/P/S) (Q to quit): ")
    if player_choice.upper() == "R" or player_choice.upper() == "P" or player_choice.upper() == "S":
        pc_choice = random.choice(CHOICES)
        if (player_choice == "R" and pc_choice == "S") or (player_choice == "P" and pc_choice == "R") or (player_choice == "S" and pc_choice == " P"):
            print("Computer chose " + pc_choice)
            print("YOU WON!")
            player_score += 1
            print(f"Player Score: {player_score}\n"
                  f"Computer Score: {pc_score}\n")
        elif (player_choice == pc_choice):
            print("DRAW!")
        else:
            print("Computer chose " + pc_choice)
            print("YOU LOST! :(")
            pc_score += 1
            print(f"Player Score: {player_score}\n"
                  f"Computer Score: {pc_score}\n")

    elif player_choice.upper() == "Q":
        break
    else:
        print("not a valid choice")