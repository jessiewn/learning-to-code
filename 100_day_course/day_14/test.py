def test():

    guess=5
    answer=4
    if guess == answer:
        print(f'you are right')
        
    elif guess != answer:
        print(f"Sorry, that's wrong.")
        answer='wrong'
        return answer

def answer(A,B):
    if A>B:
        return 'A'
    if A<B:
        return 'B'
def check_answer(guess,A,B):
    if guess == answer(A,B):
        return 'right'
    else:
        return 'wrong'
    
if check_answer(guess,A['follower_count'],B['follower_count'])=='right':
        score+=1
        print(F'you are right, current score{score}')     

