import random

def main():
    print("Welcome to the Number Guessing Game!")

    number_guess = random.randint(1, 10)
    attempt = 0

    while True:
        guess = int(input("Guess the number between 1-10: "))
        attempt += 1

        if guess < number_guess:
            print("Oops! Your guess is too low!")
        elif guess > number_guess:
            print("Oops! Your guess is too high!")
        elif guess == number_guess:
            print(f"Congratulations! You guessed the number in {attempt} attempts!")
            break  

main()
