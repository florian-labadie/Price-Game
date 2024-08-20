import random

def price_game():
    secret_number = random.randint(1, 10000)
    attempts = 0

    while True:
        attempts += 1
        print("Guess the secret number!")
        user_guess = int(input())

        if user_guess == secret_number:
            print(f"Congratulations! You found the secret number in {attempts} attempts.")
            break
        elif user_guess < secret_number:
            print("The secret number is greater.")
        elif user_guess > secret_number:
            print("The secret number is smaller.")
        elif user_guess < 1 or user_guess > 10000:
            print("Please enter a number between 1 and 10000.")
