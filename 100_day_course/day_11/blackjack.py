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

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards=[]
computer_cards=[]


def add_cards_to_player():
    a=random.choice(cards)
    player_cards.append(a)

def add_cards_to_computer():
    a=random.choice(cards)
    computer_cards.append(a)

#def add_cards()


def sum_score_player():
    total_score=0
    for i in player_cards:
        total_score = total_score+i
    return total_score


def sum_score_computer():
    total_score=0
    for i in computer_cards:
        total_score = total_score+i
    return total_score
    


def computer_play_randome():
    play=['y','n']
    return random.choice(play)




def main():
    play= input("Do you want to play a game of Blackjack? Type 'y' or 'n': Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play == 'n':
        return
    if play == 'y':
        print(logo)
        add_cards_to_player()
        add_cards_to_player()
        add_cards_to_computer()
        add_cards_to_computer()
        print(f'Your cards:{player_cards},curent score:{sum_score_player()}')
        print(f"computer's first card is {computer_cards[0]}")
        
        while True:
            continue_play=input("Type 'y' to get another card, type 'n' to pass:")
            if continue_play == 'y':
                add_cards_to_player()
                print(f'Your cards:{player_cards},curent score:{sum_score_player()}')
                if sum_score_player() > 21:
                    print('you lose')
                    break
            if continue_play == 'n':
                break
        while True:
            computer_choice=computer_play_randome()
            print(computer_choice)
            if computer_choice == 'y':
                add_cards_to_computer()
                print(f'Computer cards:{computer_cards},computer score:{sum_score_computer()}')
                if sum_score_computer() > 21:
                    print('player win')
                    break
            if computer_choice == 'n':
                break

        if sum_score_player() > sum_score_computer():
            print('you win')
        elif sum_score_player()<sum_score_computer():
            print('youlose')
        else:
            print('it is a draw')



main()

