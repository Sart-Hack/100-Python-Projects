# This is day 4 project for the 100 Days of Python course
import random

num_rounds = 1
player_score = 0
comp_score = 0

print("Welcome to Rock, Paper and Scissors. You know the rules already.")

while True:
    print(f"Round Number: {num_rounds}")
    player_input = input("Choose rock, paper or scissors. Enter \'exit\' to finish the game \n").lower()
    comp_action = random.choice(["rock", "paper", "scissors"])
    print(f"\nYou chose {player_input}, computer chose {comp_action}.\n")

    if player_input == "exit":
        print("You have exited the game.")
        break
    elif player_input == comp_action:
        print(f"Both players selected {player_input}. It's a tie!")
    elif player_input == "rock":
        if comp_action == "scissors":
            print("Rock smashes scissors! You win!")
            player_score += 1
        else:
            print("Paper covers rock! You lose.")
            comp_score += 1
    elif player_input == "paper":
        if comp_action == "rock":
            print("Paper covers rock! You win!")
            player_score += 1
        else:
            print("Scissors cuts paper! You lose.")
            comp_score += 1
    elif player_input == "scissors":
        if comp_action == "paper":
            print("Scissors cuts paper! You win!")
            player_score += 1
        else:
            print("Rock smashes scissors! You lose.")
            comp_score += 1
    else:
        print("Invalid input, try again.")
        continue

    print(f'''Your score: {player_score}\nComp score: {comp_score}\n''')

    num_rounds += 1

print(f"---Final scores---\nPlayer Score: {player_score}\nComputer Score: {comp_score}\n")
