def guess_the_number():
    print("Welcome to the 'Guess the Number' game!")
    print("Think of a number between 1 and 100, and I will try to guess it!")

    low = 1
    high = 10
    attempts = 0

    while True:
        guess = (low + high) // 2
        attempts += 1

        feedback = input(f"My guess is {guess}. Is it too high, too low, or correct? ").lower()

        if feedback == "correct":
            print(f"Yay! I guessed your number in {attempts} attempts!")
            break
        elif feedback == "too high":
            high = guess - 1 
        elif feedback == "too low":
            low = guess + 1  
        else:
            print("Please respond with 'too high', 'too low', or 'correct'.")

guess_the_number()
