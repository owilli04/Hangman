import random 
import string
#import array words
from words import words 

def hangman():
    #letter in the word
    words_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    #what the user has guessed
    used_letters = set()

    lives = 5

    #getting user input telling the user how many lives they have left
    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives left and you used these letters: ', ' ' .join(used_letters))

    #what the current word is
    words_list = [letter if letter in used_letters else '-' for letter in word]
    print('Current word; ', ' '.join(words_list))
    #print(lives_visual_dict[lives])

    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)
            print('')
        else:
            #if they guess wrong
            lives = lives-1 #takes a life away from the user
            print('Yours letter' user_letter, 'is not a member of the word') 
    elif user_letter in used_letters:
        print('You already used this letter! Try again!')
    else:
        ('THIS IS NOT A LETTER! Try again :)')

    #check whether lives=0 or the word is guessed correctly
    if lives ==0:
        print('Sorry you lost all your lives', word)
    else:
        print('Hooray! You guessed the right word', word)