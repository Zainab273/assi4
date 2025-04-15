import random

stages = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

words = ['apple', 'mango', 'banana', 'orange', 'grapes']
chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word]
guessed_letters = []
lives = len(stages) - 1

print("🎉 Welcome to Hangman! 🎉")
print("🔤 Guess the fruit name!")

while True:
    print(stages[len(stages) - 1 - lives])
    print("Word: ", " ".join(word_display))
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❗ Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("🔁 Already guessed! Try a different letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print(f"✅ Good guess! '{guess}' is in the word.")
        for idx, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[idx] = guess
    else:
        print(f"❌ Oops! '{guess}' is not in the word.")
        lives -= 1

    if '_' not in word_display:
        print("🎉 Congratulations! You guessed the word:", chosen_word)
        break

    if lives == 0:
        print(stages[len(stages) - 1])
        print(f"💀 Game Over! The word was '{chosen_word}'.")
        break
