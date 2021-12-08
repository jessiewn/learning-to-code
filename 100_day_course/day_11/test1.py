import random
def computer_play_randome():
    play=['y','n']
    return random. choice(play)

#computer_play_randome()




continue_play =input("Type 'y' to get another card, type 'n' to pass:")
continue_play= True
while continue_play:
    print('continue')
    continue_play =input("Type 'y' to get another card, type 'n' to pass:")
    if continue_play=='n':
        continue_play=False
        print('stop')

