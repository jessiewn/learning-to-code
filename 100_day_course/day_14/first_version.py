import random
import data
from art import logo
from art import vs

def game(guess):
    global score
    global A
    global B 
    if A['follower_count']> B['follower_count']:
        answer='A'
        if guess == answer:
            score+=1
            print(f'you are right, current score{score}')
            B=random.choice(data.data)
            # ?what if random same B
        elif guess != answer:
            print(f"Sorry, that's wrong. Final score: {score}")
            answer='wrong'
            return answer
    elif A['follower_count']< B['follower_count']:
        answer='B'
        if guess!=answer:
            print(f"Sorry, that's wrong. Final score: {score}")
            answer='wrong'
            return answer
        elif guess==answer:
            score+=1
            print(F'you are right, current score{score}')
            A=B
            B=random.choice(data.data)
            
print(logo)
A=random.choice(data.data)
B=random.choice(data.data) 
score=0
print(f"Compare A: {A['name']}, {A['description']}, from {A['country']}.")
print(vs)
print(f"Against B: {B['name']}, {B['description']}, from {B['country']}.")
while True:
    guess=input("Who has more followers? Type 'A' or 'B'\n")
    if game(guess)== 'wrong':
        break
    print(f"Compare A: {A['name']}, {A['description']}, from {A['country']}.")
    print(vs)
    print(f"Against B: {B['name']}, {B['description']}, from {B['country']}.")

    
