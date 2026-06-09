#libraries utilized

import random

def number_guessing_game():
    print("\n--- Number Guessing Game ---")
    number = random.randint(1, 100)
    while True:
        guess = int(input("Guess a number (1-100): "))
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("You win!")
            break

def rock_paper_scissors():
    print("\n--- Rock, Paper, Scissors ---")
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = input("Rock, Paper, or Scissors? ").lower()
    print("Computer chose:", computer)
    if player == computer:
        print("Tie!")
    elif (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        print("You win!")
    else:
        print("You lose!")

def quiz_game():
    print("\n--- Quiz Game ---")
    score = 0
    answer = input("What is the capital of France? ")
    if answer.lower() == "paris":
        score += 1
    answer = input("What is 5 + 5? ")
    if answer == "10":
        score += 1
    print("Your score:", score, "/ 2")

def hangman_game():
    print("\n--- Hangman Game ---")
    word = "python"
    guessed = []
    while True:
        display = ""
        for letter in word:
            if letter in guessed:
                display += letter
            else:
                display += "_"
        print(display)
        if "_" not in display:
            print("You win!")
            break
        guess = input("Guess a letter: ")
        guessed.append(guess)

def main():
    while True:
        print("\nChoose a game to play:")
        print("1. Number Guessing")
        print("2. Rock, Paper, Scissors")
        print("3. Quiz Game")
        print("4. Hangman")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            number_guessing_game()
        elif choice == "2":
            rock_paper_scissors()
        elif choice == "3":
            quiz_game()
        elif choice == "4":
            hangman_game()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()