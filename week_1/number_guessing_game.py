import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it!")

    target = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < target:
                print("Too low!")
            elif guess > target:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                save_results(target, attempts)
                break
        except ValueError:
            print("Invalid input! Please enter a number.")

def save_results(target, attempts):
    with open("guessing_game_results.txt", "a") as file:
        file.write(f"Guessed {target} in {attempts} attempts.\n")
    print("Results saved to guessing_game_results.txt")

# Main program
number_guessing_game()
