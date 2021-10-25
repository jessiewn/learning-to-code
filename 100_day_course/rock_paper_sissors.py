rock_pic = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_pic = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_pic = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rock=1
paper=0
scissors=2

# pictures = [rock_pic, paper_pic, scissors_pic]

pictures = [0,0,0]
pictures[rock] = rock_pic
pictures[scissors] = scissors_pic
pictures[paper] = paper_pic

print(pictures[rock])
