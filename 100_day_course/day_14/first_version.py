import random
import data

def game(answer):
    global score
    global A
    global B 
    if A['follower_count']> B['follower_count']:
        if answer == 'A':
            score+=1
            print(F'you are right, current score{score}')
            B=random.choice(data.data)
            # ?what if random same B
        elif answer == 'B':
            print(f"Sorry, that's wrong. Final score: {score}")
            return
    elif A['follower_count']< B['follower_count']:
        if answer=='A':
            print(f"Sorry, that's wrong. Final score: {score}")
            return
        elif answer=='B':
            score+=1
            print(F'you are right, current score{score}')
            A=B
            B=random.choice(data.data)

A=random.choice(data.data)
B=random.choice(data.data) 
score=0
print(f"Compare A: {A['name']}, {A['description']}, from {A['country']}.")
#print(vs)
print(f"Compare B: {B['name']}, {B['description']}, from {B['country']}.")
while True:
    answer=input('what is your guess')
    game(answer)
    print(f"Compare A: {A['name']}, {A['description']}, from {A['country']}.")
    ##print(vs)
    print(f"Compare B: {B['name']}, {B['description']}, from {B['country']}.")

    
