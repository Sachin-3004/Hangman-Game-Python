#Importing random module from Python Library
import random

#Creating a List of 5 elements
words = ["python", "network", "mobile", "coding", "machine"]

#Choosing random word from the list of 5 elements
secret_word=random.choice(words)

guessed_letters=[]
incorrect_guesses=0
max_incorrect=6

#Instructions given to the player about the Hangman Game
print("====================================")
print("WELCOME TO HANGMAN GAME!")
print("====================================")
print("I have chosen a secret word. Try to guess it letter by letter!")
print(f"You are allowed a maximum of {max_incorrect} incorrect guesses.\nIf you reach the maximum number of incorrect guesses, you will lose the game.")
    
# Main game loop
while incorrect_guesses < max_incorrect:

# Create and display the current state of the word (e.g., p _ _ t h o n)
        word_display = []
        for letter in secret_word:
            if letter in guessed_letters:
                word_display.append(letter)
            else:
                word_display.append("_")

# Display the formatted word with spaces in between for readability
        current_status = " ".join(word_display)
        print(f"\nWord: {current_status}")
        print(f"Incorrect guesses remaining: {max_incorrect - incorrect_guesses}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        
# Check if the player has guessed all the letters in the secret word
        if "_" not in word_display:
           print("\n=========================")
           print(f"Congratulations!! You Won the Game")
           print(f"The Secret Word was: {secret_word}") 
           print("=========================")
           break
# Ask the player for input
        guess = input("Guess a letter: ").strip().lower()
        
# Input Validation
# Check if the input is not exactly one character, or not an alphabetical letter
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter (A-Z).")
            continue
            
# Check if the letter has already been guessed
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Please try a different letter!")
            continue
            
# Record the guess
        guessed_letters.append(guess)
        
# Check if the guess is correct or incorrect
        if guess in secret_word:
            print(f"Correct! '{guess}' is in the word.")
        else:
            print(f"Incorrect! '{guess}' is not in the word.")
            incorrect_guesses += 1
            
# Check if game ended because the player ran out of guesses
if incorrect_guesses == max_incorrect:
         	print("\n=========================")
         	print("Game Over!!!")
         	print(f"You've run out of guesses... The Secret Word was: {secret_word}")
         	print("Better Luck Next Time!!!")
         	print("=========================") 
         	
#Coding is Completed. Hangman Game is ready to play!!!
#Enjoy the Game         	                           