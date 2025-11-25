# ----------------------------------------
# Project 2: Number Guessing Game
# ----------------------------------------

import random

def choose_level():
    print("\nSelect Difficulty:")
    print("1. Easy (1–10)")
    print("2. Medium (1–50)")
    print("3. Hard (1–100)")

    level = input("Enter choice: ")

    if level == "1": return 1, 10
    if level == "2": return 1, 50
    if level == "3": return 1, 100
    else:
        print("Invalid option! Default: Easy.")
        return 1, 10

def play_game():
    low, high = choose_level()
    number = random.randint(low, high)
    attempts = 0

    print(f"\nGuess the number between {low} and {high}.")

    while True:
        try:
            guess = int(input("Your guess: "))
        except:
            print("Enter a valid integer!")
            continue

        attempts += 1

        if guess < number:
            print("Higher ⬆️")
        elif guess > number:
            print("Lower ⬇️")
        else:
            print(f"🎉 Correct! You guessed in {attempts} attempts.")
            break

def main():
    while True:
        play_game()
        again = input("\nPlay again? (yes/no): ")
        if again.lower() != "yes":
            print("Thanks for playing!")
            break

main()
