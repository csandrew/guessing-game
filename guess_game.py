
import random

while True:
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5

    print("\nWelcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100")
    print(f"You have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} attempts!")
            break
    else:
        print(f"Game over! The number was {secret_number}")

    play_again = input("Play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break


