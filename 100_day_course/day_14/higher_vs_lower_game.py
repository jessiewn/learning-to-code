import random
from art import logo
from art import vs
import data

print(logo)
A=random.choice(data.data)
B=random.choice(data.data)
def compare(answer):
    if A['follower_count']> B['follower_count']:
        score=0
        if answer == 'A':
            score+=1
            print(F'you are right, current score{score}')
            B=random.choice(data.data)
            # ?what if random same B
        if answer == 'B':
            print(f"Sorry, that's wrong. Final score: {score}")





# what if they random same one
# ?print(A['name','description','country'])
print(f"Compare A: {A['name']}, {A['description']}, from {A['country']}.")
print(vs)
print(f"Compare B: {B['name']}, {B['description']}, from {B['country']}.")

