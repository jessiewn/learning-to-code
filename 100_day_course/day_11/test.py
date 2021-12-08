import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def random_cards():
    return random.choice(cards)
    

#print(random_cards())
player_cards=[]
computer_cards=[]



def add_cards_to_player():
    a=random.choice(cards)
    player_cards.append(a)
add_cards_to_player()
add_cards_to_player()
print(player_cards)

def sum_score():
    sum=0
    for i in player_cards:
        sum = sum+i
        return sum
sum=sum_score
print(sum)

