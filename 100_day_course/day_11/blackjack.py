############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
from art import logo

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



def add_cards(cards):
    a=random.choice(CARDS)
    cards.append(a)

def sum_score(cards):
    total=0
    for card in cards:
        if card != 11:
            card_score = card
        else:
            if total+11>21:
                card_score=1
            else:
                card_score=11
        total+=card_score
    return total

def computer_play_randome():
    play=['y','n']
    return random.choice(play)

def computer_continue():
    play=[True,False]
    return random.choice(play)



def main():
    player_cards=[]
    computer_cards=[]
    play= input("Do you want to play a game of Blackjack? Type 'y' or 'n': Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play == 'n':
        return
    if play == 'y':
        print(logo)
        add_cards(player_cards)
        add_cards(player_cards)
        add_cards(computer_cards)
        add_cards(computer_cards)
        print(f'Your cards:{player_cards},curent score:{sum_score(player_cards)}')
        print(f"computer's first card is {computer_cards[0]}")
        if sum_score(player_cards)== 21:
            print(f'your score is {sum_score(player_cards)},you win')
        elif sum_score(computer_cards)==21:
            print(f'computer score is {sum_score(computer_cards)},you lose')
        
        while True:
            continue_play=input("Type 'y' to get another card, type 'n' to pass:")
            if continue_play == 'y':
                add_cards(player_cards)
                print(f'Your cards:{player_cards},curent score:{sum_score(player_cards)}')
                if sum_score(player_cards) > 21:
                    print('you lose')
                    break
                if sum_score(player_cards) ==21:
                    print('you win')
                    break
            if continue_play == 'n':
                break
        while True:
            if sum_score(computer_cards)<17:
                add_cards(computer_cards)
            elif sum_score(computer_cards) > 21:
                print(f'computer cards {computer_cards}, computer score is {sum_score(computer_cards)}')
                print('player win')
                break
            else:
                break
            
        if sum_score(player_cards)<21 and sum_score(computer_cards)<21 and sum_score(player_cards) > sum_score(computer_cards):
            print(f'Computer cards:{computer_cards},computer score:{sum_score(computer_cards)}')
            print('player win')
        elif sum_score(player_cards)<21 and sum_score(computer_cards)<21 and sum_score(player_cards)<sum_score(computer_cards):
            print(f'Computer cards:{computer_cards},computer score:{sum_score(computer_cards)}')
            print('player lose')
        elif sum_score(player_cards)<21 and sum_score(computer_cards)<21 and sum_score(player_cards) == sum_score(computer_cards):
            print(f'Computer cards:{computer_cards},computer score:{sum_score(computer_cards)}')
            print('it is a draw')


    


main()

