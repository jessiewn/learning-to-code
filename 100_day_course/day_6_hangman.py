#Step 1 
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
import random
chosen_word= random.choice(word_list)
print(chosen_word)

display=[]
for n in range(0,len(chosen_word)):
    display.append('_')
print(display)
end_of_game = False
lives = 6
print('You have 6 lives')
print(stages[0])

while not end_of_game:
    guess=input('Guess a letter\n').lower()
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            #print(i)
            display[i]=guess
    
    if guess != chosen_word[i]:
        lives=lives-1
        print(f'now you have {lives} lives')
        print(stages[6-lives])
    print(display)
    if lives == 0:
        end_of_game = True
        print('You Lose')
    if '_' not in display:
        end_of_game = True
        print('You Win')


#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6


#TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."

    #Join all the elements in the list and turn it into a String.
    #Check if user has got all letters
#TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.