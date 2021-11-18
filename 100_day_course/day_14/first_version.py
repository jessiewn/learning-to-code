import random

import data
import art

def game(A,B,guess):
    if A> B:
        answer='A'
    elif A< B:
        answer='B'

    if guess!=answer:
        return 'wrong'
    elif guess==answer:
        return 'right'

    

def main():
    print(art.logo)
    A=random.choice(data.data)
    B=random.choice(data.data) 
    # ?what if random same item
    score=0
    print(f"Compare A: {A['name']}, {A['description']}, from {A['country']}.")
    print(art.vs)
    print(f"Against B: {B['name']}, {B['description']}, from {B['country']}.")
    while True:
        guess=input("Who has more followers? Type 'A' or 'B'\n")
        if game(A['follower_count'], B['follower_count'],guess)=='right':
            score+=1
            print(F'you are right, current score{score}')
            if A['follower_count']>B['follower_count']:
                B=random.choice(data.data) 
            elif A['follower_count']<B['follower_count']:
                A=B
                B=random.choice(data.data)
        elif game(A['follower_count'], B['follower_count'],guess)=='wrong':
            print(f"Sorry, that's wrong. Final score: {score}")
            break
        print(f"Compare A: {A['name']}, {A['description']}, from {A['country']}.")
        print(art.vs)
        print(f"Against B: {B['name']}, {B['description']}, from {B['country']}.")
main()

    
