#Hangman game using Python 
import random
words = ["apple", "guava", "mango", "kiwi", "peach","dragonfruit","banana","strawberry","blueberry",]
secretword = random.choice(words)
guessed = []
turns = 6
while turns > 0:

    for letter in secretword:
        if letter in guessed:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()

    guess = input("Enter a letter: ").lower()

    if guess in guessed:
        print("Already guessed!")
        continue

    guessed.append(guess)

    if guess not in secretword:
        turns -= 1
        print(f"Wrong guess! {turns} turns left")

    win = True

    for letter in secretword:
        if letter not in guessed:
            win = False
            break

    if win:
        print(f"You Win! The word was {secretword}")
        break

if turns == 0:
    print(f"Game Over! The word was {secretword}")