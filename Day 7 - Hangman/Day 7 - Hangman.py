# This is day 7 project for the 100 days of python

import random
import json

f = open("words_dictionary.json")
data = json.load(f)
words = [word for word in data.keys() if 2 <= len(word) <= 10]


print("Welcome to Hangman!")

print('''+---+
  |   |
      |
      |
      |
      |
=========''')

target_word = random.choice(words)
guess_word = ["_"]*len(target_word)
counter = 0
print(target_word)

print(" ".join(guess_word))
while True:

    guess_letter = input("Enter the letter you want to guess.\n")
    if guess_letter in guess_word:
        print(f"You've already guessed {guess_letter}")
    elif guess_letter in target_word:
        for i in range(len(target_word)):
            if guess_letter == target_word[i]:
                guess_word[i] = guess_letter
        print(" ".join(guess_word))

        if "_" not in guess_word:
            print("You guessed the word. You Win!")
            break

    else:
        counter += 1

        if counter == 1:
            print('''+---+
  |   |
  O   |
      |
      |
      |
=========''')
        elif counter == 2:
            print('''+---+
  |   |
  O   |
  |   |
      |
      |
=========''')
        elif counter == 3:
            print('''+---+
  |   |
  O   |
 /|   |
      |
      |
=========''')
        elif counter == 4:
            print('''+---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''')
        elif counter == 5:
            print('''+---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''')
        elif counter == 6:
            print('''+---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''')
            print("Hangman died. Game over, you lose.")
            break

