# build a minigame of rock paper scissor with the below three simple rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock
# the game will be played between the user and the computer
# the user will be asked to enter his choice of rock, paper or scissor
# the computer will randomly select its choice
# the result will be displayed to the user
# the user will be asked if he wants to play again
# if yes, the game will continue
# if no, the game will end
# the user will be shown the number of games he won, lost and tied



import random

def main():
    print("Welcome to Rock Paper Scissor Game!")
    print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock")
    print("Let's start the game!")
    play_game()

def play_game():
    user_wins = 0
    computer_wins = 0
    ties = 0
    while True:
        
        user_choice = handle_input()
        computer_choice = random.choice(["rock", "paper", "scissor"])
        print(f"Computer's choice: {computer_choice}")
        result = get_result(user_choice, computer_choice)
        print(result)
        if result == "You win!":
            user_wins += 1
        elif result == "You lose!":
            computer_wins += 1
        else:
            ties += 1
        print(f"Games won: {user_wins}, Games lost: {computer_wins}, Games tied: {ties}")
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

def handle_input():
    user_choice = input("Enter your choice (rock, paper, scissor): ")
    while user_choice.lower() not in ["rock", "paper", "scissor"]:
        user_choice = input("Invalid choice! Enter your choice (rock, paper, scissor): ")
    return user_choice

def get_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissor") or (user_choice == "scissor" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"
    
if __name__ == "__main__":
    main()

# Output:
# Welcome to Rock Paper Scissor Game!
# Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock
# Let's start the game!
# Enter your choice (rock, paper, scissor): rock
# Computer's choice: scissor
# You win!
# Games won: 1, Games lost: 0, Games tied: 0
# Do you want to play again? (yes/no): yes
# Enter your choice (rock, paper, scissor): paper
# Computer's choice: rock
# You win!
# Games won: 2, Games lost: 0, Games tied: 0
