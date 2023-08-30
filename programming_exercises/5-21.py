import random
def get_computer_choice():
    # generate a number between 1 and 3
    computer_choice_num = random.randint(1, 3)

    # map the random number to rock, paper, or scissors
    if computer_choice_num == 1:
        return "rock"
    elif computer_choice_num == 2:
        return "paper"
    else:
        return "scissors"
    
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "scissors" and computer_choice == "paper") or \
            (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = input("\nEnter your choice (rock, paper, scissors): ")
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        computer_choice = get_computer_choice()
        print(f"Computer chooses: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("\nDo you want to play again? (yes/no:) " ).lower()
        if play_again != "yes":
            print("Thank you for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
