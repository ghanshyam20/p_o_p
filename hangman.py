# we are going to make a hangman game using python 
import random


stages=[
    r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']


word_list=['aardvark','baboon','camel']


lives=6



choosen_word=random.choice(word_list)




placeholder= ""
word_length=len(choosen_word)

for postion in range(word_length):
    placeholder += "_ "

print(placeholder)

game_over=False
correct_letter=[]

while not game_over:
    guess=input("Guess a letter:").lower()



    display=""

    for letter in choosen_word:
        if letter==guess:
            display += letter
            correct_letter.append(guess)


        elif letter in correct_letter:
            display += letter


        else:
            display += "_ "

    

    if guess not in choosen_word:
        lives-=1
        if lives==0:
            game_over=True

            print("You loose")

    if "_" not in display:
        game_over=True
        print("you win ")

    print(stages[lives])


  

