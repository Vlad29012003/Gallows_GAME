
import random

# This code selects a random word from the list of strings words and prints it to the screen.
with open("headman.txt", "r") as file:
    words = file.readlines()

# The strip() method removes whitespace characters (spaces, tabs, newlines, etc.)
word = random.choice(words).strip()

def hangman():
    print ('hello welcome to hangman game.')

    word = random.choice(words).strip()
    guesses = 'bcdfghjklmnp'
    turns = 5

    while turns > 0:
        missed = 0
        for letter in word:
            if letter in guesses:
                print(letter,end=' ')
            else:
                print('_',end=' ')
                missed += 1

        if missed == 0:
            print('\n.you pleased ( -__- )  ')
            break

        guess = input('\nname a letter: ')
        guesses += guess

        if guess not in word:
            turns -= 1

            print ('\n did not please ( ^__^ )')
            print ('\n you have attempts left: ', turns)
            if turns < 5: print ('\n  | ' )
            if turns < 4: print ('  O ' )        
            if turns < 3: print (' /|\ ')
            if turns < 2: print ('  |  ')
            if turns < 1: print (' / \ ')
            if turns == 0: print ('\n\n this word: ', word)

ans = 'yes'
while ans == 'yes':
    hangman()
    print('do you want to play again? (yes or no ) ( ^__^ ) ')
    ans = input()