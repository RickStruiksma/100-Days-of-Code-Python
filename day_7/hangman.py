# Day 7 Project: Hangman

# import statements. Hangman_art contains hangman ASCII art
from hangman_art import stages, logo
from hangman_words import word_list
from random import choice
# setting up a variable to control the game loop
continue_game = True
# Lives variable
lives = 6
chosen_word = choice(word_list)
# Display the logo
print(logo)
# A little cheat code
print(f'Pssst, the solution is {chosen_word}.')

# create a display list that holds a number of underscores matching the word
display = []
for letter in chosen_word:
    display.append("_")
# game loop
while continue_game:
    # take user input
    guess = input("Please guess a letter:\n")
    # check if the letter is in chosen_word, updating the display if needed
    for i in range(0, len(display)):
        if chosen_word[i] == guess:
            display[i] = guess
    if guess in display:
        print(f"You've already guessed {guess}")
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, which is not in the word. You have {lives}\
 lives left")
        
    print("".join(display))
    # checking to see if the player has won
    if "_" not in display:
        print("You've won!")
        continue_game = False
    if lives == 0:
        print("No lives left. You lose!")
        continue_game = False
    print(stages[lives])

                     

