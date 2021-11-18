from art import logo
import random
print(logo)

RANDOM_NUMBER=random.randint(1,100)
def compare(guess):
    if guess<RANDOM_NUMBER:
        print('too low')
    elif guess>RANDOM_NUMBER:
        print('too high')
    elif guess==RANDOM_NUMBER:
        print(f'You got it! The answer was {RANDOM_NUMBER}.')
        return
def game(times):   
    for i in range(times):
        print(f'You have {times} attempts remaining to guess the number.')
        guess=int(input('make a guess'))
        compare(guess)
        times -= 1
        if guess == RANDOM_NUMBER:
            break
        
def main():
    print("Welcome to the Number Guessing Game!\n I'm thinking of a number between 1 and 100.")
    print(f'Pssst, the correct answer is {RANDOM_NUMBER}')
    level=input("Choose a difficulty. Type 'easy' or 'hard':\n")

    if level == 'easy':
        game(5)
    if level == 'hard':
        game(10)
main()
        

